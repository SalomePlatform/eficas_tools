"""
    Ce module sert à tracer les appels aux methodes pendant
    l'exécution.
    Mode d'emploi :
    Au début de la zone à tracer faire : Trace.begin_trace()
    à la fin de la zone faire : Trace.end_trace()

"""
import sys

def begin_trace():
     sys.settrace(trace_dispatch)

def end_trace():
     sys.settrace(None)

def filter(filename):
  return (filename[-10:] == 'Tkinter.py') or (filename[:21] == '/home01/chris/pkg/Pmw')

cara="+"
ldec=2
dec = cara*ldec
curframe=None

def compute_level(frame):
   """Calcule le niveau dans la pile d'execution"""
   level=0
   while frame is not None:
      frame=frame.f_back
      level=level+1
   return level-1
  

def dispatch_call(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les appels à des fonctions ou méthodes
     """
     global dec,curframe
     try:
       dec = cara*ldec*compute_level(frame)
       name = frame.f_code.co_name
       if not name: name = '???'
       if not filter(frame.f_code.co_filename):
           print dec +' call', name, frame.f_lineno,frame.f_code.co_filename
       # La trace des appels suivants est decalee de +
       dec=dec+cara*ldec
     except:
       print "Pb dans dispatch_call: ",frame,curframe
     return trace_dispatch

def dispatch_exception(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les exceptions
     """
     global dec,curframe
     try:
       dec = cara*ldec*(compute_level(frame)+1)
       name = frame.f_code.co_name
       if not name: name = '???'
       if not filter(frame.f_code.co_filename):
          print dec+' exception', name, frame.f_lineno,frame.f_code.co_filename,arg[0],arg[1]
     except:
       print "Pb dans dispatch_exception: ",frame,curframe
     return trace_dispatch

def dispatch_return(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les retours de fonction
     """
     global dec,curframe
#     print dec+' return', arg
     dec = cara*ldec*compute_level(frame)
     return trace_dispatch

def dispatch_line(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les lignes de source
     """
     import linecache
     name = frame.f_code.co_name
     if not name: name = '???'
     fn=frame.f_code.co_filename
     line = linecache.getline(fn, frame.f_lineno)
     print dec,name,frame.f_lineno,':',line.strip()
     return trace_dispatch

def trace_dispatch(frame,event,arg):
     """ Cette fonction sert à tracer tous les appels
         à des fonctions ou à des méthodes.
     """
     if event == 'call': return dispatch_call(frame, arg)
     if event == 'return': return dispatch_return(frame, arg)
#     if event == 'line': return dispatch_line(frame, arg)
     if event == 'exception': return dispatch_exception(frame, arg)
     return trace_dispatch

def a(x):
   b(x)

def b(x):
   return x

def d(x):
   return 1/x

def e():
   try:
     c=1/0
   except:
     pass

def f():
   try:
     c=1/0
   except:
     b(10)
     raise

def g():
   try:
      f()
   except:
      pass

def _test():
   begin_trace()
   a(5)
   try:
     d(0)
   except:
     pass
   b(4)
   g()
   e()  
   end_trace()
   b(3)

if __name__ == "__main__":
    _test()

