import os
import sys

try :
   sys.path.append(os.path.join(os.getenv('MAP_DIRECTORY'),'classes/python/'))
   from class_MAP_parameters import *
except :
   pass

def component_pygmee_v2(rve_size, phase_number, sieve_curve_in, sieve_curve_out, repulsion_distance, study_name, study_path, file_result_inclusions, file_result_rve):
    print "pygmee_v2 for YACS - BEGIN"
    composant="pygmee_v2"
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

    pygmee_v2_input = study_path+"/pygmee_v2_for_YACS.input"

    commande=parameter.write_for_shell(pygmee_v2_input)
    os.system(commande)

    commande= "cd /local00/bin/MAP/components/pygmee_v2/src;"
    commande+= "python pygmee_v2.py -i "+pygmee_v2_input+";\n"
    os.system(commande)

    fd = open(file_result_rve, 'r')
    line=fd.readline()
    line=fd.readline()
    volume_fraction=float(line)
    print "volume_fraction =", volume_fraction
    fd.close()    

    print "pygmee_v2 for YACS - END"
    return volume_fraction

def component_fdvgrid(lambda_I, lambda_M, rve_size, file_inclusions, finesse):
    print "fdvgrid for YACS - BEGIN"
    
    contrast=1.
    if (lambda_M>0):
        contrast=lambda_I/lambda_M
    else:
        print "lambda_M =", lambda_M, "must be gratter than 0"
        exit(0)
        
    if (finesse < 32): finesse=32

    fdvgrid_path="/local00/bin/MAP/components/fdvgrid/bin"
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
    print "benhur_input", string_1
    print "benhur_command", commande

    print "benhur for YACS - END"
