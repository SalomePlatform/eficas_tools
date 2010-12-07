import os
import sys

try :
   sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'),'classes/python/'))
   from class_MAP_parameters import *
except :
   pass

#------------------------
class component_template :
#------------------------
# classe de base pour les composants utilisant un fichier  trou
# a mettre dans les class_MAP_parameters ??

   def creeFichierTemplate(self,templateInput, fichierOutput, listeVariables, dico):
       f = file(templateInput)
       stringInput = f.read()  
       f.close()

       # find and replace with dictionnary
       for nomVar in listeVariables:
           chaineARemplacer="%_"+nomVar.upper()+"%"
           valeur=dico[nomVar]
           stringInput=stringInput.replace(chaineARemplacer,str(valeur))

       # write into ouput file
       f=open(fichierOutput,'wb')
       f.write(stringInput)
       f.close()

#-------------------------
class component_pygmee_v2:
#-------------------------

   def __init__(self,rve_size, phase_number, sieve_curve_in, sieve_curve_out, repulsion_distance, 
                 study_name, study_path, file_result_inclusions, file_result_rve):
      print "pygmee_v2 for YACS - BEGIN"
      composant="pygmee_v2"
      pygmee_v2_input = study_path+"/pygmee_v2_for_YACS.input"
      parameter=MAP_parameters()
      parameter.add_component(composant)
      parameter.add_parameter(composant, 'rve_size', rve_size)
      parameter.add_parameter(composant, 'phase_number', phase_number)
      parameter.add_parameter(composant, 'sieve_curve_in', sieve_curve_in)
      parameter.add_parameter(composant, 'sieve_curve_out',  sieve_curve_out)
      parameter.add_parameter(composant, 'repulsion_distance', repulsion_distance)
      parameter.add_parameter(composant, 'study_name', study_name)
      parameter.add_parameter(composant, 'file_result_inclusions', file_result_inclusions)
      parameter.add_parameter(composant, 'file_result_rve', file_result_rve)
      parameter.write_for_shell(pygmee_v2_input)

      commponent_dir= os.path.join(os.getenv('MAP_DIRECTORY'),'components/pygmee_v2/src')
      commande= "cd "+ commponent_dir +";"
      commande+= "python pygmee_v2.py -i "+pygmee_v2_input+";\n"
      os.system(commande)

      fd = open(file_result_rve, 'r')
      line=fd.readline()
      self.volume_fraction=float(line)
      print "volume_fraction =",self.volume_fraction
      fd.close()    

      print "pygmee_v2 for YACS - END"

   def __call__(self,rve_size, phase_number, sieve_curve_in, sieve_curve_out, repulsion_distance, 
                 study_name, study_path, file_result_inclusions, file_result_rve):
        
      return self.volume_fraction



#-----------------------
class component_fdvgrid:
#-----------------------

   def  __init__(self,lambda_I, lambda_M, rve_size, file_inclusions, finesse):
      print "fdvgrid for YACS - BEGIN"
    
      contrast=lambda_I/lambda_M
      if (finesse < 32): finesse=32

      component_dir=os.path.join(os.getenv('MAP_DIRECTORY'),'components/fdvgrid/bin')
      commande = "cd "+fdvgrid_path+";\n"
      commande+= "cp " + file_inclusions+" "+"inclusions.input"+";\n"
      commande+= "./fdvgrid 3D 1.0 0.0 0.0 v t "+str(finesse)+" cross 1e-6 "+";\n"
      os.system(commande)

      fd = open(fdvgrid_path+"/"+"lambda_x.output", 'r')
      line=fd.readline()
      self.lambda_x=float(line)
      fd.close()
      print "fdvgrid for YACS - END"

   def __call__(self,lambda_I, lambda_M, rve_size, file_inclusions, finesse):
      return self.lambda_x

#-------------------------------------------
class component_benhur(component_template) :
#-------------------------------------------

    def __init__(self,mesh_size, rve_size, inclusion_file, name_scheme, path_study):
    #------------------------------------------------------------------------------
       print "benhur for YACS - BEGIN"

       Template_path=os.path.join(os.getenv('EFICAS_ROOT'), 'MAP/Templates/s_polymers_st_1/')
       path_benhur=os.path.join(os.getenv('MAP_DIRECTORY'), 'components/benhur/')

       templateInput  = Template_path+"benhur_template.txt"
       monFichierOutput = Template_path+"s_polymers_st_1_benhur_"+str(mesh_size)+".bhr"
       lVar=('mesh_size','rve_size','inclusion_file','path_study','name_scheme','path_benhur')
       self.creeFichierTemplate(templateInput, monFichierOutput, lVar, locals())

       # launch of BENHUR on the previous file
       benhur_path = os.path.join(os.getenv('MAP_DIRECTORY'),'components/benhur/')
       commande="cd "+benhur_path+"/bin;\n"
       commande+="./benhur -i "+monFichierOutput+";\n"
       os.system(commande)
   
       self.result_mesh=path_study+'/'+name_scheme+'_benhur_'+str(mesh_size)+'.msh'
       self.result_log=path_study+'/'+name_scheme+'_benhur_'+str(mesh_size)+'.log'
   

    def __call__(self, mesh_size, rve_size, inclusion_file, name_scheme, path_study):
    #------------------------------------------------------------------------------
       return (self,result_mesh, self.result_log)


#----------------------------------------------------------
class component_aster_s_polymers_st_1 (component_template):
#----------------------------------------------------------

    def __init__(self,rve_size, mesh_size, conductivite_i, conductivite_m, name_study, 
                 path_study, aster_path):
    #------------------------------------------------------------------------------
       print "aster_s_polymers_st_1 for YACS - BEGIN"
       aster_version="STA10"
       Template_path=os.path.join(os.getenv('EFICAS_ROOT'), 'MAP/Templates/s_polymers_st_1/')

       # Gestion du .comm
       lVarC=('rve_size','conductivite_i','conductivite_m')
       templateCommInput=Template_path+"s_polymers_st_1_aster_template.comm"
       monFichierCommOutput=study_path+"/s_polymers_st_1_aster.comm"
       self.creeFichierTemplate(templateCommInput, monFichierCommOutput, lVarC, locals())

       # Gestion du .export
       lVarE=('mesh_size','aster_version','name_study','path_study')
       templateExportInput=Template_path+"s_polymers_st_1_aster_template.export"
       monFichierExportOutput=study_path+"/s_polymers_st_1_aster.export"
       self.creeFichierTemplate(templateExportInput, monFichierExportOutput, lVarE, locals())
    
       # launch of CODE_ASTER on the study
       commande="cd "+study_path+";"
       commande+=commande + aster_path + "/as_run "+monFichierExportOutput +";\n"
       os.system(commande)
       self.result_gmsh=study_path+"/s_polymers_st_1_aster.resu.msh"
       print "aster_s_polymers_st_1 for YACS - END"
    
    def __call__(self,rve_size, mesh_size, conductivite_i, conductivite_m, name_study, 
                 path_study, aster_path):
    #------------------------------------------------------------------------------
       return result_gmsh

#-------------------------
class component_gmsh_post :
#-------------------------
    def __init__(self,result_gmsh):
    #--------------------------
       commande="gmsh "+result_gmsh+";"
       os.system(commande)
       print "gmsh_post for YACS - END"

    def __call__(self, result_gmsh):
    #-------------------------------
        return 1
