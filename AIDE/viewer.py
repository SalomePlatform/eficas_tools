# -*- coding: utf-8 -*-
import os
import Tkinter
import ScrolledText
import formatter
import htmllib

class TkWriter(formatter.DumbWriter):
   def __init__(self, text,viewer):
      formatter.DumbWriter.__init__(self, self)
      self.text=text
      self.viewer=viewer

   def write(self,data):
      self.text.insert("insert", data)

   def anchor_bgn(self, href, name, type):
      if href:
          self.anchor = (href, name, type)
          self.anchor_mark = self.text.index("insert")

   def anchor_end(self):
      if self.anchor:
          url = self.anchor[0]
          tag = "href_" + url
          self.text.tag_add(tag, self.anchor_mark, "insert")
          def displayurl(event,v=self.viewer,u=url):
             v.display(u)
          self.text.tag_bind(tag, "<ButtonPress>", displayurl)
          self.text.tag_config(tag, foreground="blue", underline=1)
          self.anchor = None

class HTMLParser(htmllib.HTMLParser):
    def anchor_bgn(self, href, name, type):
        htmllib.HTMLParser.anchor_bgn(self, href, name, type)
        # On signale directement au writer le debut d'une reference
        self.formatter.writer.anchor_bgn(href, name, type)

    def anchor_end(self):
        if self.anchor:
            self.formatter.writer.anchor_end()
            self.anchor = None

import string

class DumbParser:
    def __init__(self,fmt):
        self.formatter=fmt

    def feed(self,data):
        self.formatter.writer.write(data)

    def close(self):
        pass
        
class Historique:
   def __init__(self):
      self.liste=[]
      self.index=0

   def add(self,url):
      if self.index > 0:
          old=self.liste[self.index-1]
          if url == old :return
      del self.liste[self.index:]
      self.liste.append(url)
      self.index=self.index+1

   def getback(self):
      if self.index > 1:
          self.index=self.index-1
          return self.liste[self.index-1]
      else:
          return None

   def getforward(self):
      if self.index < len(self.liste):
          url=self.liste[self.index]
          self.index=self.index+1
          return url
      else:
          return None

class HTMLViewer:
   def __init__(self,parent):
      self.init_window(parent)
      self.url=None
      self.home=None
      self.historique=Historique()
      self.createWidgets()
      self.init()

   def init_window(self,parent):
      self.parent=parent
      self.fenetre=Tkinter.Toplevel()
      self.fenetre.title("AIDE EFICAS")
      if self.fenetre.winfo_screenwidth() < 800 or self.fenetre.winfo_screenheight() < 600:
         self.fenetre.wm_minsize(300, 150)
      else:
         self.fenetre.wm_minsize(400, 200)
      self.fenetre.protocol("WM_DELETE_WINDOW",self.destroy)

   def createWidgets(self):
      frame = self.frame = Tkinter.Frame(self.fenetre)
      frame.pack(side="bottom", fill="x")
      self.homeButton = Tkinter.Button(frame, text="Index",font="Helvetica 12 bold",
                                       command=self.goHome)
      self.homeButton.pack(side="left")
      self.b_retour = Tkinter.Button(frame, text="Back",font="Helvetica 12 bold",
                                       command=self.goBack)
      self.b_retour.pack(side="left")
      self.b_avance = Tkinter.Button(frame, text="Forward",font="Helvetica 12 bold",
                                          command=self.goForward)
      self.b_avance.pack(side="left")

      self.b_close = Tkinter.Button(frame, text="Close",font="Helvetica 12 bold",
                                        command=self.destroy)
      self.b_close.pack(side="right")
      self.config_boutons()

      self.text=ScrolledText.ScrolledText(self.fenetre,bg='white',relief='sunken',font="Helvetica 12 bold")
      self.text.pack(side="top", fill="both", expand=1)
      self.text.bind("<Key-Prior>", self.page_up)
      self.text.bind("<Key-Next>", self.page_down)
      self.text.bind("<Key-Up>", self.unit_up)
      self.text.bind("<Key-Down>", self.unit_down)
      self.text.bind("<1>", self.clicked)

   def clicked(self,event):
        self.text.focus_set()

   def page_up(self,event):
        event.widget.yview_scroll(-1, "page")
   def page_down(self,event):
        event.widget.yview_scroll(1, "page")
   def unit_up(self,event):
        event.widget.yview_scroll(-1, "unit")
   def unit_down(self,event):
        event.widget.yview_scroll(1, "unit")

   def config_boutons(self):
      """
      Activation du bouton précédent s'il y a lieu
      """
      if self.historique.index > 1 :
         self.b_retour.config(state='normal')
      else :
         self.b_retour.config(state='disabled')
      if self.historique.index < len(self.historique.liste) :
         self.b_avance.config(state='normal')
      else :
         self.b_avance.config(state='disabled')

   def openurl(self,url):
      url=os.path.normpath(url)
      if self.url and not os.path.isabs(url):
         rep1,fich1=os.path.split(self.url)
         rep2,fich2=os.path.split(url)
         if rep1 != rep2 :
            url=os.path.join(rep1,rep2,fich2)
         url=os.path.normpath(url)
      try:
         f=open(url,'r')
         data=f.read()
         f.close()
      except:
         data="Impossible de trouver: "+url
      self.url=url
      if self.home is None:
         self.home=self.url
      return data

   def display(self,url):
      data=self.openurl(url)
      ext=os.path.splitext(url)[1]
      self.text.config(state="normal")
      self.text.delete("1.0", "end")
      writer=TkWriter(self.text,self)
      fmt=formatter.AbstractFormatter(writer)
      if ext == ".html":
         parser=HTMLParser(fmt)
      else:
         parser=DumbParser(fmt)
      parser.feed(data)
      parser.close()
      self.text.config(state="disabled")
      self.historique.add(url)
      self.config_boutons()

   def init(self):
      self.fenetre.bind("<KeyPress-BackSpace>", self.goBack)
      
   def goHome(self,event=None):
      if self.home and self.home != self.url:
         self.display(self.home)

   def goBack(self,event=None):
      url=self.historique.getback()
      if url:self.display(url)
         
   def goForward(self,event=None):
      url=self.historique.getforward()
      if url:self.display(url)

   def destroy(self):
       try:
          self.fenetre.destroy()
       except:
          pass

if __name__ == "__main__":
    v=HTMLViewer(None)
    v.display("fichiers/index.html")
    v.fenetre.mainloop()
      
