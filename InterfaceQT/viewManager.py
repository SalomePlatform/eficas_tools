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

import os
from InterfaceQT import utilIcons 
from qt import *


##fonctions utilitaires
def normabspath(path):
    """
    Function returning a normalized, absolute path.
    
    @param path file path (string)
    @return absolute, normalized path (string)
    """
    return os.path.abspath(path)
    
    
def samepath(f1, f2):
    """
    Function to compare two paths.
    
    @param f1 first path for the compare (string)
    @param f2 second path for the compare (string)
    @return flag indicating whether the two paths represent the
        same path on disk.
    """
    if f1 is None or f2 is None:
        return 0
        
    if normcasepath(f1) == normcasepath(f2):
        return 1
        
    return 0

def normcasepath(path):
    """
    Function returning a path, that is normalized with respect to its case and references.
    
    @param path file path (string)
    @return case normalized path (string)
    """
    return os.path.normcase(os.path.normpath(path))    
    



class ViewManager:
    """
    Base class inherited by all specific viewmanager classes.
    
    It defines the interface to be implemented by specific
    viewmanager classes and all common methods.
    
    @signal lastEditorClosed emitted after the last editor window was closed
    @signal editorOpened(string) emitted after an editor window was opened
    @signal editorSaved(string) emitted after an editor window was saved
    @signal checkActions(editor) emitted when some actions should be checked
            for their status
    @signal cursorChanged(editor) emitted after the cursor position of the active
            window has changed
    @signal breakpointToggled(editor) emitted when a breakpoint is toggled.
    @signal bookmarkToggled(editor) emitted when a bookmark is toggled.
    """
    def __init__(self, ui ):
        """
        Constructor
        
        @param ui reference to the main user interface
        @param dbs reference to the debug server object
        """
        # initialize the instance variables
        self.ui = ui
        self.appliEficas = ui
        self.editors = []
        self.doubles = {}
        self.currentEditor = None
        self.untitledCount = 0
        self.srHistory = {"search" : QStringList(), "replace" : QStringList()}
        self.editorsCheckFocusIn = 1
        self.recent =  QStringList()      
                
        
        # initialize the central store for api information (used by
        # autocompletion and calltips)
        self.apis = {}
        self.initFileFilters()
        
        
    def initFileFilters(self):
        """
        Private method to initialize the lists of supported filename filters.
        """
        self.fileFiltersString = self.trUtf8(\
            'Python Files (*.py);;'
            'Aster Files (*.com*);;'
            'Pyrex Files (*.pyx);;'
            'Quixote Template Files (*.ptl);;'
            'IDL Files (*.idl);;'
            'C Files (*.h *.c);;'
            'C++ Files (*.h *.hpp *.hh *.cxx *.cpp *.cc);;'
            'C# Files (*.cs);;'
            'HTML Files (*.html *.htm *.asp *.shtml *.css);;'
            'PHP Files (*.php *.php3 *.php4 *.php5 *.phtml);;'
            'XML Files (*.xml *.xsl *.xslt *.dtd);;'
            'Java Files (*.java);;'
            'JavaScript Files (*.js);;'
            'SQL Files (*.sql);;'
            'Docbook Files (*.docbook);;'
            'Perl Files (*.pl *.pm *.ph);;'
            'Shell Files (*.sh);;'
            'Aster Files (*.com*);;'
            'All Files (*)')

        fileFilters = QStringList.split(';;', self.fileFiltersString)
        
        self.ext2Filter = {}
        for fileFilter in fileFilters:
            extensions = QStringList.split('*', fileFilter)
            for extension in extensions[1:]:
                extension = unicode(extension).strip().replace(')', '')
                if extension:
                    self.ext2Filter[extension] = unicode(fileFilter)
        
        
        
    #####################################################################
    ## methods above need to be implemented by a subclass
    #####################################################################
    
    def canSplit(self):
        """
        public method to signal if splitting of the view is available.
        
        @return flag indicating splitting of the view is available.
        """
        return 0
        
    def addSplit(self):
        """
        Public method used to split the current view.
        """
        pass
        
    def removeSplit(self):
        """
        Public method used to remove the current split view.
        
        @return Flag indicating successful deletion
        """
        return 0
        
    def setSplitOrientation(self, orientation):
        """
        Public method used to set the orientation of the split view.
        
        @param orientation orientation of the split
                (QSplitter.Horizontal or QSplitter.Vertical)
        """
        pass
        
    def eventFilter(self, object, event):
        """
        Private method called to filter an event.
        
        @param object object, that generated the event (QObject)
        @param event the event, that was generated by object (QEvent)
        @return flag indicating if event was filtered out
        """
        return 0
        
    def focusInEvent(self, event):
        """
        Public method called when the viewmanager receives focus.
        
        @param event the event object (QFocusEvent)
        """
        self.editorActGrp.setEnabled(1)
        
    def focusOutEvent(self, event):
        """
        Public method called when the viewmanager loses focus.
        
        @param event the event object (QFocusEvent)
        """
        self.editorActGrp.setEnabled(0)
        
    
    def initEditMenu(self):
        """
        Public method to create the Edit menu
        
        @return the generated menu
        """
        menu = QPopupMenu(self.ui)
        menu.insertTearOffHandle()
        self.undoAct.addTo(menu)
        self.redoAct.addTo(menu)
        self.revertAct.addTo(menu)
        menu.insertSeparator()
        self.cutAct.addTo(menu)
        self.copyAct.addTo(menu)
        self.pasteAct.addTo(menu)
        self.deleteAct.addTo(menu)
        menu.insertSeparator()
        self.indentAct.addTo(menu)
        self.unindentAct.addTo(menu)
        menu.insertSeparator()
        self.commentAct.addTo(menu)
        self.uncommentAct.addTo(menu)
        self.streamCommentAct.addTo(menu)
        self.boxCommentAct.addTo(menu)
        menu.insertSeparator()
        self.autoCompleteAct.addTo(menu)
        self.autoCompleteFromDocAct.addTo(menu)
        self.autoCompleteFromAPIsAct.addTo(menu)
        menu.insertSeparator()
        self.searchAct.addTo(menu)
        self.searchAgainAct.addTo(menu)
        self.replaceAct.addTo(menu)
        menu.insertSeparator()
        self.searchFilesAct.addTo(menu)
        menu.insertSeparator()
        self.gotoAct.addTo(menu)
        self.gotoBraceAct.addTo(menu)
        menu.insertSeparator()
        self.selectBraceAct.addTo(menu)
        self.selectAllAct.addTo(menu)
        self.deselectAllAct.addTo(menu)
        menu.insertSeparator()
        self.shortenEmptyAct.addTo(menu)
        self.convertEOLAct.addTo(menu)
        
        return menu
        
    def initEditToolbar(self):
        """
        Public method to create the Edit toolbar
        
        @return the generated toolbar
        """
        tb = QToolBar(self.ui)
        self.undoAct.addTo(tb)
        self.redoAct.addTo(tb)
        tb.addSeparator()
        self.cutAct.addTo(tb)
        self.copyAct.addTo(tb)
        self.pasteAct.addTo(tb)
        self.deleteAct.addTo(tb)
        tb.addSeparator()
        self.indentAct.addTo(tb)
        self.unindentAct.addTo(tb)
        tb.addSeparator()
        self.commentAct.addTo(tb)
        self.uncommentAct.addTo(tb)
        
        return tb
        
    ##################################################################
    ## Initialize the search related actions, search menu and toolbar
    ##################################################################
    
    def initSearchActions(self):
        """
        Private method defining the user interface actions for the search commands.
        """
        self.searchActGrp = QActionGroup(self)
        
        self.searchAct = QAction(self.trUtf8('Search'),
                QIconSet(utilIcons.getPixmap("find.png")),
                self.trUtf8('&Search...'),
                QKeySequence(self.trUtf8("CTRL+F","Search|Search")),
                self.searchActGrp)
        self.searchAct.setStatusTip(self.trUtf8('Search for a text'))
        self.searchAct.setWhatsThis(self.trUtf8(
            """<b>Search</b>"""
            """<p>Search for some text in the current editor. A"""
            """ dialog is shown to enter the searchtext and options"""
            """ for the search.</p>"""
        ))
        self.connect(self.searchAct,SIGNAL('activated()'),self.handleSearch)
        self.searchActions.append(self.searchAct)
        
        self.searchAgainAct = QAction(self.trUtf8('Search again'),
                QIconSet(utilIcons.getPixmap("findNext.png")),
                self.trUtf8('Search &again'),
                Qt.Key_F3,self.searchActGrp)
        self.searchAgainAct.setStatusTip(self.trUtf8('Search again for text'))
        self.searchAgainAct.setWhatsThis(self.trUtf8(
            """<b>Search again</b>"""
            """<p>Search again for some text in the current editor."""
            """ The previously entered searchtext and options are reused.</p>"""
        ))
        self.connect(self.searchAgainAct,SIGNAL('activated()'),self.searchDlg.handleFindNext)
        self.searchActions.append(self.searchAgainAct)
        
        self.replaceAct = QAction(self.trUtf8('Replace'),
                self.trUtf8('&Replace...'),
                QKeySequence(self.trUtf8("CTRL+R","Search|Replace")),
                self.searchActGrp)
        self.replaceAct.setStatusTip(self.trUtf8('Replace some text'))
        self.replaceAct.setWhatsThis(self.trUtf8(
            """<b>Replace</b>"""
            """<p>Search for some text in the current editor and replace it. A"""
            """ dialog is shown to enter the searchtext, the replacement text"""
            """ and options for the search and replace.</p>"""
        ))
        self.connect(self.replaceAct,SIGNAL('activated()'),self.handleReplace)
        self.searchActions.append(self.replaceAct)
        
        self.gotoAct = QAction(self.trUtf8('Goto Line'),
                QIconSet(utilIcons.getPixmap("goto.png")),
                self.trUtf8('&Goto Line...'),
                QKeySequence(self.trUtf8("CTRL+G","Search|Goto Line")),
                self.searchActGrp)
        self.gotoAct.setStatusTip(self.trUtf8('Goto Line'))
        self.gotoAct.setWhatsThis(self.trUtf8(
            """<b>Goto Line</b>"""
            """<p>Go to a specific line of text in the current editor."""
            """ A dialog is shown to enter the linenumber.</p>"""
        ))
        self.connect(self.gotoAct,SIGNAL('activated()'),self.handleGoto)
        self.searchActions.append(self.gotoAct)
        
        self.gotoBraceAct = QAction(self.trUtf8('Goto Brace'),
                QIconSet(utilIcons.getPixmap("gotoBrace.png")),
                self.trUtf8('Goto &Brace'),
                QKeySequence(self.trUtf8("CTRL+L","Search|Goto Brace")),
                self.searchActGrp)
        self.gotoBraceAct.setStatusTip(self.trUtf8('Goto Brace'))
        self.gotoBraceAct.setWhatsThis(self.trUtf8(
            """<b>Goto Brace</b>"""
            """<p>Go to the matching brace in the current editor.</p>"""
        ))
        self.connect(self.gotoBraceAct,SIGNAL('activated()'),self.handleGotoBrace)
        self.searchActions.append(self.gotoBraceAct)
        
        self.searchActGrp.setEnabled(0)
        
        self.searchFilesAct = QAction(self.trUtf8('Search in Files'),
                QIconSet(utilIcons.getPixmap("projectFind.png")),
                self.trUtf8('Search in &Files...'),
                QKeySequence(self.trUtf8("SHIFT+CTRL+F","Search|Search Files")),
                self)
        self.searchFilesAct.setStatusTip(self.trUtf8('Search for a text in files'))
        self.searchFilesAct.setWhatsThis(self.trUtf8(
            """<b>Search in Files</b>"""
            """<p>Search for some text in the files of a directory tree"""
            """ or the project. A dialog is shown to enter the searchtext"""
            """ and options for the search and to display the result.</p>"""
        ))
        self.connect(self.searchFilesAct,SIGNAL('activated()'),self.handleSearchFiles)
        self.searchActions.append(self.searchFilesAct)
        
        
    ##################################################################
    ## Initialize the view related actions, view menu and toolbar
    ##################################################################
    
    def initViewActions(self):
        """
        Protected method defining the user interface actions for the view commands.
        """
        self.viewActGrp = QActionGroup(self)
        self.viewFoldActGrp = QActionGroup(self)

        self.zoomInAct = QAction(self.trUtf8('Zoom in'),
                            QIconSet(utilIcons.getPixmap("zoomIn.png")),
                            self.trUtf8('Zoom &in'),
                            Qt.CTRL+Qt.Key_Plus, self.viewActGrp)
        self.zoomInAct.setStatusTip(self.trUtf8('Zoom in on the text'))
        self.zoomInAct.setWhatsThis(self.trUtf8(
                """<b>Zoom in</b>"""
                """<p>Zoom in on the text. This makes the text bigger.</p>"""
                ))
        self.connect(self.zoomInAct,SIGNAL('activated()'),self.handleZoomIn)
        self.viewActions.append(self.zoomInAct)
        
        self.zoomOutAct = QAction(self.trUtf8('Zoom out'),
                            QIconSet(utilIcons.getPixmap("zoomOut.png")),
                            self.trUtf8('Zoom &out'),
                            Qt.CTRL+Qt.Key_Minus, self.viewActGrp)
        self.zoomOutAct.setStatusTip(self.trUtf8('Zoom out on the text'))
        self.zoomOutAct.setWhatsThis(self.trUtf8(
                """<b>Zoom out</b>"""
                """<p>Zoom out on the text. This makes the text smaller.</p>"""
                ))
        self.connect(self.zoomOutAct,SIGNAL('activated()'),self.handleZoomOut)
        self.viewActions.append(self.zoomOutAct)
        
        self.zoomToAct = QAction(self.trUtf8('Zoom'),
                            QIconSet(utilIcons.getPixmap("zoomTo.png")),
                            self.trUtf8('&Zoom'),
                            0, self.viewActGrp)
        self.zoomToAct.setStatusTip(self.trUtf8('Zoom the text'))
        self.zoomToAct.setWhatsThis(self.trUtf8(
                """<b>Zoom</b>"""
                """<p>Zoom the text. This opens a dialog where the"""
                """ desired size can be entered.</p>"""
                ))
        self.connect(self.zoomToAct,SIGNAL('activated()'),self.handleZoom)
        self.viewActions.append(self.zoomToAct)
        
        self.toggleAllAct = QAction(self.trUtf8('Toggle all folds'),
                            self.trUtf8('Toggle &all folds'),
                            0, self.viewFoldActGrp)
        self.toggleAllAct.setStatusTip(self.trUtf8('Toggle all folds'))
        self.toggleAllAct.setWhatsThis(self.trUtf8(
                """<b>Toggle all folds</b>"""
                """<p>Toggle all folds of the current editor.</p>"""
                ))
        self.connect(self.toggleAllAct,SIGNAL('activated()'),self.handleToggleAll)
        self.viewActions.append(self.toggleAllAct)
        
        self.toggleCurrentAct = QAction(self.trUtf8('Toggle current fold'),
                            self.trUtf8('Toggle &current fold'),
                            0, self.viewFoldActGrp)
        self.toggleCurrentAct.setStatusTip(self.trUtf8('Toggle current fold'))
        self.toggleCurrentAct.setWhatsThis(self.trUtf8(
                """<b>Toggle current fold</b>"""
                """<p>Toggle the folds of the current line of the current editor.</p>"""
                ))
        self.connect(self.toggleCurrentAct,SIGNAL('activated()'),self.handleToggleCurrent)
        self.viewActions.append(self.toggleCurrentAct)
        
        self.unhighlightAct = QAction(self.trUtf8('Remove all highlights'),
                            QIconSet(utilIcons.getPixmap("unhighlight.png")),
                            self.trUtf8('Remove all highlights'),
                            0, self)
        self.unhighlightAct.setStatusTip(self.trUtf8('Remove all highlights'))
        self.unhighlightAct.setWhatsThis(self.trUtf8(
                """<b>Remove all highlights</b>"""
                """<p>Remove the highlights of all editors.</p>"""
                ))
        self.connect(self.unhighlightAct,SIGNAL('activated()'),self.unhighlight)
        self.viewActions.append(self.unhighlightAct)
        
        self.splitViewAct = QAction(self.trUtf8('Split view'),
                            QIconSet(utilIcons.getPixmap("splitVertical.png")),
                            self.trUtf8('&Split view'),
                            0, self)
        self.splitViewAct.setStatusTip(self.trUtf8('Add a split to the view'))
        self.splitViewAct.setWhatsThis(self.trUtf8(
                """<b>Split view</b>"""
                """<p>Add a split to the view.</p>"""
                ))
        self.connect(self.splitViewAct,SIGNAL('activated()'),self.handleSplitView)
        self.viewActions.append(self.splitViewAct)
        
        self.splitOrientationAct = QAction(self.trUtf8('Arrange horizontally'),
                            self.trUtf8('Arrange &horizontally'),
                            0, self, None, 1)
        self.splitOrientationAct.setStatusTip(self.trUtf8('Arrange the splitted views horizontally'))
        self.splitOrientationAct.setWhatsThis(self.trUtf8(
                """<b>Arrange horizontally</b>"""
                """<p>Arrange the splitted views horizontally.</p>"""
                ))
        self.splitOrientationAct.setOn(0)
        self.connect(self.splitOrientationAct,SIGNAL('activated()'),self.handleSplitOrientation)
        self.viewActions.append(self.splitOrientationAct)
        
        self.splitRemoveAct = QAction(self.trUtf8('Remove split'),
                            QIconSet(utilIcons.getPixmap("remsplitVertical.png")),
                            self.trUtf8('&Remove split'),
                            0, self)
        self.splitRemoveAct.setStatusTip(self.trUtf8('Remove the current split'))
        self.splitRemoveAct.setWhatsThis(self.trUtf8(
                """<b>Remove split</b>"""
                """<p>Remove the current split.</p>"""
                ))
        self.connect(self.splitRemoveAct,SIGNAL('activated()'),self.removeSplit)
        self.viewActions.append(self.splitRemoveAct)
        
        self.viewActGrp.setEnabled(0)
        self.viewFoldActGrp.setEnabled(0)
        self.unhighlightAct.setEnabled(0)
        self.splitViewAct.setEnabled(0)
        self.splitOrientationAct.setEnabled(0)
        self.splitRemoveAct.setEnabled(0)
        
    def initViewMenu(self):
        """
        Public method to create the View menu
        
        @return the generated menu
        """
        menu = QPopupMenu(self.ui)
        menu.insertTearOffHandle()
        self.viewActGrp.addTo(menu)
        menu.insertSeparator()
        self.viewFoldActGrp.addTo(menu)
        menu.insertSeparator()
        self.unhighlightAct.addTo(menu)
        if self.canSplit():
            menu.insertSeparator()
            self.splitViewAct.addTo(menu)
            self.splitOrientationAct.addTo(menu)
            self.splitRemoveAct.addTo(menu)       
        return menu
        
    def initViewToolbar(self):
        """
        Public method to create the View toolbar
        
        @return the generated toolbar
        """
        tb = QToolBar(self.ui)
        self.viewActGrp.addTo(tb)
        tb.addSeparator()
        self.unhighlightAct.addTo(tb)
        if self.canSplit():
            tb.addSeparator()
            self.splitViewAct.addTo(tb)
            self.splitRemoveAct.addTo(tb)
        
        return tb
        
    ##################################################################
    ## Initialize the macro related actions and macro menu
    ##################################################################
    
    def initMacroActions(self):
        """
        Private method defining the user interface actions for the macro commands.
        """
        self.macroActGrp = QActionGroup(self)

        self.macroStartRecAct = QAction(self.trUtf8('Start Macro Recording'),
                            self.trUtf8('S&tart Macro Recording'),
                            0, self.macroActGrp)
        self.macroStartRecAct.setStatusTip(self.trUtf8('Start Macro Recording'))
        self.macroStartRecAct.setWhatsThis(self.trUtf8(
                """<b>Start Macro Recording</b>"""
                """<p>Start recording editor commands into a new macro.</p>"""
                ))
        self.connect(self.macroStartRecAct,SIGNAL('activated()'),self.handleMacroStartRecording)
        self.macroActions.append(self.macroStartRecAct)
        
        self.macroStopRecAct = QAction(self.trUtf8('Stop Macro Recording'),
                            self.trUtf8('Sto&p Macro Recording'),
                            0, self.macroActGrp)
        self.macroStopRecAct.setStatusTip(self.trUtf8('Stop Macro Recording'))
        self.macroStopRecAct.setWhatsThis(self.trUtf8(
                """<b>Stop Macro Recording</b>"""
                """<p>Stop recording editor commands into a new macro.</p>"""
                ))
        self.connect(self.macroStopRecAct,SIGNAL('activated()'),self.handleMacroStopRecording)
        self.macroActions.append(self.macroStopRecAct)
        
        self.macroRunAct = QAction(self.trUtf8('Run Macro'),
                            self.trUtf8('&Run Macro'),
                            0, self.macroActGrp)
        self.macroRunAct.setStatusTip(self.trUtf8('Run Macro'))
        self.macroRunAct.setWhatsThis(self.trUtf8(
                """<b>Run Macro</b>"""
                """<p>Run a previously recorded editor macro.</p>"""
                ))
        self.connect(self.macroRunAct,SIGNAL('activated()'),self.handleMacroRun)
        self.macroActions.append(self.macroRunAct)
        
        self.macroDeleteAct = QAction(self.trUtf8('Delete Macro'),
                            self.trUtf8('&Delete Macro'),
                            0, self.macroActGrp)
        self.macroDeleteAct.setStatusTip(self.trUtf8('Delete Macro'))
        self.macroDeleteAct.setWhatsThis(self.trUtf8(
                """<b>Delete Macro</b>"""
                """<p>Delete a previously recorded editor macro.</p>"""
                ))
        self.connect(self.macroDeleteAct,SIGNAL('activated()'),self.handleMacroDelete)
        self.macroActions.append(self.macroDeleteAct)
        
        self.macroLoadAct = QAction(self.trUtf8('Load Macro'),
                            self.trUtf8('&Load Macro'),
                            0, self.macroActGrp)
        self.macroLoadAct.setStatusTip(self.trUtf8('Load Macro'))
        self.macroLoadAct.setWhatsThis(self.trUtf8(
                """<b>Load Macro</b>"""
                """<p>Load an editor macro from a file.</p>"""
                ))
        self.connect(self.macroLoadAct,SIGNAL('activated()'),self.handleMacroLoad)
        self.macroActions.append(self.macroLoadAct)
        
        self.macroSaveAct = QAction(self.trUtf8('Save Macro'),
                            self.trUtf8('&Save Macro'),
                            0, self.macroActGrp)
        self.macroSaveAct.setStatusTip(self.trUtf8('Save Macro'))
        self.macroSaveAct.setWhatsThis(self.trUtf8(
                """<b>Save Macro</b>"""
                """<p>Save a previously recorded editor macro to a file.</p>"""
                ))
        self.connect(self.macroSaveAct,SIGNAL('activated()'),self.handleMacroSave)
        self.macroActions.append(self.macroSaveAct)
        
        self.macroActGrp.setEnabled(0)
        
    def initMacroMenu(self):
        """
        Public method to create the Macro menu
        
        @return the generated menu
        """
        menu = QPopupMenu(self.ui)
        menu.insertTearOffHandle()
        self.macroActGrp.addTo(menu)
        return menu
    

    def checkDirty(self, editor):
        """
        Private method to check dirty status and open a message window.
        
        @param editor editor window to check
        @return flag indicating successful reset of the dirty flag (boolean)
        """        
     
        if (editor.modified) and (editor in self.doubles.keys()) :
            res = QMessageBox.warning(
                     None,
                     self.trUtf8("Fichier Duplique"),
                     self.trUtf8("Le fichier ne sera pas sauvegarde."),
                     self.trUtf8("&Quitter"), 
                     self.trUtf8("&Annuler"))
            if res == 0 : return 1
            return 0
        if editor.modified:
            fn = editor.getFileName()
            if fn is None:
                fn = self.trUtf8('Noname')
            res = QMessageBox.warning(self.parent(), 
                self.trUtf8("Fichier Modifie"),
                self.trUtf8("Le fichier <b>%1</b> n a pas ete sauvegarde.")
                    .arg(fn),
                self.trUtf8("&Sauvegarder"), self.trUtf8("&Quitter "),
                self.trUtf8("&Annuler"), 0, 2)
            if res == 0:
                (ok, newName) = editor.saveFile()
                if ok:
                    self.setEditorName(editor, newName)
                return ok
            elif res == 2:
                return  0
        return 1
        
    def checkAllDirty(self):
        """
        Public method to check the dirty status of all editors.
        
        @return flag indicating successful reset of all dirty flags (boolean)
        """
        for editor in self.editors:
            if not self.checkDirty(editor):
                return 0
                
        return 1
        
    def closeEditor(self, editor):
        """
        Private method to close an editor window.
        
        @param editor editor window to be closed
        @return flag indicating success (boolean)
        """
        # save file if necessary
        if not self.checkDirty(editor):
            return 0
            
        # remove the window
        self.removeView(editor)
        self.editors.remove(editor)        
        if not len(self.editors):
            self.handleLastEditorClosed()
            self.emit(PYSIGNAL('lastEditorClosed'), ()) #CS_pbruno connecter signal avec l'appli
        return 1
    
    def handleClose(self):
        """
        Public method to close the current window.
        
        @return flag indicating success (boolean)
        """
        aw = self.activeWindow()
        if aw is None:
            return 0
            
        res = self.closeEditor(aw)
        if res and aw == self.currentEditor:
            self.currentEditor = None
            
        return res
        
    def handleNewView(self):
        """
        Public method to close the current window.
        
        @return flag indicating success (boolean)
        """
        aw = self.activeWindow()
        if aw is None:
            return 0
            
        aw.handleNewView()
        
            
    def handleCloseAll(self):
        """
        Private method to close all editor windows via file menu.
        """
        savedEditors = self.editors[:]
        retour=1
        for editor in savedEditors:
            retour=retour*self.closeEditor(editor)
        return retour
            
    def handleCloseWindow(self, fn):
        """
        Public method to close an arbitrary source editor.
        
        @param fn filename of editor to be closed
        @return flag indicating success (boolean)
        """
        for editor in self.editors:
            if samepath(fn, editor.getFileName()):
                break
        else:
            return 1
            
        res = self.closeEditor(editor)
        if res and editor == self.currentEditor:
            self.currentEditor = None
            
        return res
        
    def handleExit(self):
        """
        Public method to handle the debugged program terminating.
        """
        if self.currentEditor is not None:
            self.currentEditor.highlight()
            self.currentEditor = None
            
        self.setSbFile()

    def handlePythonFile(self,pyfn,lineno=None):
        """
        Public method to handle the user selecting a file for display.
        
        @param pyfn name of file to be opened
        @param lineno line number to place the cursor at
        """
        try:
            self.displayPythonFile(pyfn,lineno)
        except IOError:
            pass

        
    def displayJDC(self,jdc,fn=None):
        """
        Public slot to display a file in an editor.
        
        @param fn name of file to be opened
        @param lineno line number to place the cursor at
        """        
        titre=None
        if fn != None : titre=fn.split("/")[-1]
        newWin, editor = self.getEditor(None, jdc, title = titre )
        
        if newWin:
            editor.fileName=fn
            self.handleModificationStatusChanged(editor.modified, editor)
        self.checkActions(editor)
        
        # insert filename into list of recently opened files
        self.addToRecentList(editor.getFileName())


        
    def newEditorView(self, fn, caller):
        """
        Public method to create a new editor displaying the given document.
        
        @param fn filename of this view
        @param caller reference to the editor calling this method        
        """
        from editor import JDCEditor
        editor = JDCEditor(fn, None, self, editor=caller)
        self.editors.append(editor)
        self.connect(editor, PYSIGNAL('modificationStatusChanged'),
            self.handleModificationStatusChanged)
        self.connect(editor, PYSIGNAL('cursorChanged'), self.handleCursorChanged)
        self.connect(editor, PYSIGNAL('editorSaved'), self.handleEditorSaved)
        self.connect(editor, PYSIGNAL('breakpointToggled'), self.handleBreakpointToggled)
        self.connect(editor, PYSIGNAL('bookmarkToggled'), self.handleBookmarkToggled)
        self.connect(editor, PYSIGNAL('syntaxerrorToggled'), self.handleSyntaxErrorToggled)
        self.connect(editor, PYSIGNAL('autoCompletionAPIsAvailable'), 
            self.handleEditoracAPIsAvailable)
        self.handleEditorOpened()
        self.emit(PYSIGNAL('editorOpened'), (fn,))
        
        self.connect(caller, PYSIGNAL('editorRenamed'), editor.handleRenamed)
        self.connect(editor, PYSIGNAL('editorRenamed'), caller.handleRenamed)
        
        self.addView(editor, fn)
        self.handleModificationStatusChanged(editor.modified, editor)
        self.checkActions(editor)
        
    def addToRecentList(self, fn):
        """
        Public slot to add a filename to the list of recently opened files.
        
        @param fn name of the file to be added
        """
        self.recent.remove(fn)
        self.recent.prepend(fn)
        if len(self.recent) > 9:
            self.recent = self.recent[:9]

    def toggleWindow(self,w):
        """
        Private method to toggle a workspace window.
        
        @param w editor window to be toggled
        """
        if w.isHidden():
            w.show()
        else:
            w.hide()

    def setFileLine(self,fn,line,error=0,syntaxError=0):
        """
        Public method to update the user interface when the current program or line changes.
        
        @param fn filename of editor to update (string)
        @param line line number to highlight (int)
        @param error flag indicating an error highlight (boolean)
        @param syntaxError flag indicating a syntax error
        """
        self.setSbFile(fn,line)

        try:
            newWin, self.currentEditor = self.getEditor(fn)
        except IOError:
            return

        # Change the highlighted line.
        self.currentEditor.highlight(line,error,syntaxError)

        self.currentEditor.highlightVisible()
        self.checkActions(self.currentEditor, 0)
            
    def setSbFile(self,fn=None,line=None,pos=None):
        """
        Private method to set the file info in the status bar.
        
        @param fn filename to display (string)
        @param line line number to display (int)
        @param pos character position to display (int)
        """
        if fn is None:
            fn = ''
            writ = '   '
        else:
            if QFileInfo(fn).isWritable():
                writ = ' rw'
            else:
                writ = ' ro'
        
        self.sbWritable.setText(writ)
        self.sbFile.setText(self.trUtf8('File: %1').arg(fn,-50))

        if line is None:
            line = ''

        self.sbLine.setText(self.trUtf8('Line: %1').arg(line,5))

        if pos is None:
            pos = ''
            
        self.sbPos.setText(self.trUtf8('Pos: %1').arg(pos, 5))
        
    def unhighlight(self, current=0):
        """
        Public method to switch off all highlights.
        
        @param current flag indicating only the current editor should be unhighlighted
                (boolean)
        """
        if current: 
            if self.currentEditor is not None:
                self.currentEditor.highlight()
        else:
            for editor in self.editors:
                editor.highlight()

    def getOpenFilenames(self):
        """
        Public method returning a list of the filenames of all editors.
        
        @return list of all opened filenames (list of strings)
        """
        filenames = []
        for editor in self.editors:
            fn = editor.getFileName()
            if fn is not None:
                filenames.append(fn)
                
        return filenames
                
    def getEditor(self, fn, jdc = None, title = None, units = None):
        """
        Private method to return the editor displaying the given file.
        
        If there is no editor with the given file, a new editor window is
        created.
        
        @param fn filename to look for
        @param isPythonFile flag indicating that this is a Python file
                even if it doesn't have the .py extension (boolean)
        @return tuple of two values giving a flag indicating a new window creation and
            a reference to the editor displaying this file
        """
        newWin = 0
        double=None
        for editor in self.editors:
            if samepath(fn, editor.getFileName()):
               abort = QMessageBox.warning(self,
                        self.trUtf8("Fichier"),
                        self.trUtf8("Le fichier <b>%1</b> est deja ouvert.Voulez-vous l ouvrir tel qu'il etait lors du dernier enregistrement") .arg(fn),
                        self.trUtf8("&Duplication"),
                        self.trUtf8("&Annuler"), None, 1)
               if abort:
                        break
               double=editor
        else:
            from editor import JDCEditor
            editor = JDCEditor(fn, jdc, self,units=units)
            if double != None :
               self.doubles[editor]=double
               #self.doubles[double]=editor
            if editor.jdc: # le fichier est bien un jdc            
                self.editors.append(editor)
                self.connect(editor, PYSIGNAL('modificationStatusChanged'),
                    self.handleModificationStatusChanged)
                self.connect(editor, PYSIGNAL('cursorChanged'), self.handleCursorChanged)
                self.connect(editor, PYSIGNAL('editorSaved'), self.handleEditorSaved)
                self.connect(editor, PYSIGNAL('breakpointToggled'), self.handleBreakpointToggled)
                self.connect(editor, PYSIGNAL('bookmarkToggled'), self.handleBookmarkToggled)
                self.connect(editor, PYSIGNAL('syntaxerrorToggled'), self.handleSyntaxErrorToggled)
                self.connect(editor, PYSIGNAL('autoCompletionAPIsAvailable'), 
                    self.handleEditoracAPIsAvailable)
                self.handleEditorOpened()
                self.emit(PYSIGNAL('editorOpened'), (fn,))
                newWin = 1
            else:
                editor.closeIt()

        if newWin:
            self.addView(editor, fn , title)
        elif editor.jdc:
            self.showView(editor, fn)
            
        return (newWin, editor)
        
        
    def getOpenEditor(self, fn):
        """
        Public method to return the editor displaying the given file.
        
        @param fn filename to look for
        @return a reference to the editor displaying this file or None, if
            no editor was found
        """
        for editor in self.editors:
            if samepath(fn, editor.getFileName()):
                return editor
                
        return None

    def getActiveName(self):
        """
        Public method to retrieve the filename of the active window.
        
        @return filename of active window (string)
        """
        aw = self.activeWindow()
        if aw:
            return aw.getFileName()
        else:
            return None

    def saveEditor(self, fn):
        """
        Public method to save a named editor file.
        
        @param fn filename of editor to be saved (string)
        @return flag indicating success (boolean)
        """
        for editor in self.editors:
            if samepath(fn, editor.getFileName()):
                break
        else:
            return 1
            
        if not editor.modified:
            return 1
        else:
            ok, dummy = editor.saveFile()
            return ok
        
    def saveCurrentEditor(self):
        """
        Public slot to save the contents of the current editor.
        """
        aw = self.activeWindow()
        if aw in self.doubles.keys() :
           QMessageBox.warning(
                     None,
                     self.trUtf8("Fichier Duplique"),
                     self.trUtf8("Le fichier ne sera pas sauvegarde."),
                     self.trUtf8("&Annuler"))
           return
        if aw:
            ok, newName = aw.saveFile()
            if ok:
                self.setEditorName(aw, newName)
        else:
            return

    def saveAsCurrentEditor(self):
        """
        Public slot to save the contents of the current editor to a new file.
        """
        aw = self.activeWindow()
        if aw:
            ok, newName = aw.saveFileAs()
            if ok:
                self.setEditorName(aw, newName)
        else:
            return

    def saveAllEditors(self):
        """
        Public slot to save the contents of all editors.
        """
        for editor in self.editors:
            ok, newName = editor.saveFile()
            if ok:
                self.setEditorName(editor, newName)
        
        # restart autosave timer
        if self.autosaveInterval > 0:
            self.autosaveTimer.start(self.autosaveInterval * 60000, 1)

    def saveCurrentEditorToProject(self):
        """
        Public slot to save the contents of the current editor to the current project.
        """
        pro = self.ui.getProject()
        path = pro.ppath
        aw = self.activeWindow()
        if aw:
            ok, newName = aw.saveFileAs(path)
            if ok:
                self.setEditorName(aw, newName)
                pro.appendFile(newName)
        else:
            return
        
    def newIncludeEditor(self) :
        self.newEditor(include=1)
        
    def newEditor(self,include=0):
        """
        Public slot to generate a new empty editor.
        """
        from editor import JDCEditor
        editor = JDCEditor(None,None,self,include=include)
        
        self.editors.append(editor)
        self.connect(editor, PYSIGNAL('modificationStatusChanged'),
            self.handleModificationStatusChanged)
        self.connect(editor, PYSIGNAL('cursorChanged'), self.handleCursorChanged)
        self.connect(editor, PYSIGNAL('editorSaved'),   self.handleEditorSaved)
        self.connect(editor, PYSIGNAL('breakpointToggled'), self.handleBreakpointToggled)
        self.connect(editor, PYSIGNAL('bookmarkToggled'), self.handleBookmarkToggled)
        self.connect(editor, PYSIGNAL('syntaxerrorToggled'), self.handleSyntaxErrorToggled)
        self.connect(editor, PYSIGNAL('autoCompletionAPIsAvailable'), 
            self.handleEditoracAPIsAvailable)
        self.addView(editor, None)
        self.handleEditorOpened()
        self.checkActions(editor)
        self.emit(PYSIGNAL('editorOpened'), (None,))
        
    def printCurrentEditor(self):
        """
        Public slot to print the contents of the current editor.
        """
        aw = self.activeWindow()
        if aw:
            aw.printFile()
        else:
            return

    def printCurrentEditorSel(self):
        """
        Public slot to print the selection of the current editor.
        """
        aw = self.activeWindow()
        if aw:
            aw.printSelection()
        else:
            return

    def handlevisuJdcPy(self):
        if self.activeWindow()== None : return
        self.activeWindow().viewJdcPy()
        
    def handleViewJdcFichierSource(self):
        if self.activeWindow()== None : return
        self.activeWindow().viewJdcSource()
                
    def handleViewJdcRapport(self):
        if self.activeWindow()== None : return
        self.activeWindow().viewJdcRapport()
        
    def handleNewProject(self):
        """
        Public slot to handle the NewProject signal.
        """
        self.saveToProjectAct.setEnabled(1)
        
    def handleProjectOpened(self):
        """
        Public slot to handle the projectOpened signal.
        """
        self.saveToProjectAct.setEnabled(1)
        
    def handleProjectClosed(self):
        """
        Public slot to handle the projectClosed signal.
        """
        self.saveToProjectAct.setEnabled(0)
        
    def handleProjectFileRenamed(self, oldfn, newfn):
        """
        Public slot to handle the projectFileRenamed signal.
        
        @param oldfn old filename of the file (string)
        @param newfn new filename of the file (string)
        """
        editor = self.getOpenEditor(oldfn)
        if editor:
            editor.fileRenamed(newfn)
        
    def enableEditorsCheckFocusIn(self, enabled):
        """
        Public method to set a flag enabling the editors to perform focus in checks.
        
        @param enabled flag indicating focus in checks should be performed (boolean)
        """
        self.editorsCheckFocusIn = enabled
        
    def editorsCheckFocusInEnabled(self):
        """
        Public method returning the flag indicating editors should perform focus in checks.
        
        @return flag indicating focus in checks should be performed (boolean)
        """
        return self.editorsCheckFocusIn

    def handleFindFileName(self):
        """
        Private method to handle the search for file action.
        """
        self.ui.findFileNameDialog.show()
        self.ui.findFileNameDialog.raiseW()
        self.ui.findFileNameDialog.setActiveWindow()
        
    ##################################################################
    ## Below are the action methods for the edit menu
    ##################################################################
    
    def handleEditUndo(self):
        """
        Private method to handle the undo action.
        """
        self.activeWindow().undo()
        
    def handleEditRedo(self):
        """
        Private method to handle the redo action.
        """
        self.activeWindow().redo()
        
    def handleEditRevert(self):
        """
        Private method to handle the revert action.
        """
        self.activeWindow().revertToUnmodified()
        
    def handleEditCut(self):
        """
        Private method to handle the cut action.
        """
        self.activeWindow().cut()
        
    def handleEditCopy(self):
        """
        Private method to handle the copy action.
        """
        self.activeWindow().copy()
        
    def handleEditPaste(self):
        """
        Private method to handle the paste action.
        """
        self.activeWindow().paste()
        
    def handleEditDelete(self):
        """
        Private method to handle the delete action.
        """
        self.activeWindow().clear()
        
    def handleEditIndent(self):
        """
        Private method to handle the indent action.
        """
        self.activeWindow().indentLineOrSelection()
        
    def handleEditUnindent(self):
        """
        Private method to handle the unindent action.
        """
        self.activeWindow().unindentLineOrSelection()
        
    def handleEditComment(self):
        """
        Private method to handle the comment action.
        """
        self.activeWindow().commentLineOrSelection()
        
    def handleEditUncomment(self):
        """
        Private method to handle the uncomment action.
        """
        self.activeWindow().uncommentLineOrSelection()
        
    def handleEditStreamComment(self):
        """
        Private method to handle the stream comment action.
        """
        self.activeWindow().streamCommentLineOrSelection()
        
    def handleEditBoxComment(self):
        """
        Private method to handle the box comment action.
        """
        self.activeWindow().boxCommentLineOrSelection()
        
    def handleEditSelectBrace(self):
        """
        Private method to handle the select to brace action.
        """
        self.activeWindow().selectToMatchingBrace()
        
    def handleEditSelectAll(self):
        """
        Private method to handle the select all action.
        """
        self.activeWindow().selectAll(1)
        
    def handleEditDeselectAll(self):
        """
        Private method to handle the select all action.
        """
        self.activeWindow().selectAll(0)
        
    def handleConvertEOL(self):
        """
        Private method to handle the convert line end characters action.
        """
        aw = self.activeWindow()
        aw.convertEols(aw.eolMode())
        
    def handleShortenEmptyLines(self):
        """
        Private method to handle the shorten empty lines action.
        """
        self.activeWindow().handleShortenEmptyLines()
        
    def handleEditAutoComplete(self):
        """
        Private method to handle the autocomplete action.
        """
        aw = self.activeWindow()
        aw.autoComplete()
        
    def handleEditAutoCompleteFromDoc(self):
        """
        Private method to handle the autocomplete from document action.
        """
        aw = self.activeWindow()
        aw.autoCompleteFromDocument()
        
    def handleEditAutoCompleteFromAPIs(self):
        """
        Private method to handle the autocomplete from APIs action.
        """
        aw = self.activeWindow()
        aw.autoCompleteFromAPIs()
        
    def handleEditoracAPIsAvailable(self, available):
        """
        Private method to handle the availability of API autocompletion signal.
        """
        self.autoCompleteFromAPIsAct.setEnabled(available)
        
    ##################################################################
    ## Below are the action and utility methods for the search menu
    ##################################################################

    def getWord(self, text, index):
        """
        Private method to get the word at a position.
        
        @param text text to look at (string or QString)
        @param index position to look at (int)
        @return the word at that position
        """
        re = QRegExp('[^\w_]')
        start = text.findRev(re, index) + 1
        end = text.find(re, index)
        if end > start:
            word = text.mid(start, end-start)
        else:
            word = QString('')
        return word
        
    def textForFind(self):
        """
        Private method to determine the selection or the current word for the next find operation.
        
        @return selection or current word (QString)
        """
        aw = self.activeWindow()
        if aw is None:
            return ''
            
        if aw.hasSelectedText():
            text = aw.selectedText()
            if text.contains('\r') or text.contains('\n'):
                # the selection contains at least a newline, it is
                # unlikely to be the expression to search for
                return ''
                
            return text
            
        # no selected text, determine the word at the current position
        line, index = aw.getCursorPosition()
        return self.getWord(aw.text(line), index)
        
    def getSRHistory(self, key):
        """
        Private method to get the search or replace history list.
        
        @param key list to return (must be 'search' or 'replace')
        @return the requested history list (QStringList)
        """
        return self.srHistory[key]
        
    def handleSearch(self):
        """
        Private method to handle the search action.
        """
        self.searchDlg.showFind(self.textForFind())
        
    def handleReplace(self):
        """
        Private method to handle the replace action.
        """
        self.replaceDlg.showReplace(self.textForFind())
        
    def handleGoto(self):
        """
        Private method to handle the goto action.
        """
        aw = self.activeWindow()
        dlg = GotoDialog(self.ui, None, 1)
        dlg.selectAll()
        if dlg.exec_loop() == QDialog.Accepted:
            aw.gotoLine(min(dlg.getLinenumber(), aw.lines()))
        
    def handleGotoBrace(self):
        """
        Private method to handle the goto brace action.
        """
        self.activeWindow().moveToMatchingBrace()
        
    def handleSearchFiles(self):
        """
        Private method to handle the search in files action.
        """
        self.ui.findFilesDialog.show(self.textForFind())
        self.ui.findFilesDialog.raiseW()
        self.ui.findFilesDialog.setActiveWindow()
        
    ##################################################################
    ## Below are the action methods for the view menu
    ##################################################################
    
    def handleZoomIn(self):
        """
        Private method to handle the zoom in action.
        """
        self.activeWindow().zoomIn()
        
    def handleZoomOut(self):
        """
        Private method to handle the zoom out action.
        """
        self.activeWindow().zoomOut()
        
    def handleZoom(self):
        """
        Private method to handle the zoom action.
        """
        aw = self.activeWindow()
        dlg = ZoomDialog(aw.getZoom(), self.ui, None, 1)
        if dlg.exec_loop() == QDialog.Accepted:
            aw.zoomTo(dlg.getZoomSize())
            
    def handleToggleAll(self):
        """
        Private method to handle the toggle all folds action.
        """
        self.activeWindow().foldAll()
        
    def handleToggleCurrent(self):
        """
        Private method to handle the toggle current fold action.
        """
        aw = self.activeWindow()
        line, index = aw.getCursorPosition()
        aw.foldLine(line)
        
    def handleSplitView(self):
        """
        Private method to handle the split view action.
        """
        self.addSplit()
        
    def handleSplitOrientation(self):
        """
        Private method to handle the split orientation action.
        """
        if self.splitOrientationAct.isOn():
            self.setSplitOrientation(QSplitter.Horizontal)
            self.splitViewAct.setIconSet(\
                QIconSet(utilIcons.getPixmap("splitHorizontal.png")))
            self.splitRemoveAct.setIconSet(\
                QIconSet(utilIcons.getPixmap("remsplitHorizontal.png")))
        else:
            self.setSplitOrientation(QSplitter.Vertical)
            self.splitViewAct.setIconSet(\
                QIconSet(utilIcons.getPixmap("splitVertical.png")))
            self.splitRemoveAct.setIconSet(\
                QIconSet(utilIcons.getPixmap("remsplitVertical.png")))
    
    ##################################################################
    ## Below are the action methods for the macro menu
    ##################################################################
    
    def handleMacroStartRecording(self):
        """
        Private method to handle the start macro recording action.
        """
        self.activeWindow().handleStartMacroRecording()
        
    def handleMacroStopRecording(self):
        """
        Private method to handle the stop macro recording action.
        """
        self.activeWindow().handleStopMacroRecording()
        
    def handleMacroRun(self):
        """
        Private method to handle the run macro action.
        """
        self.activeWindow().handleRunMacro()
        
    def handleMacroDelete(self):
        """
        Private method to handle the delete macro action.
        """
        self.activeWindow().handleDeleteMacro()
        
    def handleMacroLoad(self):
        """
        Private method to handle the load macro action.
        """
        self.activeWindow().handleLoadMacro()
        
    def handleMacroSave(self):
        """
        Private method to handle the save macro action.
        """
        self.activeWindow().handleSaveMacro()
    
    ##################################################################
    ## Below are the action methods for the bookmarks menu
    ##################################################################
    
    def handleToggleBookmark(self):
        """
        Private method to handle the toggle bookmark action.
        """
        self.activeWindow().handleToggleBookmark()
        
    def handleNextBookmark(self):
        """
        Private method to handle the next bookmark action.
        """
        self.activeWindow().handleNextBookmark()
    
    def handlePreviousBookmark(self):
        """
        Private method to handle the previous bookmark action.
        """
        self.activeWindow().handlePreviousBookmark()
    
    def handleClearAllBookmarks(self):
        """
        Private method to handle the clear all bookmarks action.
        """
        for editor in self.editors:
            editor.handleClearBookmarks()
            
        self.bookmarkNextAct.setEnabled(0)
        self.bookmarkPreviousAct.setEnabled(0)
        self.bookmarkClearAct.setEnabled(0)
    
    def handleShowBookmarksMenu(self):
        """
        Private method to handle the show bookmarks menu signal.
        """
        self.bookmarks = {}
        self.bookmarksMenu.clear()
        
        filenames = self.getOpenFilenames()
        filenames.sort()
        for filename in filenames:
            editor = self.getOpenEditor(filename)
            for bookmark in editor.getBookmarks():
                if len(filename) > 50:
                    dots = "..."
                else:
                    dots = ""
                id = self.bookmarksMenu.insertItem(\
                        "%s%s : %d" % (dots, filename[-50:], bookmark))
                self.bookmarks[id] = (filename, bookmark)
    
    def handleBookmarkSelected(self, id):
        """
        Private method to handle the bookmark selected signal.
        
        @param id index of the selected menu entry
                This acts as an index into the list of bookmarks
                that was created, when the bookmarks menu was built.
        """
        self.displayPythonFile(self.bookmarks[id][0], self.bookmarks[id][1])
        
    def handleBookmarkToggled(self, editor):
        """
        Private slot to handle the bookmarkToggled signal.
        
        It checks some bookmark actions and reemits the signal.
        
        @param editor editor that sent the signal
        """
        if editor.hasBookmarks():
            self.bookmarkNextAct.setEnabled(1)
            self.bookmarkPreviousAct.setEnabled(1)
            self.bookmarkClearAct.setEnabled(1)
        else:
            self.bookmarkNextAct.setEnabled(0)
            self.bookmarkPreviousAct.setEnabled(0)
            self.bookmarkClearAct.setEnabled(0)
        self.emit(PYSIGNAL('bookmarkToggled'), (editor,))
    
    def handleGotoSyntaxError(self):
        """
        Private method to handle the goto syntax error action.
        """
        self.activeWindow().handleGotoSyntaxError()
    
    def handleClearAllSyntaxErrors(self):
        """
        Private method to handle the clear all syntax errors action.
        """
        for editor in self.editors:
            editor.handleClearSyntaxError()
    
    def handleSyntaxErrorToggled(self, editor):
        """
        Private slot to handle the syntaxerrorToggled signal.
        
        It checks some syntax error actions and reemits the signal.
        
        @param editor editor that sent the signal
        """
        if editor.hasSyntaxErrors():
            self.syntaxErrorGotoAct.setEnabled(1)
            self.syntaxErrorClearAct.setEnabled(1)
        else:
            self.syntaxErrorGotoAct.setEnabled(0)
            self.syntaxErrorClearAct.setEnabled(0)
        self.emit(PYSIGNAL('syntaxerrorToggled'), (editor,))
    
    ##################################################################
    ## Below are general utility methods
    ##################################################################
    
    def handleResetUI(self):
        """
        Public slot to handle the resetUI signal.
        """
        editor = self.activeWindow()
        if editor is None:
            self.setSbFile()
        else:
            line, pos = editor.getCursorPosition()
            self.setSbFile(editor.getFileName(), line+1, pos)
        
    def closeViewManager(self):
        """
        Public method to shutdown the viewmanager. 
        
        If it cannot close all editor windows, it aborts the shutdown process.
        
        @return flag indicating success (boolean)
        """
        self.handleCloseAll()
        if len(self.editors):
            return 0
        else:
            return 1

    def handleLastEditorClosed(self):
        """
        Private slot to handle the lastEditorClosed signal.
        """
        self.SauveRecents() 
        
        
    def handleEditorOpened(self):
        """
        Private slot to handle the editorOpened signal.
        """
        self.closeActGrp.setEnabled(1)
        self.saveActGrp.setEnabled(1)
        self.printAct.setEnabled(1)
        self.printSelAct.setEnabled(1)
        self.editActGrp.setEnabled(1)
        self.searchActGrp.setEnabled(1)
        self.viewActGrp.setEnabled(1)
        self.viewFoldActGrp.setEnabled(1)
        self.unhighlightAct.setEnabled(1)
        self.splitViewAct.setEnabled(1)
        self.splitOrientationAct.setEnabled(1)
        self.macroActGrp.setEnabled(1)
        self.bookmarkActGrp.setEnabled(1)
        
        # activate the autosave timer
        if not self.autosaveTimer.isActive() and \
           self.autosaveInterval > 0:
            self.autosaveTimer.start(self.autosaveInterval * 60000, 1)
        
        
    def checkActions(self, editor, setSb=1):
        """
        Private slot to check some actions for their enable/disable status and set the statusbar info.
        
        @param editor editor window
        @param setSb flag indicating an update of the status bar is wanted (boolean)
        """
        if editor is not None:
            self.saveAct.setEnabled(editor.modified)
            self.revertAct.setEnabled(editor.modified)
            
            lex = editor.getLexer()
            if lex is not None:
                self.commentAct.setEnabled(lex.canBlockComment())
                self.uncommentAct.setEnabled(lex.canBlockComment())
                self.streamCommentAct.setEnabled(lex.canStreamComment())
                self.boxCommentAct.setEnabled(lex.canBoxComment())
            else:
                self.commentAct.setEnabled(0)
                self.uncommentAct.setEnabled(0)
                self.streamCommentAct.setEnabled(0)
                self.boxCommentAct.setEnabled(0)
            
            if editor.hasBookmarks():
                self.bookmarkNextAct.setEnabled(1)
                self.bookmarkPreviousAct.setEnabled(1)
                self.bookmarkClearAct.setEnabled(1)
            else:
                self.bookmarkNextAct.setEnabled(0)
                self.bookmarkPreviousAct.setEnabled(0)
                self.bookmarkClearAct.setEnabled(0)
            
            if editor.hasSyntaxErrors():
                self.syntaxErrorGotoAct.setEnabled(1)
                self.syntaxErrorClearAct.setEnabled(1)
            else:
                self.syntaxErrorGotoAct.setEnabled(0)
                self.syntaxErrorClearAct.setEnabled(0)
            
            if editor.canAutoCompleteFromAPIs():
                self.autoCompleteFromAPIsAct.setEnabled(1)
            else:
                self.autoCompleteFromAPIsAct.setEnabled(0)
                
            if setSb:
                line, pos = editor.getCursorPosition()
                self.setSbFile(editor.getFileName(), line+1, pos)
                
            self.emit(PYSIGNAL('checkActions'), (editor,))
        
    def handlePreferencesChanged(self):
        """
        Public slot to handle the preferencesChanged signal.
        
        This method performs the following actions
            <ul>
            <li>reread the colours for the syntax highlighting</li>
            <li>reloads the already created API objetcs</li>
            <li>starts or stops the autosave timer</li>
            <li><b>Note</b>: changes in viewmanager type are activated
              on an application restart.</li>
            </ul>
        """
        # reload api information
        for language, api in self.apis.items():
            if api is not None:
                apifiles = Preferences.getEditorAPI(language)
                if len(apifiles):
                    api.clear()
                    for apifile in apifiles:
                        api.load(apifile)
                else:
                    self.apis[language] = None
                    
        # reload editor settings
        for editor in self.editors:
            editor.readSettings()
            
        # reload the autosave timer setting
        self.autosaveInterval = Preferences.getEditor("AutosaveInterval")
        if len(self.editors):
            if self.autosaveTimer.isActive() and \
               self.autosaveInterval == 0:
                self.autosaveTimer.stop()
            elif not self.autosaveTimer.isActive() and \
               self.autosaveInterval > 0:
                self.autosaveTimer.start(self.autosaveInterval * 60000, 1)
        
    def handleEditorSaved(self, fn):
        """
        Public slot to handle the editorSaved signal.
        
        It simply reemits the signal.
        
        @param fn filename of the saved editor
        """
        self.emit(PYSIGNAL('editorSaved'), (fn,))
        
    def handleCursorChanged(self, fn, line, pos):
        """
        Private slot to handle the cursorChanged signal. 
        
        It emits the signal cursorChanged with parameter editor.
        
        @param fn filename (string)
        @param line line number of the cursor (int)
        @param pos position in line of the cursor (int)
        """
        self.setSbFile(fn, line, pos)
        self.emit(PYSIGNAL('cursorChanged'), (self.getOpenEditor(fn),))
        
    def handleBreakpointToggled(self, editor):
        """
        Private slot to handle the breakpointToggled signal.
        
        It simply reemits the signal.
        
        @param editor editor that sent the signal
        """
        self.emit(PYSIGNAL('breakpointToggled'), (editor,))
        
            
    def getProject(self):
        """
        Public method to get a reference to the Project object.
        
        @return Reference to the Project object (Project.Project)
        """
        return self.ui.getProject()
        
    def getActions(self, type):
        """
        Public method to get a list of all actions.
        
        @param type string denoting the action set to get.
                It must be one of "edit", "file", "search",
                "view" or "window"
        @return list of all actions (list of QAction)
        """
        try:
            exec 'actionList = self.%sActions[:]' % type
        except:
            actionList = []
                
        return actionList
        
    def editorCommand(self, cmd):
        """
        Private method to send an editor command to the active window.
        
        @param cmd the scintilla command to be sent
        """
        aw = self.activeWindow()
        if aw:
            aw.SendScintilla(cmd)
        
    ##################################################################
    ## Below are protected utility methods
    ##################################################################
    
    def _getOpenStartDir(self):
        """
        Protected method to return the starting directory for a file open dialog. 
        
        The appropriate starting directory is calculated
        using the following search order, until a match is found:<br />
            1: Directory of currently active editor<br />
            2: Directory of currently active Project<br />
            3: CWD

        @return String name of directory to start or None
        """
        # if we have an active source, return its path
        if self.activeWindow() is not None and \
           self.activeWindow().getFileName():
            return os.path.dirname(self.activeWindow().getFileName())
            
        # ok, try if there is an active project and return its path
        elif self.getProject().isOpen():
            return self.getProject().ppath
            
        else:
            try :
               userDir=os.path.expanduser("~/Eficas_install/")
               return userDir
            except :
               return ""        


    def _getOpenFileFilter(self):
        """
        Protected method to return the active filename filter for a file open dialog.
        
        The appropriate filename filter is determined by file extension of
        the currently active editor.
        
        @return name of the filename filter (QString) or None
        """
        if self.activeWindow() is not None and \
           self.activeWindow().getFileName():
            ext = os.path.splitext(self.activeWindow().getFileName())[1]
            try:
                return QString(self.ext2Filter[ext])
            except KeyError:
                return None
                
        else:
            return None

            


"""
Module implementing a tabbed viewmanager class.
"""



class TabWidget(QTabWidget):
    """
    Class implementing a custimized TabWidget.
    """
    def __init__(self, parent):
        """
        Constructor
        
        @param parent parent widget (QWidget)
        """
        QTabWidget.__init__(self, parent)
        
        self.editors = []
        self.curIndex = 0
        
        self.connect(self, SIGNAL("currentChanged(QWidget *)"), self.handleCurrentChanged)
        
    def handleCurrentChanged(self):
        """
        Private slot called by the currentChanged signal.
        """
        self.curIndex = self.currentPageIndex()
        
    def addTab(self, editor, title):
        """
        Overwritten method to add a new tab.
        
        @param editor the editor object to be added (QScintilla.Editor.Editor)
        @param title title for the new tab (string, QString or QTab)
        """
        QTabWidget.addTab(self, editor, title)
        
        if not editor in self.editors:
            self.editors.append(editor)
            self.connect(editor, PYSIGNAL('captionChanged'),
                self.handleCaptionChange)
                
    def showPage(self, editor):
        """
        Overridden method to show a tab.
        
        @param editor the editor object to be shown (QScintilla.Editor.Editor)
        """
        QTabWidget.showPage(self, editor)
        self.curIndex = self.indexOf(editor)
        
    def nextTab(self):
        """
        Public slot used to show the next tab.
        """
        if self.count():
            self.curIndex += 1
            if self.curIndex == self.count():
                self.curIndex = 0
                
            QTabWidget.showPage(self, self.page(self.curIndex))

    def prevTab(self):
        """
        Public slot used to show the previous tab.
        """
        if self.count():
            self.curIndex -= 1
            if self.curIndex == -1:
                self.curIndex = self.count() - 1
                
            QTabWidget.showPage(self, self.page(self.curIndex))

    def handleCaptionChange(self, cap, editor):
        """
        Private method to handle Caption change signals from the editor. 
        
        Updates the listview text to reflect the new caption information.
        
        @param cap Caption for the editor
        @param editor Editor to update the caption for
        """
        fn = editor.getFileName()
        if fn:
            txt = os.path.basename(fn)
            if editor.isReadOnly():
                txt = '%s (ro)' % txt
            self.changeTab(editor, txt)
        
    def removePage(self, object):
        """
        Overwritten method to remove a page.
        
        @param object object to be removed (QObject)
        """
        QTabWidget.removePage(self, object)
        
        self.disconnect( object, PYSIGNAL('captionChanged'),
                         self.handleCaptionChange )
        self.editors.remove(object)
        
    def hasEditor(self, editor):
        """
        Public method to check for an editor.
        
        @param editor editor object to check for
        @return flag indicating, whether the editor to be checked belongs
            to the list of editors managed by this tab widget.
        """
        return editor in self.editors
        
    def hasEditors(self):
        """
        Public method to test, if any editor is managed.
        
        @return flag indicating editors are managed
        """
        return len(self.editors) and 1 or 0
        
class Tabview(QSplitter, ViewManager):
    """
    Class implementing a tabbed viewmanager class embedded in a splitter.
    
    @signal lastEditorClosed emitted after the last editor window was closed
    @signal editorOpened emitted after an editor window was opened
    @signal editorSaved emitted after an editor window was saved
    """
    def __init__(self,parent, ui):
        """
        Constructor
        
        @param parent parent widget (QWidget)
        @param ui reference to the main user interface
        @param dbs reference to the debug server object
        """
        self.tabWidgets = []
        
        QSplitter.__init__(self,parent)
        ViewManager.__init__(self, ui)
        tw = TabWidget(self)
        self.tabWidgets.append(tw)
        self.currentTabWidget = tw
        self.connect(tw, SIGNAL('currentChanged(QWidget*)'),
            self.handleCurrentChanged)
        tw.installEventFilter(self)
        tw.tabBar().installEventFilter(self)
        self.setOrientation(QSplitter.Vertical)
        
    def initViewActions(self):
        """
        Protected method defining the user interface actions for the view commands.
        """
        ViewManager.initViewActions(self)
        
        self.nextTabAct = QAction(self.trUtf8('Show next tab'), 
                      self.trUtf8('Show next tab'), 
                      QKeySequence(self.trUtf8('Ctrl+Alt+Tab')), self)
        self.connect(self.nextTabAct, SIGNAL('activated()'), self.nextTab)
        self.viewActions.append(self.nextTabAct)
        
        self.prevTabAct = QAction(self.trUtf8('Show previous tab'), 
                      self.trUtf8('Show previous tab'), 
                      QKeySequence(self.trUtf8('Shift+Ctrl+Alt+Tab')), self)
        self.connect(self.prevTabAct, SIGNAL('activated()'), self.prevTab)
        self.viewActions.append(self.prevTabAct)
        
    def nextTab(self):
        """
        Private slot used to show the next tab of the current tabwidget.
        """
        self.currentTabWidget.nextTab()
        
    def prevTab(self):
        """
        Private slot used to show the previous tab of the current tabwidget.
        """
        self.currentTabWidget.prevTab()
        
    def canCascade(self):
        """
        Public method to signal if cascading of managed windows is available.
        
        @return flag indicating cascading of windows is available
        """
        return 0
        
    def canTile(self):
        """
        Public method to signal if tiling of managed windows is available.
        
        @return flag indicating tiling of windows is available
        """
        return 0
        
    def canSplit(self):
        """
        public method to signal if splitting of the view is available.
        
        @return flag indicating splitting of the view is available.
        """
        return 1
        
    def tile(self):
        """
        Public method to tile the managed windows.
        """
        pass
        
    def cascade(self):
        """
        Public method to cascade the managed windows.
        """
        pass
        
    def removeAllViews(self):
        """
        Private method to remove all views (i.e. windows)
        """
        for win in self.editors:
            self.removeView(win)
            
    def removeView(self, win):
        """
        Private method to remove a view (i.e. window)
        
        @param win editor window to be removed
        """
        for tw in self.tabWidgets:
            if tw.hasEditor(win):
                tw.removePage(win)
                break        
        win.closeIt()        
        
        # if this was the last editor in this view, switch to the next, that
        # still has open editors
        for i in range(self.tabWidgets.index(tw), -1, -1) + \
                 range(self.tabWidgets.index(tw) + 1, len(self.tabWidgets)):
            if self.tabWidgets[i].hasEditors():
                self.currentTabWidget = self.tabWidgets[i]
                self.activeWindow().setFocus()
                break
    
    def addView(self, win, fn=None, title=None):
        """
        Private method to add a view (i.e. window)
        
        @param win editor window to be added
        @param fn filename of this editor
        """
        win.show()
        if fn is None:
            if title== None : 
               self.untitledCount += 1
               self.currentTabWidget.addTab(win, self.trUtf8("Untitled %1").arg(self.untitledCount))
            else :
               self.currentTabWidget.addTab(win, title)
        else:
            txt = os.path.basename(fn)
            if not QFileInfo(fn).isWritable():
                txt = '%s (ro)' % txt
            self.currentTabWidget.addTab(win, txt)
            self.currentTabWidget.setTabToolTip(win, os.path.dirname(fn))
        self.currentTabWidget.showPage(win)
        win.setFocus()
    
    def showView(self, win, fn=None):
        """
        Private method to show a view (i.e. window)
        
        @param win editor window to be shown
        @param fn filename of this editor
        """
        win.show()
        for tw in self.tabWidgets:
            if tw.hasEditor(win):
                tw.showPage(win)
                self.currentTabWidget = tw
                break
        win.setFocus()
    
    def activeWindow(self):
        """
        Private method to return the active (i.e. current) window.
        
        @return reference to the active editor
        """
        return self.currentTabWidget.currentPage()
        
    def handleShowWindowMenu(self, windowMenu):
        """
        Private method to set up the viewmanager part of the Window menu.
        
        @param windowMenu reference to the window menu
        """
        pass
        
    def initWindowActions(self):
        """
        Define the user interface actions for window handling.
        """
        pass
        
    def setEditorName(self, editor, newName):
        """
        Change the displayed name of the editor.
        
        @param editor editor window to be changed
        @param newName new name to be shown (string or QString)
        """
        self.currentTabWidget.changeTab(editor, 
            os.path.basename(unicode(newName)))
        self.currentTabWidget.setTabToolTip(editor, 
            os.path.dirname(unicode(newName)))
    
    def handleModificationStatusChanged(self, m, editor):
        """
        Private slot to handle the modificationStatusChanged signal.
        
        @param m flag indicating the modification status (boolean)
        @param editor editor window changed
        """
        for tw in self.tabWidgets:
            if tw.hasEditor(editor):
                break
        if m:
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("fileModified.png")))
        elif editor.hasSyntaxErrors():
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("syntaxError.png")))
        else:
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("empty.png")))
        self.checkActions(editor)
        
    def handleSyntaxErrorToggled(self, editor):
        """
        Private slot to handle the syntaxerrorToggled signal.
        
        @param editor editor that sent the signal
        """
        for tw in self.tabWidgets:
            if tw.hasEditor(editor):
                break
        if editor.hasSyntaxErrors():
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("syntaxError.png")))
        else:
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("empty.png")))
                
        ViewManager.handleSyntaxErrorToggled(self, editor)
        
    def addSplit(self):
        """
        Public method used to split the current view.
        """
        tw = TabWidget(self)
        tw.show()
        self.tabWidgets.append(tw)
        self.currentTabWidget = self.tabWidgets[-1]
        self.connect(tw, SIGNAL('currentChanged(QWidget*)'),
            self.handleCurrentChanged)
        tw.installEventFilter(self)
        tw.tabBar().installEventFilter(self)
        self.setSizes([int(100/len(self.tabWidgets))] * len(self.tabWidgets))
        self.splitRemoveAct.setEnabled(1)
        
    def removeSplit(self):
        """
        Public method used to remove the current split view.
        
        @return flag indicating successfull removal
        """
        if len(self.tabWidgets) > 1:
            tw = self.currentTabWidget
            res = 1
            savedEditors = tw.editors[:]
            for editor in savedEditors:
                res &= self.closeEditor(editor)
            if res:
                i = self.tabWidgets.index(tw)
                if i == len(self.tabWidgets)-1:
                    i -= 1
                self.tabWidgets.remove(tw)
                tw.close(1)
                self.currentTabWidget = self.tabWidgets[i]
                if len(self.tabWidgets) == 1:
                    self.splitRemoveAct.setEnabled(0)
                return 1
                
        return 0
        
    def setSplitOrientation(self, orientation):
        """
        Public method used to set the orientation of the split view.
        
        @param orientation orientation of the split
                (QSplitter.Horizontal or QSplitter.Vertical)
        """
        self.setOrientation(orientation)
        
    def handleCurrentChanged(self, editor):
        """
        Private slot to handle the currentChanged signal.
        
        @param editor selected editor window
        """
        self.checkActions(editor)
        editor.setFocus()
        
    def eventFilter(self, watched, event):
        """
        Method called to filter the event queue.
        
        @param watched the QObject being watched
        @param event the event that occurred
        @return always 0
        """
        if event.type() == QEvent.MouseButtonPress and \
           not event.button() == Qt.RightButton:
            if isinstance(watched, QTabWidget):
                self.currentTabWidget = watched
            elif isinstance(watched, QTabBar):
                self.currentTabWidget = watched.parent()
            elif isinstance(watched, QScintilla.Editor.Editor):
                for tw in self.tabWidgets:
                    if tw.hasEditor(watched):
                        self.currentTabWidget = tw
                        break
                        
            aw = self.activeWindow()
            if aw is not None:
                self.checkActions(aw)
                aw.setFocus()
            
        return 0


class MyTabview(Tabview):
    """
    Base class inherited by all specific viewmanager classes.
    
    It defines the interface to be implemented by specific
    viewmanager classes and all common methods.
    
    @signal lastEditorClosed emitted after the last editor window was closed
    @signal editorOpened(string) emitted after an editor window was opened
    @signal editorSaved(string) emitted after an editor window was saved
    @signal checkActions(editor) emitted when some actions should be checked
            for their status
    @signal cursorChanged(editor) emitted after the cursor position of the active
            window has changed
    @signal breakpointToggled(editor) emitted when a breakpoint is toggled.
    @signal bookmarkToggled(editor) emitted when a bookmark is toggled.
    """
    def __init__(self, parent, ui):
        Tabview.__init__(self, parent, ui)
        self.appli=parent
        self.code =self.appli.code
        self.salome=self.appli.salome
        self.initRecent()

    def initRecent(self) :
       rep=self.appli.CONFIGURATION.rep_user
       monFichier=rep+"/listefichiers_"+self.code
       index=0
       try :
           f=open(monFichier)
           while ( index < 9) :
              ligne=f.readline()
              if ligne != "" :
                 l=(ligne.split("\n"))[0]
                 self.recent.append(l)
              index=index+1
       except : pass

       try    : f.close()
       except : pass
        
    def SauveRecents(self) :
       rep=self.appli.CONFIGURATION.rep_user
       monFichier=rep+"/listefichiers_"+self.code
       try :
            f=open(monFichier,'w')
            if len(self.recent) == 0 : return
            index=0
            while ( index <  len(self.recent)):
              ligne=str(self.recent[index])+"\n"
              f.write(ligne)
              index=index+1
       except :
            pass
       try :
            f.close()
       except :
            pass


    def checkActions(self, editor, setSb=1):
        """
        Private slot to check some actions for their enable/disable status and set the statusbar info.
        
        @param editor editor window
        @param setSb flag indicating an update of the status bar is wanted (boolean)
        """        
        self.emit(PYSIGNAL('checkActions'), (editor,)) 
 

    def addToRecentList(self, fn):
        """
        Public slot to add a filename to the list of recently opened files.
        
        @param fn name of the file to be added
        """
        self.recent.remove(fn)
        self.recent.prepend(fn)
        if len(self.recent) > 9:
            self.recent = self.recent[:9] 
        
    def handleOpen(self,fn=None,patron=0,units=None):
        """
        Public slot to open a Python JDC file.
        
        @param prog name of file to be opened (string or QString)
               patron booleen pour indiquer si le fichier doit etre
                      ajoute a la liste des fichiers ouverts recemment
        """
        # Get the file name if one wasn't specified.
        if fn is None:

            fn = QFileDialog.getOpenFileName(self._getOpenStartDir(),
                        self.trUtf8('JDC Files (*.comm);;''All Files (*)'), self.ui)

            if fn.isNull():
                return

        fn = normabspath(unicode(fn))

        newWin, editor = self.getEditor(fn,units=units)
        
        if newWin:
            self.handleModificationStatusChanged(editor.modified, editor)
        self.checkActions(editor)
        
        # insert filename into list of recently opened files
        if patron == 0 : self.addToRecentList(fn)
    

   ##################################################################
   ## Below are protected utility methods
   #################################################################
    
    def _getOpenStartDir(self):
        """
        Protected method to return the starting directory for a file open dialog. 
        
        The appropriate starting directory is calculated
        using the following search order, until a match is found:<br />
            1: Directory of currently active editor<br />
            2: Directory of currently active Project<br />
            3: CWD

        @return String name of directory to start or None
        """
        # if we have an active source, return its path
        if self.activeWindow() is not None and \
           self.activeWindow().getFileName():
            return os.path.dirname(self.activeWindow().getFileName())
            
            
        else:
            # None will cause open dialog to start with cwd
            try :
               userDir=os.path.expanduser("~/Eficas_install/")
               return userDir
            except :
               return ""        


    def handleEditorOpened(self):
        """
        Private slot to handle the editorOpened signal.
        """
        pass
        
    def handleModificationStatusChanged(self, m, editor):
        """
        Private slot to handle the modificationStatusChanged signal.
        
        @param m flag indicating the modification status (boolean)
        @param editor editor window changed
        """
        for tw in self.tabWidgets:
            if tw.hasEditor(editor):
                break
        if m:
            #tw.setTabIconSet(editor, 
            #    QIconSet(utilIcons.getPixmap("fileModified.png")))
            pass
        elif editor.hasSyntaxErrors():
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("syntaxError.png")))
        else:
            tw.setTabIconSet(editor, 
                QIconSet(utilIcons.getPixmap("empty.png")))
        self.checkActions(editor)        
        
        


if __name__=='__main__':
    import sys
    import prefs 
    if hasattr(prefs,'encoding'):
       # Hack pour changer le codage par defaut des strings
       import sys
       reload(sys)
       sys.setdefaultencoding(prefs.encoding)
       del sys.setdefaultencoding
       # Fin hack

    #CS_pbruno note: fait implicitement des trucs ces imports (grr)
    #import styles
    from Editeur import import_code
    from Editeur import session

    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code    
    app = QApplication(sys.argv)
    
    mw = MyTabview(None,None)
    app.setMainWidget(mw)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    mw.show()
    mw.getEditor('azAster.comm')
    mw.getEditor('azAster2.comm')
    res = app.exec_loop()
    sys.exit(res)
