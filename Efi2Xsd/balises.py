typeSimple    = '\t<simpleType name="{}">\n\t\t<restriction base="{}"/>\n\t</simpleType>\n'
eltDsSequence = '\t\t\t<element name="{}" type="{}:{}" minOccurs="{}" maxOccurs="{}"/>\n'

debutTypeComplexe = '\t<complexType name="{}">\n\t\t<sequence>\n'
finTypeComplexe   = '\t\t</sequence>\n\t</complexType>\n'

debutTypeCata = '\t<complexType name="{}">\n\t\t<choice minOccurs="0" maxOccurs="unbounded">\n'
finTypeCata   = '\t\t</choice>\n\t</complexType> '

eltCata = '<element name="JDD" type="{}:{}"/>\n'


if __name__ == '__main__' :
   nomElt='Simple'
   nomDuType='T_Simple'
   nomDuTypeBase='int'
   nomDuComplexe='T_Complexe'
   nomDuCode='monCode'
   minOccurs=1
   maxOccurs=1

   texteSimple=typeSimple.format(nomDuType, nomDuTypeBase)
   texteElt=eltDsSequence.format(nomElt,nomDuCode,nomDuType,minOccurs,maxOccurs)

   minOccurs=0
   texteComplexe=debutTypeComplexe.format(nomDuComplexe)
   texteComplexe+=texteElt
   texteComplexe+=finTypeComplexe
   texteEltComplexe=eltDsSequence.format(nomElt,nomDuCode,nomDuType,minOccurs,maxOccurs)

   texteCata=debutTypeCata.format(nomDuCode)
   texteCata+=texteEltComplexe
   texteCata+=finTypeCata

   eltRacine=eltCata.format(nomDuCode, 'T_'+nomDuCode)
   print (texteSimple+texteComplexe+texteCata+eltRacine)

