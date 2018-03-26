from atmo import *

myatmo=CreateFromDocument(open('./ex_jdc.xml').read())
myatmo.toxml()

print myatmo.toDOM().toprettyxml()
print myatmo.Wind.Wind_Speed

myWind=myatmo.Wind
myWind.Wind_Speed=50
myatmo.Wind=myWind
print myatmo.toDOM().toprettyxml()

file=open('./ex_jdc_bis.xml','w');file.write(myatmo.toxml());file.close()
myatmobis=CreateFromDocument(open('./ex_jdc_bis.xml').read())
print myatmobis.toDOM().toprettyxml()
