# -*- coding: utf-8 -*-
"""
    Ce module sert à tracer les appels aux methodes pendant
    l'exécution.
    Mode d'emploi :
    Au début de la zone à tracer faire : Trace.begin_trace()
    à la fin de la zone faire : Trace.end_trace()

"""
import sys

# Variables globales
def _filter(frame):
  return 0
filter=_filter

_upcall=0
_call=1
_return=0
_exception=1
_line=0

# Paramètres
cara="+"
ldec=1

def begin_trace(filtre=None,upcall=0):
     global _upcall,filter
     if filtre: filter=filtre
     _upcall=upcall
     sys.settrace(trace_dispatch)

def end_trace():
     global _upcall,filter
     filter=_filter
     _upcall=0
     sys.settrace(None)

def compute_level(frame):
   """Calcule le niveau dans la pile d'execution"""
   level=0
   while frame is not None:
      frame=frame.f_back
      level=level+1
   return level-1

def upcall():
    frame=sys._getframe(1)
    level=compute_level(frame)
    print level*cara,frame.f_code.co_name, " : ",frame.f_code.co_filename,frame.f_lineno
    frame=frame.f_back
    print level*' ',"-> appele par : ",frame.f_code.co_name,frame.f_code.co_filename,frame.f_lineno
    
def dispatch_call(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les appels à des fonctions ou méthodes
     """
     try:
       level = ldec*(compute_level(frame)-1)
       name = frame.f_code.co_name
       if not name: name = '???'
       if not filter(frame):
           print level*cara +' call', name, frame.f_code.co_filename,frame.f_lineno
           if _upcall:
              f_back=frame.f_back
              print level*' ',"-> appele par : ",f_back.f_code.co_name,f_back.f_code.co_filename,f_back.f_lineno
     except:
       print "Pb dans dispatch_call: ",frame
     return trace_dispatch

def dispatch_exception(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les exceptions
     """
     try:
       dec = cara*ldec*(compute_level(frame)+0)
       name = frame.f_code.co_name
       if not name: name = '???'
       if not filter(frame):
          print dec,name,'exception',frame.f_code.co_filename,frame.f_lineno,arg[0],arg[1]
     except:
       print "Pb dans dispatch_exception: ",frame
     return trace_dispatch

def dispatch_return(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les retours de fonction
     """
     dec = cara*ldec*compute_level(frame)
     name = frame.f_code.co_name
     if not name: name = '???'
     print dec,name,'return', arg
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
     dec = cara*ldec*compute_level(frame)
     print dec,name,':',line.strip(),frame.f_lineno
     return trace_dispatch

def trace_dispatch(frame,event,arg):
     """ Cette fonction sert à tracer tous les appels
         à des fonctions ou à des méthodes.
     """
     if _call and event == 'call': return dispatch_call(frame, arg)
     if _return and event == 'return': return dispatch_return(frame, arg)
     if _line and event == 'line': return dispatch_line(frame, arg)
     if _exception and event == 'exception': return dispatch_exception(frame, arg)
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
   def filter(frame):
       return not frame.f_code.co_name == 'a'

   begin_trace(filtre=filter,upcall=1)
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

