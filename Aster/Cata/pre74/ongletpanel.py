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
from Tkinter import *

class OngletPanel :
  """ 
      Onglet Panel parametre et commentaire avec param_eval
  """ 
  def makeParamCommentPage_for_etape(self,page):
      """
      Crée la page qui offre le choix à l'utilisateur d'ajouter un commentaire
      ou un paramètre, avant ou après le noeud courant dans l'arbre.
      Cette page est destinée aux objets de niveau ETAPE cad à toutes les CMD,
      les commentaires inter commandes et les paramètres
      """
      # les frame ...
      self.frame_comment = Frame(page,bd=1,relief='raised')
      self.frame_param   = Frame(page,bd=1,relief='raised')
      self.frame_eval    = Frame(page,bd=1,relief='raised')
      self.frame_boutons = Frame(page,bd=1,relief='raised')
      self.frame_comment.place(relx=0,rely=0,relwidth=1,relheight=0.28)
      self.frame_param.place(relx=0,rely=0.28,relwidth=1,relheight=0.28)
      self.frame_eval.place(relx=0,rely=0.56,relwidth=1,relheight=0.28)
      self.frame_boutons.place(relx=0,rely=0.84,relwidth=1,relheight=0.16)
      # remplissage de la frame commentaire
      Label(self.frame_comment,text = "Insérer un commentaire :").place(relx=0.1,rely=0.5,anchor='w')
      but_comment_avant = Button(self.frame_comment,
                                 text = "AVANT "+self.node.item.get_nom(),
                                 command = lambda s=self :s.ajout_commentaire(ind = 'before'))
      but_comment_apres = Button(self.frame_comment,
                                 text = "APRES "+self.node.item.get_nom(),
                                 command = self.ajout_commentaire)
      but_comment_avant.place(relx=0.6,rely=0.3,anchor='w',relwidth=0.3)
      but_comment_apres.place(relx=0.6,rely=0.7,anchor='w',relwidth=0.3)
      # remplissage de la frame paramètre
      Label(self.frame_param,text = "Insérer un paramètre :").place(relx=0.1,rely=0.5,anchor='w')
      but_param_avant = Button(self.frame_param,
                                 text = "AVANT "+self.node.item.get_nom(),
                                 command = lambda s=self :s.ajout_parametre(ind = 'before'))
      but_param_apres = Button(self.frame_param,
                                 text = "APRES "+self.node.item.get_nom(),
                                 command = self.ajout_parametre)
      but_param_avant.place(relx=0.6,rely=0.3,anchor='w',relwidth=0.3)
      but_param_apres.place(relx=0.6,rely=0.7,anchor='w',relwidth=0.3)
      # remplissage de la frame eval
      Label(self.frame_eval,text="Insérer un paramètre EVAL :").place(relx=0.1,rely=0.5,anchor='w')
      but_eval_avant = Button(self.frame_eval,
                              text = "AVANT "+self.node.item.get_nom(),
                              command = lambda s=self :s.ajout_parametre_eval(ind = 'before'))
      but_eval_apres = Button(self.frame_eval,
                              text = "APRES "+self.node.item.get_nom(),
                              command = self.ajout_parametre_eval)
      but_eval_avant.place(relx=0.6,rely=0.3,anchor='w',relwidth=0.3)
      but_eval_apres.place(relx=0.6,rely=0.7,anchor='w',relwidth=0.3)      
      # remplissage de la frame boutons
      Button(self.frame_boutons,
             text="Commentariser toute la commande",
             command = self.comment_commande).place(relx=0.5,rely=0.5,anchor='center')
    
  def ajout_parametre_eval(self,ind='after'):
      """
      Ajoute un paramètre EVAL à l'intérieur du JDC :
      - si ind='after'  : l'ajoute après l'objet courant
      - si ind='before' : l'ajoute avant.
      """
      if self.parent.modified == 'n' : self.parent.init_modif()
      return self.node.append_brother("PARAMETRE_EVAL",ind)

  def destroy(self):
      self.frame_eval=None

