import os
import sys

try :
   sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'),'classes/python/'))
   from class_MAP_parameters import *
except :
   pass


#-------------------------
class component_RBM:
#-------------------------

   def __init__(self,CS,CSJ,GS,GSJ,VMAX,VMAXJ,study_path):
      print "RBM - BEGIN"
      composant="RBM"
      RBM_input = study_path+"/RBM.input"
      parameter=MAP_parameters()
      parameter.add_component(composant)
      parameter.add_parameter(composant, 'CS', CS)
      parameter.add_parameter(composant, 'CSJ', CSJ)
      parameter.add_parameter(composant, 'GS', GS)
      parameter.add_parameter(composant, 'GSJ', GSJ)
      parameter.add_parameter(composant, 'VMAX', VMAX)
      parameter.add_parameter(composant, 'VMAXJ', VMAXJ)
      parameter.write(RBM_input)

      #commande= "cd "+ commponent_dir +";"
      #commande+= "python rbm.py -i "+RBM_input+";\n"
      #os.system(commande)

      print "RBM - END"


#-------------------------
class component_DISPL:
#-------------------------

   def __init__(self,CS,CSJ,GS,GSJ,VMAXJ,VMAX,study_path):
      print "DISPL - BEGIN"
      composant="DISPL"
      DISPL_input = study_path+"/DISPL.input"
      parameter=MAP_parameters()
      parameter.add_component(composant)
      parameter.add_parameter(composant, 'CS', CS)
      parameter.add_parameter(composant, 'CSJ', CSJ)
      parameter.add_parameter(composant, 'GS', GS)
      parameter.add_parameter(composant, 'GSJ', GSJ)
      parameter.add_parameter(composant, 'VMAX', VMAX)
      parameter.add_parameter(composant, 'VMAXJ', VMAXJ)
      parameter.write(DISPL_input)

      #commande= "cd "+ commponent_dir +";"
      #commande+= "python rbm.py -i "+DISPL_input+";\n"
      #os.system(commande)

      print "DISPL - END"


