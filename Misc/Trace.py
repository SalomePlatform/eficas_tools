"""
    Ce module sert � tracer les appels aux methodes pendant
    l'ex�cution.
    Mode d'emploi :
    Au d�but de la zone � tracer faire : Trace.begin_trace()
    � la fin de la zone faire : Trace.end_trace()

"""
import sys

def begin_trace():
     sys.settrace(trace_dispatch)

def end_trace():
     sys.settrace(None)

def dispatch_call(frame, arg):
     """ Cette fonction est appel�e par trace_dispatch
         pour tracer les appels � des fonctions ou m�thodes
     """
     name = frame.f_code.co_name
     if not name: name = '???'
     print '+++ call', name, arg

def trace_dispatch(frame,event,arg):
     """ Cette fonction sert � tracer tous les appels
         � des fonctions ou � des m�thodes.
     """
     if event == 'call':
        return dispatch_call(frame, arg)
     return trace_dispatch

