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

# Installation de tous les fichiers Python, texte et images du repertoire et des sous-repertoires (sauf CVS)
install (
          FILES
                appli.py basestyle.py browser.py bureau.py catabrowser.py
                cataediteur.py centerwindow.py change_comm.py compobase.py
                compobloc.py compocommandecomm.py compocomm.py compoerror.py
                compofact.py compoformule.py compojdc.py compomacro.py 
                compomclist.py componiveau.py componuplet.py compooper.py 
                compoparameval.py compoparam.py compoproc.py composimp.py 
                definition_cata.py eficas_go.py eficas.py eficas_test.py 
                faq.py fenetre_mc_inconnus.py fonctionpanel.py fontes.py 
                images.py __init__.py Interp.py jdcdisplay.py 
                listeFichiers.py listePatronsTK.py macrodisplay.py menubar.py
                newsimppanel.py options.py panels.py panelsSalome.py 
                patches.py plusieursassdpanel.py plusieursbasepanel.py 
                plusieursintopanel.py plusieurspanel.py readercata.py 
                shellpanel.py splash.py statusbar.py styles.py
                toolbar.py tooltip.py treeitemincanvas.py treewidget.py 
                TroisDPal.py uniqueassdpanel.py uniquebasepanel.py 
                uniquecomppanel.py uniqueintopanel.py
                uniquepanel.py uniquesdcopanel.py widgets.py
          DESTINATION ${CMAKE_INSTALL_PREFIX}/InterfaceTK
	)

### Local Variables:
### mode: cmake
### End:
