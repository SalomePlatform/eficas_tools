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

def dispatch_call(frame, arg):
     """ Cette fonction est appelée par trace_dispatch
         pour tracer les appels à des fonctions ou méthodes
     """
     name = frame.f_code.co_name
     if not name: name = '???'
     print '+++ call', name, arg

def trace_dispatch(frame,event,arg):
     """ Cette fonction sert à tracer tous les appels
         à des fonctions ou à des méthodes.
     """
     if event == 'call':
        return dispatch_call(frame, arg)
     return trace_dispatch

