#include <qobject.h>
#include <qwidget.h>
#include <qsocketnotifier.h> 
#include <qtimer.h>

#include <tcl.h>
EXTERN int              TclInExit _ANSI_ARGS_((void));

class Notifier;

typedef struct FileHandler {
    int fd;
    int mask;                   /* Mask of desired events: TCL_READABLE, etc. */
    int readyMask;              /* Events that have been seen since the
                                   last time FileHandlerEventProc was called
                                   for this file. */
    Notifier *qtNotifier;
    Tcl_FileProc *proc;         /* Procedure to call, in the style of
                                 * Tcl_CreateFileHandler. */
    ClientData clientData;      /* Argument to pass to proc. */
    struct FileHandler *nextPtr;/* Next in list of all files we care about. */
} FileHandler;

class Notifier : public QObject
{
    Q_OBJECT
public:
    Notifier(FileHandler *,int);
public slots:
    void dataReceived();
    void dataWritable();
    void dataExcept();
private: 
    QSocketNotifier *sn;
    FileHandler *fhdr;
};

class Filter : public QObject
{
public:
    Filter();
    bool eventFilter( QObject *, QEvent * );
    int mustFilter;
};

class Timer : public QObject
{
    Q_OBJECT
public:
    Timer();
    QTimer *timer;
public slots:
    void timeout();
};

