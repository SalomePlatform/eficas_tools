import sys
sys.path[:0]=['../..','../../..']

# On récupère les plugins de la famille convert
import convert

p=convert.plugins['asterv5']()
p.readfile('totalmod.comm')
if not p.cr.estvide():
   print p.cr
   sys.exit(0)

s=p.convert('exec')
if not p.cr.estvide():
   print p.cr
   sys.exit(0)

print s
