"""
   Ce module contient la fonction utilitaire centerwindow
   qui sert à centrer une fenetre
"""
import types

def centerwindow(window,parent = 'avec'):
    if parent =='avec':
        parent = window.winfo_parent()
        if type(parent) == types.StringType:
            parent = window._nametowidget(parent)
    # Find size of window.
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    if width == 1 and height == 1:
        # If the window has not yet been displayed, its size is
        # reported as 1x1, so use requested size.
        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()
    # Place in centre of screen:
    if parent =='avec' :
        x = (window.winfo_screenwidth() - width) / 2 - parent.winfo_vrootx()
        y = (window.winfo_screenheight() - height) / 3 - parent.winfo_vrooty()
    else:
        x = (window.winfo_screenwidth() - width) / 2 
        y = (window.winfo_screenheight() - height) / 3
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    window.geometry('+%d+%d' % (x, y))
    
