import os
import sys

try :
   sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'),'classes/python/'))
   from class_MAP_parameters import *
except :
   pass

class component_pygmee_v2:

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
def component_fdvgrid(lambda_I, lambda_M, rve_size, file_inclusions, finesse):
    print "fdvgrid for YACS - BEGIN"
    
    contrast=1.
    if (lambda_M>0):
        contrast=lambda_I/lambda_M
    else:
        print "lambda_M =", lambda_M, "must be gratter than 0"
        exit(0)
        
    if (finesse < 32): finesse=32

    fdvgrid_path="/local/noyret/MAP/components/fdvgrid/bin"
    commande= "cd "+fdvgrid_path+";\n"
    commande+= "echo "+ str(rve_size)+" > "+"rve.input"+";\n"
    commande+= "cp " + file_inclusions+" "+"inclusions.input"+";\n"
    commande+= "echo "+str(contrast)+" > "+"contrast.input"+";\n"
    commande+= "./fdvgrid 3D 1.0 0.0 0.0 v t "+str(finesse)+" cross 1e-6 "+";\n"
    os.system(commande)

    fd = open(fdvgrid_path+"/"+"lambda_x.output", 'r')
    line=fd.readline()
    lambda_x=float(line)
    print "lambda_x =", lambda_x
    fd.close()

    print "fdvgrid for YACS - END"
    return lambda_x

def remplaceDICO(chaine,dico) :
    for mot in dico.keys() :
       rplact="%"+mot+"%"
       result=chaine.replace(rplact,str(dico[mot]))
       chaine=result
    return chaine

def component_benhur(finesse, rve_size, inclusion_name, study_name, study_path):
    print "benhur for YACS - BEGIN"

    finesse=int(finesse)

    Template_path=os.path.join(os.getenv('EFICAS_ROOT'), 'MAP/Templates/s_polymers_st_1/')
    monFichierInput=Template_path+"benhur_template.txt"
    monFichierOutput=Template_path+"s_polymers_st_1_benhur_"+str(finesse)+".bhr"

    benhur_path=os.path.join(os.getenv('MAP_DIRECTORY'), 'components/benhur/')

    f = file(monFichierInput)
    string_0 = f.read()  
    f.close()
    # find and replace with BENHUR dictionnary
    dicoBenhur=dict()
    dicoBenhur["_RVE_SIZE"]=rve_size
    dicoBenhur["_MESH_SIZE"]=finesse
    dicoBenhur["_INCLUSION_FILE"]=inclusion_name
    dicoBenhur["_PATH_STUDY"]=study_path
    dicoBenhur["_NAME_SCHEME"]=study_name
    dicoBenhur["_PATH_BENHUR"]=benhur_path
    string_1=remplaceDICO(string_0,dicoBenhur)
    # write into ouput file
    f=open(monFichierOutput,'wb')
    f.write(string_1)
    f.close()
    # launch of BENHUR on the previous file
    benhur_path=os.path.join(os.getenv('MAP_DIRECTORY'),'components/benhur/')
    commande="cd "+benhur_path+"/bin;\n"
    commande+="./benhur -i "+monFichierOutput+";\n"
    os.system(commande)

    result_mesh=study_path+'/'+study_name+'_benhur_'+str(finesse)+'.msh'
    result_log=study_path+'/'+study_name+'_benhur_'+str(finesse)+'.log'

    print 'result_mesh =', result_mesh
    print 'result_log =', result_log

    print "benhur for YACS - END"

    return (result_mesh, result_log)

def component_aster_s_polymers_st_1(rve_size, finesse, lambda_I, lambda_M, study_name, study_path, aster_path):
    print "aster_s_polymers_st_1 for YACS - BEGIN"

    finesse=int(finesse)
    
    Template_path=os.path.join(os.getenv('EFICAS_ROOT'), 'MAP/Templates/s_polymers_st_1/')
    monFichierCommInput=Template_path+"s_polymers_st_1_aster_template.comm"
    monFichierExportInput=Template_path+"s_polymers_st_1_aster_template.export"

    monFichierCommOutput=study_path+"/s_polymers_st_1_aster.comm"
    monFichierExportOutput=study_path+"/s_polymers_st_1_aster.export"
    # Lecture du fichier a trous a pour le fichier export
    f = file(monFichierExportInput)
    string_0 = f.read()  
    f.close()         
    # find and replace with CODE_ASTER dictionnary
    dicoAster=dict()
    dicoAster["_MESH_SIZE"]=str(finesse)
    dicoAster["_ASTER_VERSION"]="STA10"
    dicoAster["_NAME_STUDY"]="s_polymers_st_1"
    dicoAster["_PATH_STUDY"]=study_path
    dicoAster["_CONDUCTIVITE_I"]=str(lambda_I)
    dicoAster["_CONDUCTIVITE_M"]=str(lambda_M)
    string_1=remplaceDICO(string_0,dicoAster)
    # write into output file
    f=open(monFichierExportOutput,'wb')
    f.write(string_1)
    f.close()

    # Lecture du fichier a trous a pour le fichier comm
    f = file(monFichierCommInput)
    string_0 = f.read()  
    f.close()   
    # find and replace with CODE_ASTER dictionnary
    # find and replace with CODE_ASTER dictionnary
    dicoAster=dict()
    dicoAster["_RVE_SIZE"]=str(rve_size)
    dicoAster["_CONDUCTIVITE_I"]=str(lambda_I)
    dicoAster["_CONDUCTIVITE_M"]=str(lambda_M)
    string_1=remplaceDICO(string_0,dicoAster)
    # write into output file
    f=open(monFichierCommOutput,'wb')
    f.write(string_1)
    f.close()
    
    # launch of CODE_ASTER on the study
    commande="cd "+study_path+";"
    commande+=commande + aster_path + "/as_run "+monFichierExportOutput +";\n"
    os.system(commande)
    
    print "aster_s_polymers_st_1 for YACS - END"

    result_gmsh=study_path+"/s_polymers_st_1_aster.resu.msh"

    return result_gmsh

def component_gmsh_post(result_gmsh):
    print "gmsh_post for YACS - BEGIN"
    commande="gmsh "+result_gmsh+";"
    os.system(commande)
    
    print "gmsh_post for YACS - END"

    return
