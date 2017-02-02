#!/usr/bin/env python
import sys, re
dicoCataToLabel={}
dicoCataToTelemac={}
Entete  = '<?xml version="1.0" encoding="utf-8"?>'
Entete +='<!DOCTYPE TS><TS version="1.1" language="en">'
Entete +='<context>\n'
Entete +='    <name>@defaut</name>\n'

Fin ='</context>\n</TS>\n'

pattern_In=re.compile(r'^\s*<source>(?P<ident>.*)</source>\s*$')
pattern_Out=re.compile(r'^\s*<translation>(?P<traduit>.*)</translation>\s*$')

listeMaj=[]
listeMaj.append(('for h','for H'))
listeMaj.append(('pour h','pour H'))
listeMaj.append(('for u','for U'))
listeMaj.append(('pour u','pour U'))
listeMaj.append(('of k','of K'))
listeMaj.append(('de k','de K'))
listeMaj.append(('of h','of H'))
listeMaj.append(('de h','de H'))
listeMaj.append(('u and v','U and V'))
listeMaj.append(('u et v','U et V'))
listeMaj.append(('on h','on H'))
listeMaj.append(('sur h','sur H'))
listeMaj.append(('supg','SUPG'))
listeMaj.append(('k and epsilon','K and Epsilon'))
listeMaj.append(('k-epsilon','K-Epsilon'))
listeMaj.append(('gmres','GMRES'))
listeMaj.append(('cgstab','CGSTAB'))
listeMaj.append(('q(z)','Q(Z)'))
listeMaj.append(('z(q)','Z(Q)'))
listeMaj.append(('wgs84','WGS84'))
listeMaj.append(('wgs84','UTM'))
listeMaj.append(('n-scheme','N-Scheme'))
listeMaj.append(('scheme n','Scheme N'))
listeMaj.append(('psi-scheme','PSI-Scheme'))
listeMaj.append((' psi',' PSI'))
listeMaj.append(('f(t90)','F(T90)'))
listeMaj.append(('(pa)','(Pa)'))
listeMaj.append(('h clipping','H clipping'))
listeMaj.append(('delwaq','DELWAQ'))
listeMaj.append(('tomawac','TOMAWAC'))
listeMaj.append(('chezy','CHEZY'))
listeMaj.append(('hllc','HLLC'))
listeMaj.append(('c-u','C-U'))
listeMaj.append(('c,u,v','C,U,V'))
listeMaj.append(('h,u,v','H,U,V'))
listeMaj.append(('previmer','PREVIMER'))
listeMaj.append(('fes20xx','FES20XX'))
listeMaj.append(('legos-nea','LEGOS-NEA'))
listeMaj.append(('tpxo','TPXO'))
listeMaj.append((' x',' X'))
listeMaj.append((' y',' Y'))
listeMaj.append(('waf','WAF'))
listeMaj.append(('(w/kg)','(W/kg)'))
listeMaj.append(('(j/kg)','(W/kg)'))
listeMaj.append(('zokagoa','Zokagoa'))
listeMaj.append(('nikuradse','Nikuradse'))
listeMaj.append(('froude','Froude'))
listeMaj.append(('gauss','Gauss'))
listeMaj.append(('seidel','Seidel'))
listeMaj.append(('leo','Leo'))
listeMaj.append(('postma','Postma'))
listeMaj.append(('crout','Crout'))
listeMaj.append(('okada','Okada'))
listeMaj.append(('jmj','JMJ'))
listeMaj.append(('haaland','HAALAND'))
listeMaj.append(('grad(u)','grad(U)'))
listeMaj.append(('variable z','variable Z'))
listeMaj.append(('variable r','variable R'))
listeMaj.append(('ascii','ASCII'))


def traite(fichier,fichierDico, fichierTs):
  f=open(fichier,'r')
  t=f.read()
  for ligne in t.split('\n'):
     if pattern_In.match(ligne): 
        m=pattern_In.match(ligne)
        ident=m.group('ident')
     if pattern_Out.match(ligne): 
        m=pattern_Out.match(ligne)
        traduit=m.group('traduit')
        dicoCataToTelemac[ident]=traduit
        traduitMin=traduit.lower()
        for t in listeMaj :
           traduit=traduitMin.replace(t[0],t[1])
           traduitMin=traduit
        chaine=traduitMin[0].upper()+traduitMin[1:]
        dicoCataToLabel[ident]=chaine
  f.close()

  f=open(fichierDico,'w')
  f.write ("dicoCataToEngTelemac = {\n")
  for k in dicoCataToTelemac.keys() :
       l= '   "'+  k +'" : "'+ dicoCataToTelemac[k]+'",\n'
       f.write(l)
  f.write(" }\n")
  f.write( "dicoCasEnToCata = {\n")
  for k in dicoCataToTelemac.keys() :
      l= '   "'+ dicoCataToTelemac[k] +'" : "'+ k+'",\n'
      f.write(l)
  f.write( " }\n")
  f.close()

  f=open(fichierTs,'w')
  f.write( Entete)
  for k in dicoCataToTelemac.keys() :
      texte = "    <message>\n        <source>"
      texte+= k
      texte+= "</source>\n        <translation>"
      texte+= dicoCataToLabel[k]
      texte+= "</translation>\n    </message>\n"
      f.write( texte)

  f.write( Fin)

    
if __name__ == "__main__":
  import optparse
  parser=optparse.OptionParser(usage="utilisation : %prog [options]")
  parser.add_option(u"-i","--input",dest="fichierIn",type='string',
                    help=("nom du fichier ts a traduire"))
  parser.add_option(u"-d","--dico",dest="fichierDico",type='string',
                    help=("nom du fichier contenant les dictionnaires labelTelemac:labelCata en sortie"))
  parser.add_option(u"-t","--tsFile",dest="fichierTs",type='string',
                    help=("nom du fichier ts contenant labelCata vers label IHM"))


  (options,args)=parser.parse_args(sys.argv[1:])
  if options.fichierIn == None or options.fichierDico == None or options.fichierTs==None :
      print 'reEcrittsEn.py -i <inputfile> -d <dicofile> -t <tsfile>'
      print './reEcrittsEn.py -i cata_name2eng_name.ts -d dicoCasEnToCata.py -t labelCataToIhmEn.ts'
      sys.exit(1)
  traite(options.fichierIn,options.fichierDico,options.fichierTs)

