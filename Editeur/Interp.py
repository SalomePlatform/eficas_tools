# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================

import Tkinter,ScrolledText
import os, sys, string, traceback 
import code

sys.ps1 = ">>> "
sys.ps2 = "... "

class PythonInterpreter( code.InteractiveConsole):
    def __init__( self, text, namespace = None):
        code.InteractiveConsole.__init__( self, namespace)
        self.text = text

    def showtraceback( self):
        start = self.text.pos + " - 1 lines"
        code.InteractiveConsole.showtraceback( self)
        end = self.text.pos
        self.text.tag_add( "exception", start, end)

class InterpWindow(Tkinter.Toplevel):
    def __init__(self,namespace, parent=None):
        Tkinter.Toplevel.__init__(self,parent)
        self._initTkWidgets()
        self.stdout = self.stderr = self
        self.pos = '1.0'
        self.history = [ '' ]
        self.hpos = 0
        self.tabCount = 0
        self.shell = PythonInterpreter( self,namespace)
        self.write("Python %s on %s\n%s\n(%s)\n" %
                       (sys.version, sys.platform, sys.copyright,
                        self.__class__.__name__))
        self.write( sys.ps1)
        self.text.focus_set()

    def _initTkWidgets( self):
        self.text = ScrolledText.ScrolledText( self, bg = "white",fg="black", wrap="word")
        self.text.pack( fill='both', expand = 1)
        self.text.bind( '<KeyPress>', self.clearMsg)
        self.text.bind( '<Return>', self.inputhandler)
        self.text.bind( '<Up>', self.uphistory)
        self.text.bind( '<Down>', self.downhistory)
        self.text.bind( '<Control-a>', self.goto_sol)
        self.text.bind( '<Control-d>', self.sendeof)
        self.text.tag_config("exception", foreground = "red")

    def swapStdFiles(self):
        sys.stdout,self.stdout = self.stdout,sys.stdout
        sys.stderr,self.stderr = self.stderr,sys.stderr

    def write(self, data):
        self.text.insert("end", data)
        self.pos = self.text.index("end - 1 char")
        self.text.yview_pickplace("end")

    def tag_add( self, tag, start, end):
        self.text.tag_add( tag, start, end)

    def inputhandler(self, *args):
        # Remove any extraneous stuff
        self.text.delete( self.pos + " lineend", "end")
        # Now get the line
        line = self.text.get(self.pos, "end - 1 char")
        self.text.insert("end", "\n")
        self.pos = self.text.index("end")
        self.addHistory( line)
        self.swapStdFiles()
        if self.shell.push( line):
            self.write(sys.ps2)
        else:
            self.write(sys.ps1)
        self.swapStdFiles()
        self.text.mark_set("insert", "end")
        return "break"

    def addHistory( self, line):
        if line:
            self.history.insert( len( self.history) - 1, line)
            self.hpos = len( self.history) - 1

    def sendeof(self, *args):
        self.destroy()
        return "break"

    def uphistory(self, event=None):
        if not self.history: return "break"

        if self.hpos > 0:
            self.hpos = self.hpos - 1

        line = self.history[ self.hpos]
        self.text.delete( self.pos, "end")
        self.text.insert( self.pos, line)

        return "break"

    def downhistory( self, event=None):
        if not self.history: return "break"

        if self.hpos < (len( self.history) - 1):
            self.hpos = self.hpos + 1

        line = self.history[ self.hpos]
        self.text.delete( self.pos, "end")
        self.text.insert( self.pos, line)

        return "break"

    def goto_sol( self, event=None):
        """
        Met en mode edition la ligne courante
        """
        self.text.mark_set( 'insert', 'insert linestart + 4 chars')
        return "break"
        
    def clearMsg( self, event=None):
        index = self.text.index( "insert")
        self.text.delete( "insert lineend", "end")
        self.tabCount = 0

if __name__ == "__main__":
    app = Tkinter.Tk()
    d={'a':1}

    def go():
      InterpWindow(d,parent=app)

    Tkinter.Button(app,text="Interp",command=go).pack()
    Tkinter.Button(app,text="Quit",command=app.destroy).pack()

    app.mainloop()

