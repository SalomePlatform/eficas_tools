#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
using namespace std;
#include <iostream>
#include <sys/time.h>
#include <Python.h>
#include <sip.h>

/*
 * With Qt version 3.0, we must use this horrible hack : #define private public
 * With Qt version > 3.0, this no more needed
 * So commentarize #define QT30, with Qt version > 3.0
 */
#undef QT32
#define QT30
#ifdef QT30
#define private public /* We need to use processNextEvent(),
                             therefore we need
                             access to the internal variables. */
#include <qapplication.h>
#undef private /* On revient au normal */
#else
#include <qapplication.h>
#include <qeventloop.h>
#endif

#include <qsocketnotifier.h>


#include "notify.h"
#include <tk.h>

extern "C" void QtFileProc(FileHandler *,int);
extern "C" void QtTimerProc();
extern "C" bool processQtEvent(bool );
extern "C" int qtlooplevel();
extern "C" void notifierFilter(int );

//#define _DEBUG_
# ifdef _DEBUG_
# define HERE {cout<<flush ; cerr << "- Trace " << __FILE__ << " [" << __LINE__ << "] : " << flush ;}
# define SCRUTE(var) {HERE ; cerr << #var << "=" << var << endl ;}
# define MESSAGE(chain) {HERE ; cerr << chain << endl ;}
#else
# define HERE
# define SCRUTE(var)
# define MESSAGE(chain)
#endif

extern "C" int qtlooplevel(){
#ifdef QT30
   return qApp->loopLevel();
#else
   return qApp->eventLoop()->loopLevel();
#endif
}

extern "C" bool processQtEvent(bool canWait)
{
    bool flag;
    /*
     * This function is called by WaitForEvent (internal loop of 
     * Tcl Notifier) so only some Qt events will be taken in account.
     * We install a filter on qApp
     * before processing next qt event with wait.
     */
    notifierFilter(1);
#ifdef QT30
    flag= qApp->processNextEvent(canWait);
#else
    if(canWait){
       flag= qApp->eventLoop()->processEvents(QEventLoop::AllEvents | QEventLoop::WaitForMore );
    }else{
       flag= qApp->eventLoop()->processEvents(QEventLoop::AllEvents );
    }
#endif
    notifierFilter(0);
    return flag;
}

/*
 *  This object (Notifier) calls QtFileProc when some data is present
 *  on f->fd socket (Tk X11 socket)
 */
Notifier::Notifier(FileHandler *f,int mask):QObject()
    {
      fhdr=f;
      if (mask & TCL_READABLE){
        sn = new QSocketNotifier( f->fd, QSocketNotifier::Read );
        QObject::connect( sn, SIGNAL(activated(int)), this, SLOT(dataReceived()) );
      }else if (mask & TCL_WRITABLE){
        sn = new QSocketNotifier( f->fd, QSocketNotifier::Write );
        QObject::connect( sn, SIGNAL(activated(int)), this, SLOT(dataWritable()) );
      }else if (mask & TCL_EXCEPTION){
        sn = new QSocketNotifier( f->fd, QSocketNotifier::Exception );
        QObject::connect( sn, SIGNAL(activated(int)), this, SLOT(dataExcept()) );
      }
    }

void Notifier::dataReceived()
    {
        //fprintf(stderr,"dataReceived\n");
        QtFileProc(fhdr,TCL_READABLE);
    }
void Notifier::dataWritable()
    {
        //fprintf(stderr,"dataWritable\n");
        QtFileProc(fhdr,TCL_WRITABLE);
    }
void Notifier::dataExcept()
    {
        //fprintf(stderr,"dataExcept\n");
        QtFileProc(fhdr,TCL_EXCEPTION);
    }

Timer::Timer():QObject()
{
      // Create a QT timer
      timer= new QTimer(this);
      // Connect it    
      connect( timer, SIGNAL(timeout()), this,SLOT(timeout()) );
      // but don't start it
}
void Timer::timeout()
{
   MESSAGE("timeout");
   /*
    * QT timer associated to Tcl notifier has fired
    * stop it
    * and call Tcl notifier function QtTimerProc
    */
   timer->stop();
   QtTimerProc();
}


Filter::Filter():QObject()
{
   mustFilter=0;
   // Install it as an application-global event filter to catch ...
   SCRUTE(qApp);
   qApp->installEventFilter( this );
}

bool Filter::eventFilter( QObject *obj, QEvent *event )
{
   MESSAGE("Filter::eventFilter");
   SCRUTE(event->type());
   if (mustFilter){
      /*
       * We are in a modal TK loop (WaitForEvent has been called)
       * so we ignore some Qt events
       */
      if(event->type() == QEvent::MouseButtonPress) return TRUE; 
      if(event->type() == QEvent::MouseButtonRelease)return TRUE;
      if(event->type() == QEvent::MouseButtonDblClick)return TRUE;
      //if(event->type() == QEvent::KeyPress)return TRUE;
      if(event->type() == 6)return TRUE; 
      //if(event->type() == QEvent::KeyRelease)return TRUE;
      if(event->type() == 7)return TRUE; 
      // We don't allow to close Qt windows in Tk modal loop
      if(event->type() == QEvent::Close)return TRUE;
   }
   return QObject::eventFilter( obj, event ); // don't eat event
}

/*
 * The following structure is what is added to the Tcl event queue when
 * file handlers are ready to fire.
 */

typedef struct FileHandlerEvent {
    Tcl_Event header;           /* Information that is standard for
                                 * all events. */
    int fd;                     /* File descriptor that is ready.  Used
                                 * to find the FileHandler structure for
                                 * the file (can't point directly to the
                                 * FileHandler structure because it could
                                 * go away while the event is queued). */
} FileHandlerEvent;

/*
 * The following static structure contains the state information for the
 * Qt based implementation of the Tcl notifier.
 */

static struct NotifierState {
    int currentTimeout;
    Filter *filter;
    Timer *timer;
    FileHandler *firstFileHandlerPtr;   /* Pointer to head of file handler
                                         * list. */
} notifier;

/*
 * The following static indicates whether this module has been initialized.
 */
static int initialized = 0;

extern "C" void  InitNotifier (void);

static Tk_RestrictAction EventRestrictProc(ClientData arg, XEvent *eventPtr)
{
   /*
    * We are in a modal QT loop (qApp->loopLevel() > 1)
    * so we ignore some TK events
    */
   //printf("event : %d\n",eventPtr->type);
   if (qtlooplevel() == 1) return TK_PROCESS_EVENT;
   if(eventPtr->type == ButtonRelease)return TK_DISCARD_EVENT;
   if(eventPtr->type == ButtonPress)return TK_DISCARD_EVENT;
   if(eventPtr->type == KeyRelease)return TK_DISCARD_EVENT;
   if(eventPtr->type == KeyPress)return TK_DISCARD_EVENT;
   if(eventPtr->type == MotionNotify)return TK_DISCARD_EVENT;
   return TK_PROCESS_EVENT;
}

static void restrictevents()
{
    ClientData info,oldArg;
    //if (qtlooplevel()>1) Tk_RestrictEvents(EventRestrictProc,&info,&oldArg);
    if (qtlooplevel()>0) Tk_RestrictEvents(EventRestrictProc,&info,&oldArg);
    else Tk_RestrictEvents(NULL,&info,&oldArg);
}
/*
 *----------------------------------------------------------------------
 *
 * SetTimer --
 *
 *      This procedure sets the current notifier timeout value.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      Replaces any previous timer.
 *
 * This function starts or stops the notifier timer
 * It called when Tcl_SetTime(xxx) is called
 * This notifier timer calls QtTimerProc when timer event occurs
 *----------------------------------------------------------------------
 */

static void
SetTimer(Tcl_Time *timePtr)
         /* Timeout value, may be NULL. */
{
    long timeout;
    MESSAGE("SetTimer");

    if (!initialized) {
        InitNotifier();
    }

    if (notifier.currentTimeout != 0) {
        // stopQtTimer();
        // printf("stop timer \n");
        notifier.timer->timer->stop();
        notifier.currentTimeout = 0;
    }
    if (timePtr) {
        timeout = timePtr->sec * 1000 + timePtr->usec / 1000;
        // startQtTimer(timeout);
        // printf("start timer %ld\n",timeout);
        notifier.timer->timer->start(timeout);
        notifier.currentTimeout = 1;
    }
}

/*
 *  Ask _tkinter to service all pending events
 */

static void DoEvents()
{
  long ret=1;
  MESSAGE("DoEvents");
  SIP_BLOCK_THREADS
  //Tcl_ServiceAll();
  PyObject * tkinter=PyImport_ImportModule("_tkinter");
  while(ret==1){
    // Process one Tcl event without blocking
    MESSAGE("dooneevent call");
    PyObject *res=PyObject_CallMethod(tkinter,"dooneevent","i",2);
    if(!res){
      PyErr_Print();
      SIP_UNBLOCK_THREADS
      return;
    }
    ret= PyInt_AsLong(res);
    SCRUTE(ret);
    Py_DECREF(res);
    //SCRUTE(res->ob_refcnt);
    // usleep(20000);
  }

  Py_DECREF(tkinter);
  SCRUTE(tkinter->ob_refcnt);
  SIP_UNBLOCK_THREADS
  MESSAGE("end of DoEvents");
  return;
}

/*
 * If running is 1, we have already called DoEvents and so dooneevent from
 * _tkinter module. It's a recursive call so don't call again DoEvents
 * it will block.We are in Tcl so it's safe to call directly Tcl_ServiceAll.
 * If running is 0, we are running out of _tkinter module so we must
 * call Tcl_ServiceAll through dooneevent from _tkinter module
 */
static int running=1;
static int waitfor=0;
/*
 * ServiceAll could be called recursively so be careful
 */
static void ServiceAll()
{
  if(running==1){
    // It's safe to call directly Tcl_ServiceAll
    Tcl_ServiceAll();
  }else if(waitfor==1){
    // It's safe to call directly Tcl_ServiceAll
    Tcl_ServiceAll();
  }else{
    // Call Tcl_ServiceAll through Python _tkinter module interface
    // to have safe state
    running=1;
    DoEvents();
    running=0;
  }
}
/*
 *----------------------------------------------------------------------
 *
 * QtTimerProc --
 *
 *      This procedure is the QtTimerCallbackProc used to handle
 *      timeouts.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      Processes all queued events.
 *
 * This function is declared to the Tcl notifier 
 *     notifierprocs.setTimerProc = SetTimer;
 *  Tcl_SetNotifier(&notifierprocs);
 *  This function is called when a timer event occurs
 *----------------------------------------------------------------------
 */

void QtTimerProc()
{
    MESSAGE("QtTimerProc");
    restrictevents();
    ServiceAll();
}

/*
 *----------------------------------------------------------------------
 *
 * CreateFileHandler --
 *
 *      This procedure registers a file handler with the Qt notifier.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      Creates a new file handler structure and registers one or more
 *      input procedures with Qt.
 *
 *----------------------------------------------------------------------
 * CCAR:
 *    Cette procedure est appelee par Tcl via le notifier (notifier.createFileHandlerProc)
 *    Elle est chargée d'enregistrer dans la boucle Qt un file handler dont le file
 * descripteur sera celui de la connexion X spécifique de Tk.
 *   Ainsi on peut deriver le traitement des evenements X de Tk vers les procedures
 *   qui sont localisées dans ce fichier
 * This function is declared to the Tcl notifier 
 *  notifierprocs.createFileHandlerProc = CreateFileHandler
 *  Tcl_SetNotifier(&notifierprocs);
 * Then Tcl calls it during initialization : ????
 */

static void
CreateFileHandler(int fd, int mask, Tcl_FileProc proc, ClientData clientData)
/*    int fd;                        Handle of stream to watch. 
 *    int mask;                      OR'ed combination of TCL_READABLE,
 *                                 TCL_WRITABLE, and TCL_EXCEPTION:
 *                                 indicates conditions under which
 *                                 proc should be called. 
 *  Tcl_FileProc *proc;            Procedure to call for each
 *                                 selected event. 
 *  ClientData clientData;         Arbitrary data to pass to proc. 
 */
{
    FileHandler *filePtr;

    MESSAGE("CreateFileHandler");

    if (!initialized) {
        InitNotifier();
    }

    for (filePtr = notifier.firstFileHandlerPtr; filePtr != NULL;
            filePtr = filePtr->nextPtr) {
        if (filePtr->fd == fd) {
            break;
        }
    }
    if (filePtr == NULL) {
        filePtr = (FileHandler*) ckalloc(sizeof(FileHandler));
        filePtr->fd = fd;
        filePtr->readyMask = 0;
        filePtr->mask = 0;
        filePtr->nextPtr = notifier.firstFileHandlerPtr;
        notifier.firstFileHandlerPtr = filePtr;
    }
    filePtr->proc = proc;
    filePtr->clientData = clientData;
    /*
     * Enregistrement avec la boucle Qt
     *  Toute activité sur le file descripteur fd (connexion X spécifique Tk)
     *  sera détectée et redirigée vers la procédure QtFileProc
     * Create a Notifier object to redirect X11 events present on socket filePtr->fd
     * towards QtFileProc
     */
    filePtr->qtNotifier=new Notifier(filePtr,mask);

    filePtr->mask = mask;
}

/*
 *----------------------------------------------------------------------
 *
 * DeleteFileHandler --
 *
 *      Cancel a previously-arranged callback arrangement for
 *      a file.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      If a callback was previously registered on file, remove it.
 *
 *----------------------------------------------------------------------
 */

static void
DeleteFileHandler(int fd)
/*
 *  int fd;                      Stream id for which to remove
 *                               callback procedure. 
 */
{
    FileHandler *filePtr, *prevPtr;

    if (!initialized) {
        InitNotifier();
    }

    /*
     * Find the entry for the given file (and return if there
     * isn't one).
     */

    for (prevPtr = NULL, filePtr = notifier.firstFileHandlerPtr; ;
            prevPtr = filePtr, filePtr = filePtr->nextPtr) {
        if (filePtr == NULL) {
            return;
        }
        if (filePtr->fd == fd) {
            break;
        }
    }

    /*
     * Clean up information in the callback record.
     */

    if (prevPtr == NULL) {
        notifier.firstFileHandlerPtr = filePtr->nextPtr;
    } else {
        prevPtr->nextPtr = filePtr->nextPtr;
    }
    /*
     * Destruction du notifier Qt
     */
    delete filePtr->qtNotifier;

    ckfree((char *) filePtr);
}

static int FileHandlerEventProc(Tcl_Event *evPtr, int flags);
/*
 *----------------------------------------------------------------------
 *
 * QtFileProc --
 *
 *      These procedures are called by Qt when a file becomes readable,
 *      writable, or has an exception.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      Makes an entry on the Tcl event queue if the event is
 *      interesting.
 *
 *----------------------------------------------------------------------
 *  Lorsqu'une activité est detectée sur le file descripteur fd cette
 *  procédure crée un evenement Tcl qu'elle rajoute dans la queue Tcl
 *  Elle demande ensuite de servir (Tcl_ServiceAll) tous les evenements
 *  Tcl présents dans la queue Tcl
 *  L'evenement est créé avec comme procédure de traitement associée FileHandlerEventProc
 */

void QtFileProc(FileHandler *filePtr,int mask)
{
    FileHandlerEvent *fileEvPtr;
    MESSAGE("QtFileProc");

    /*
     * Ignore unwanted or duplicate events.
     */

    if (!(filePtr->mask & mask) || (filePtr->readyMask & mask)) {
        return;
    }

    /*
     * This is an interesting event, so put it onto the event queue.
     *  On demande qu'il soit traité avec la procédure FileHandlerEventProc
     */

    filePtr->readyMask |= mask;

    fileEvPtr = (FileHandlerEvent *) ckalloc(sizeof(FileHandlerEvent));
    fileEvPtr->header.proc = FileHandlerEventProc;
    fileEvPtr->fd = filePtr->fd;
    Tcl_QueueEvent((Tcl_Event *) fileEvPtr, TCL_QUEUE_TAIL);

    /*
     * Process events on the Tcl event queue before returning to Qt.
     */

    // On entre dans la boucle de traitement des evenements Tcl (retour vers Python?)
    /*
     * L'evenement file sera traité ce qui conduit à mettre les evenements X
     * dans la queue Tcl. Ces evenements (X) seront alors traités dans la foulée
     * La source d'evenement X enregistrée par Tcl_CreateEventSource est egalement
     * consultée pendant cette phase (assertion a verifier)
     */

    restrictevents();
    ServiceAll();

    // On revient vers la boucle Qt
}

/*
 *----------------------------------------------------------------------
 *
 * FileHandlerEventProc --
 *
 *      This procedure is called by Tcl_ServiceEvent when a file event
 *      reaches the front of the event queue.  This procedure is
 *      responsible for actually handling the event by invoking the
 *      callback for the file handler.
 *
 * Results:
 *      Returns 1 if the event was handled, meaning it should be removed
 *      from the queue.  Returns 0 if the event was not handled, meaning
 *      it should stay on the queue.  The only time the event isn't
 *      handled is if the TCL_FILE_EVENTS flag bit isn't set.
 *
 * Side effects:
 *      Whatever the file handler's callback procedure does.
 *
 *----------------------------------------------------------------------
 */

static int
FileHandlerEventProc(Tcl_Event *evPtr, int flags)
/*
 *  Tcl_Event *evPtr;            Event to service. 
 *  int flags;                   Flags that indicate what events to
 *                               handle, such as TCL_FILE_EVENTS. 
 */
{
    FileHandler *filePtr;
    FileHandlerEvent *fileEvPtr = (FileHandlerEvent *) evPtr;
    int mask;
    MESSAGE("FileHandlerEventProc");

    if (!(flags & TCL_FILE_EVENTS)) {
        return 0;
    }

    /*
     * Search through the file handlers to find the one whose handle matches
     * the event.  We do this rather than keeping a pointer to the file
     * handler directly in the event, so that the handler can be deleted
     * while the event is queued without leaving a dangling pointer.
     */

    for (filePtr = notifier.firstFileHandlerPtr; filePtr != NULL;
            filePtr = filePtr->nextPtr) {
        if (filePtr->fd != fileEvPtr->fd) {
            continue;
        }

        /*
         * The code is tricky for two reasons:
         * 1. The file handler's desired events could have changed
         *    since the time when the event was queued, so AND the
         *    ready mask with the desired mask.
         * 2. The file could have been closed and re-opened since
         *    the time when the event was queued.  This is why the
         *    ready mask is stored in the file handler rather than
         *    the queued event:  it will be zeroed when a new
         *    file handler is created for the newly opened file.
         */

        mask = filePtr->readyMask & filePtr->mask;
        filePtr->readyMask = 0;
        if (mask != 0) {
            // On utilise ici la procédure enregistrée avec le file handler
            // Normalement il s'agit de DisplayFileProc (fichier unix/tkUnixEvent.c de Tk)
            (*filePtr->proc)(filePtr->clientData, mask);
        }
        break;
    }
    return 1;
}


/*
 *----------------------------------------------------------------------
 *
 * WaitForEvent --
 *
 *      This function is called by Tcl_DoOneEvent to wait for new
 *      events on the message queue.  If the block time is 0, then
 *      Tcl_WaitForEvent just polls without blocking.
 *
 * Results:
 *      Returns 1 if an event was found, else 0.  This ensures that
 *      Tcl_DoOneEvent will return 1, even if the event is handled
 *      by non-Tcl code.
 *
 * Side effects:
 *      Queues file events that are detected by the select.
 *
 *----------------------------------------------------------------------
 */

static int
WaitForEvent(
    Tcl_Time *timePtr)          /* Maximum block time, or NULL. */
{
    int ret;
    //bool old_app_exit_loop;
    int timeout;
    MESSAGE("WaitForEvent");

    if (!initialized) {
        InitNotifier();
    }

    //SCRUTE(Tk_GetNumMainWindows());
    //if(Tk_GetNumMainWindows()<1){
       // That should not have happened. quit now ???
       //qApp->quit();
    //}

    if (timePtr) {
        // Wait with timeout
        MESSAGE("Have timeout");
        timeout = timePtr->sec * 1000 + timePtr->usec / 1000;
        if (timeout == 0) {
            // Try to process one event without waiting
            MESSAGE("Process an event without waiting");
            /*
             * We are already in Tkinter module so Tcl calls
             * should be done directly without using DoEvents
             * wrapping
             */
	    SCRUTE(running);
            waitfor=1;
            ret=processQtEvent(FALSE);
	    waitfor=0;
            if (ret) {
                MESSAGE("Qt event caught");
                // an event has been proccessed
                return 1;
            } else {
                // no event has been proccessed
                MESSAGE("No Qt event caught");
                return 0;
            }
        } else {
            MESSAGE("Start the timer");
            Tcl_SetTimer(timePtr);
        }
    } else {
      // timePtr == NULL, blocking wait of an event
    }
    // Blocking wait
    MESSAGE("Wait an event");
    SCRUTE(running);
    waitfor=1;
    ret=processQtEvent(TRUE);
    waitfor=0;
/*
    if(ret==FALSE && qApp->app_exit_loop == TRUE){
      MESSAGE("Critical : qt loop is ended and we will loop forever");
      old_app_exit_loop = qApp->app_exit_loop;
      qApp->app_exit_loop=FALSE;
      processQtEvent(TRUE);
      qApp->app_exit_loop=old_app_exit_loop;
    }
*/
    return 1;
}

/*
 *----------------------------------------------------------------------
 *
 * NotifierExitHandler --
 *
 *      This function is called to cleanup the notifier state before
 *      Tcl is unloaded.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      Destroys the notifier window.
 *
 *----------------------------------------------------------------------
 */

static void
NotifierExitHandler(
    ClientData clientData)      /* Not used. */
{
    delete notifier.timer;
    delete notifier.filter;

    for (; notifier.firstFileHandlerPtr != NULL; ) {
        Tcl_DeleteFileHandler(notifier.firstFileHandlerPtr->fd);
    }
    initialized = 0;
}

/*
 *----------------------------------------------------------------------
 *
 * InitNotifier --
 *
 *      Initializes the notifier state.
 *
 * Results:
 *      None.
 *
 * Side effects:
 *      Creates a new exit handler.
 *
 *----------------------------------------------------------------------
 * La procedure InitNotifier doit etre appelée avant d'initialiser Tcl et Tk
 * par Tcl_Init et Tk_Init
 * Tcl_SetNotifier enregistre les procedures du notifier aupres de Tcl
 * et en particulier notifier.createFileHandlerProc en tant que tclStubs.tcl_CreateFileHandler
 * lui meme appelé par Tcl_CreateFileHandler qui est appelé à l'initialisation par
 * TkpOpenDisplay avec comme argument proc : DisplayFileProc
 * TkpOpenDisplay est lui meme appelé par GetScreen qui est appelé à l'initialisation
 * par CreateTopLevelWindow
 *
 * Tk_Init appelle Initialize qui
 *  1 - crée une toplevel par appel à TkCreateFrame
 *      cette création a comme effet de bord l'appel à GetScreen
 *  2 - appelle TkpInit qui réalise des initialisations spécifiques
 *      dont TkCreateXEventSource() qui crée une source d'évenements Tcl par
 *      Tcl_CreateEventSource(DisplaySetupProc, DisplayCheckProc, NULL);
 *      Cette source est enregistrée dans la liste des sources qui mémorise
 *      les procédures dans source->setupProc et source->checkProc
 *      Les sources sont appelées par Tcl_ServiceAll qui appelle Tcl_ServiceEvent
 *      qui traite un evenement
 *
 * La procédure DisplayFileProc appelle TransferXEventsToTcl qui met les evenements
 * X dans la queue Tk en appelant Tk_QueueWindowEvent
 * Tk_QueueWindowEvent appelle soit Tcl_DoWhenIdle soit Tcl_QueueEvent pour mettre
 * cet evenement dans la queue Tcl
 * Tcl_QueueEvent appelle QueueEvent qui fait le travail
 *
 */

extern "C" void InitNotifier()
{
    MESSAGE("InitNotifier");

    /*
     * Only reinitialize if we are not in exit handling. The notifier
     * can get reinitialized after its own exit handler has run, because
     * of exit handlers for the I/O and timer sub-systems (order dependency).
     */

    if (TclInExit()) {
        return;
    }
    initialized = 1;
    memset(&notifier, 0, sizeof(notifier));
    notifier.timer= new Timer();
    notifier.filter= new Filter();

    Tcl_SetServiceMode(TCL_SERVICE_ALL);
}

ClientData
initNotifierProc()
{
return (ClientData) 0;
}

void InitNotifierProcs()
{
    Tcl_NotifierProcs notifierprocs;
    MESSAGE("InitNotifierProcs");
    memset(&notifierprocs, 0, sizeof(notifierprocs));
    notifierprocs.createFileHandlerProc = CreateFileHandler;
    notifierprocs.deleteFileHandlerProc = DeleteFileHandler;
    notifierprocs.setTimerProc = SetTimer;
    notifierprocs.waitForEventProc = WaitForEvent;
#if TCL_MINOR_VERSION > 3
    notifierprocs.initNotifierProc = initNotifierProc;
#endif
    MESSAGE("Tcl_SetNotifier");
    Tcl_SetNotifier(&notifierprocs);
    MESSAGE("Tcl_CreateExitHandler");
    Tcl_CreateExitHandler(NotifierExitHandler, NULL);
}

extern "C" void notifierFilter(int filter)
{
    notifier.filter->mustFilter=filter;
}

static PyMethodDef Module_Methods[] =
  {
    {NULL, NULL}
  };

extern "C" void initnotifqt()
{
PyObject *m;
static char modulename[] = "notifqt";
MESSAGE("initnotifqt");
// Protect Tcl notifier if qApp is not started
if(qApp) InitNotifierProcs();
/*
 * If the module is linked with the right lib (qt-mt)
 * this module and libqtcmodule share global variables as qApp
 * and others
 */
// We are called from Python so initialize the ServiceAll trick.
running=0;
m = Py_InitModule(modulename, Module_Methods);
}
