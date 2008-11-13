from qt import *
import os


def traduction(directPath,editor,version):
    if version == "V7V8" : 
       from Traducteur import traduitV7V8 
       suffixe="v8.comm"
    if version == "V8V9" : 
       from Traducteur import traduitV8V9 
       suffixe="v9.comm"
    fn = QFileDialog.getOpenFileName( QString(directPath) , "")

    FichieraTraduire=str(fn)
    if (FichieraTraduire == "" or FichieraTraduire == () ) : return
    i=FichieraTraduire.rfind(".")
    Feuille=FichieraTraduire[0:i]
    FichierTraduit=Feuille+suffixe

    i=Feuille.rfind("/")
    directLog=Feuille[0:i]
    log=directLog+"/convert.log"
    os.system("rm -rf "+log)
    os.system("rm -rf "+FichierTraduit)

    qApp.setOverrideCursor(QCursor(Qt.WaitCursor))
    if version == "V7V8" : traduitV7V8.traduc(FichieraTraduire,FichierTraduit,log)
    if version == "V8V9" : traduitV8V9.traduc(FichieraTraduire,FichierTraduit,log)
    qApp.setOverrideCursor(QCursor(Qt.ArrowCursor))

    Entete="Fichier Traduit : "+FichierTraduit +"\n\n"
    if  os.stat(log)[6] != 0L :
        f=open(log)
        texte= f.read()
        f.close()
    else :
       texte = Entete  
       commande="diff "+FichieraTraduire+" "+FichierTraduit+" >/dev/null"
       try :
         if os.system(commande) == 0 :
            texte = texte + "Pas de difference entre le fichier origine et le fichier traduit"
       except :
         pass

    from desVisu import DVisu
    titre = "conversion de "+ FichieraTraduire
    monVisu=DVisu(parent=editor,fl=Qt.WType_Dialog)
    monVisu.setCaption(titre)
    monVisu.TB.setText(texte)
    monVisu.show()

