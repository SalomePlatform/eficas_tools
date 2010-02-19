# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
   Ce module contient le plugin generateur de fichier au format 
   SEP pour EFICAS.

"""
import traceback
import types,string,re,os

from generator_python import PythonGenerator

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'perfect',
        # La factory pour creer une instance du plugin
          'factory' : PerfectGenerator,
          }


class PerfectGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format py 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def gener(self,obj,format='brut',config=None):
       self.text=PythonGenerator.gener(self,obj,format)
       self.generePythonPerfect()
       return self.text

   def generePythonPerfect(self) :
        '''
        '''
        import sys
        sys.path.append("/local/noyret/PERFECT/perfect_platform")
        print "avant import"
        import PDM 
        import PMM
        import PSM 
        print "apres import"
#!/usr/bin/env python



# script exported from study my new study
# generated using the PSM.ExportStudy package and the script_tmpl.py
# template

        import getopt, sys, time
        from PSM.PerfectStudy import ExecutionStatus
        
        short_opts = "dhst"
        long_opts = [
            "debug",
            "help",
            "save",
            "test",
        ]
        
        TXT_HELP = r"""
        SYNTAX:
            python script.py [options]
        DESCRIPTION:
            will launch the exported python script
        OPTIONS:
            -h, --help:
                print this help (and you found it!)
            -d, --debug:
                when enabled, if a module execution fails, the error messages of this
                module will be printed (default no)
            -s, --save:
                will save the study (format <study>.prf) when the computation is
                finished, if it has finished with no error (default no)
            -t, --test:
                will automatically look for a 'return_flag' produced by a comparison
                list in the current study, and will exit with a return code depending
                on the return_flag:
                    0 (normal exit) if the return_flag is 1 (criterion satisfied)
                    1 (error exit)  if the return_flag is 0 (criterion not satisfied)
                This is usefull especially for non-regression tests.
        """
        
        START_MESSAGE = r"""
        
                            +-------------------------+
                            |  PERFECT python script  |
                            +-------------------------+
        
        """
        
        DEBUG_MODE = False
        TEST_MODE = False
        SAVE_STUDY = False
        INDENT = 4*" "
        
        # set the options
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
        for opt,arg in opts:
            if opt in ("-h", "--help"):
                print TXT_HELP
                sys.exit(0)
            if opt in ("-d", "--debug"):
                DEBUG_MODE = True
            if opt in ("-s", "--save"):
                SAVE_STUDY = True
            if opt in ("-t", "--test"):
                TEST_MODE = True
        
        # 1st: determine and write what are the packages needed for the definition 
        #      of the input data
        from PDM.BasicUnits import Flux, Energy, Temperature, Time, DamageRate, Volume, Dimension, AtomicDensity, Stress
        from PDM.Crystal import IronBccCrystal
        from PDM.BasicTypes import PerfectFile, String, TableCoefficient, Coefficient, StringListChoice
        from PDM.Irradiation import NeutronSpectrum, OperatingConditions
        
        
        ################################################################################
        
        # 2nd: write study preferences and so on
        print START_MESSAGE
        print ">>> Defining study '%s'" % ("my new study")
        from PSM import PerfectStudy
        a_study = PerfectStudy.PerfectStudy()
        a_study.set_study({'date': '12/11/09', 'description': 'no description', 'filename': '/local/noyret/PerfectStudy/studies/my_new_new_study.prf', 'name': 'my new study', 'author': 'gadjanor'})
        
        # 3rd: write the study chain
        print ">>> Setting the study chain"
        a_study.set_chain_modules_path_list([['RPV2.IRRAD', 'PMM.RPV']])
            
        # 4th: list and write all input data needed
        print ">>> Defining the list of input data"
        specter_path = PerfectFile()
        specter_path.path = '/local/noyret/PERFECT/perfect_platform/tools/bin/specter.exe_64'
        specter_path.format = ''
        
        neutron_spectrum = NeutronSpectrum()
        neutron_spectrum.spectrum_description.value = 'Flux de neutrons total  osiris'
        col0 = Coefficient()
        col0.name = 'Energies'
        col0.value = 20.0
        col0.unit = 'MeV'
        col1 = Flux()
        col1.name = 'Fluxes'
        col1.value = 2213561344.0
        col1.unit = 'n_per_cm2_per_s'
        neutron_spectrum.spectrum.columns = [col0, col1]
        neutron_spectrum.spectrum.values = [[1.6195e-08, 157854046530.125], [3.2380000000000003e-08, 50535692980.711899], [6.9749999999999999e-08, 66380592563.133797], [1.5029999999999999e-07, 85471465500.099396], [3.2370000000000002e-07, 112865380791.41], [6.9729999999999998e-07, 132262477629.74699], [1.502e-06, 125499304036.588], [3.236e-06, 155325512030.22501], [6.9709999999999998e-06, 165859614237.423], [1.502e-05, 138404454165.83801], [3.235e-05, 136094651024.06], [6.9690000000000005e-05, 125096838337.642], [0.00015009999999999999, 169481805527.93799], [0.0003234, 126382978723.40401], [0.00069669999999999997, 74648637900.179001], [0.0015009999999999999, 147792404056.47198], [0.0032330000000000002, 174136408828.793], [0.0069649999999999998, 119086100616.425], [0.015010000000000001, 151134619208.59], [0.032320000000000002, 142105388745.27701], [0.069620000000000001, 212703121893.01999], [0.14999999999999999, 321412606880.09497], [0.1832, 294202425929.60797], [0.22370000000000001, 355893418174.58698], [0.40760000000000002, 392456551998.409], [0.49790000000000001, 482468880493.14001], [0.60809999999999997, 408021475442.43402], [0.74270000000000003, 580268045337.04504], [0.90720000000000001, 680368264068.40295], [1.1080000000000001, 628730165042.75195], [1.353, 567879101212.96497], [1.653, 633883000000.0], [2.0190000000000001, 726967000000.0], [2.4660000000000002, 584931000000.0], [3.012, 627575000000.0], [3.6789999999999998, 484280000000.0], [4.4930000000000003, 354030000000.0], [5.4880000000000004, 259284000000.0], [6.7030000000000003, 214234000000.0], [8.1869999999999994, 119961000000.0], [10.0, 63117120700.0], [14.960000000000001, 24112944919.0], [20.0, 2213561344.0]]
        
        operating_conditions = OperatingConditions()
        operating_conditions.flux_cut_off_energy.name = ''
        operating_conditions.flux_cut_off_energy.value = 1.0
        operating_conditions.flux_cut_off_energy.unit = 'MeV'
        operating_conditions.temp_irrad.name = 'T'
        operating_conditions.temp_irrad.value = 573.0
        operating_conditions.temp_irrad.unit = 'K'
        operating_conditions.time_irrad.name = ''
        operating_conditions.time_irrad.value = 10000000.0
        operating_conditions.time_irrad.unit = 's'
        col0 = Coefficient()
        col0.name = 'relative_time'
        col0.value = 1.0
        col0.unit = ''
        operating_conditions.relative_time_increments.columns = [col0]
        operating_conditions.relative_time_increments.values = [[1e-10], [1.0000000000000001e-09], [3e-09], [1e-08], [2.9999999999999997e-08], [9.9999999999999995e-08], [2.9999999999999999e-07], [9.9999999999999995e-07], [3.0000000000000001e-06], [1.0000000000000001e-05], [3.0000000000000001e-05], [0.0001], [0.00029999999999999997], [0.001], [0.0030000000000000001], [0.01], [0.029999999999999999], [0.10000000000000001], [0.29999999999999999], [1.0]]
        operating_conditions.rescaling_flux.name = ''
        operating_conditions.rescaling_flux.value = 0.0
        operating_conditions.rescaling_flux.unit = 'n_per_cm2_per_s'
        operating_conditions.rescaling_NRT_damage_rate.name = ''
        operating_conditions.rescaling_NRT_damage_rate.value = 0.0
        operating_conditions.rescaling_NRT_damage_rate.unit = 'dpa_per_s'
        
        bcc_crystal = IronBccCrystal()
        bcc_crystal.atomic_volume.name = ''
        bcc_crystal.atomic_volume.value = 1.18199515e-29
        bcc_crystal.atomic_volume.unit = 'm3'
        bcc_crystal.lattice_parameter.name = 'Dimension'
        bcc_crystal.lattice_parameter.value = 2.87
        bcc_crystal.lattice_parameter.unit = 'angstrom'
        bcc_crystal.atomic_density.name = ''
        bcc_crystal.atomic_density.value = 8.46027160095e+28
        bcc_crystal.atomic_density.unit = 'at_per_m3'
        bcc_crystal.mu.name = 'Sigma'
        bcc_crystal.mu.value = 70.0
        bcc_crystal.mu.unit = 'GPa'
        bcc_crystal.structure.string_list = ['bcc', 'fcc']
        bcc_crystal.structure.value = 'bcc'
        bcc_crystal.nu.name = ''
        bcc_crystal.nu.value = 0.3
        bcc_crystal.nu.unit = ''
        
        a_study.perfect_chain.set_dict_inputs({
            'specter_path': specter_path,
            'neutron_spectrum': neutron_spectrum,
            'operating_conditions': operating_conditions,
            'bcc_crystal': bcc_crystal,
        })
        
        
        # 5th: checks if the study is correctly defined
        print ">>> Assert if the study is correctly defined"
        if not a_study.ok():
            raise AssertionError
        print INDENT + "Ok."
        
        # 6th: initilize study execution callbacks
        def current_module_changed(the_module):
            print INDENT + 60*"-"
            print INDENT + ">>> Module " + the_module.get_absolute_name()
            pass
        
        a_study.on_current_module_changed = current_module_changed
        
        def progress_value_changed(the_progress_value):
            sys.stdout.write( 2*INDENT + "- Completed: %4.1f %%\r" % (the_progress_value*100.) )
            sys.stdout.flush()
            pass
        
        a_study.on_progress_value_changed = progress_value_changed
        
        # 7th: launch the study and wait till it will finish
        print "creating new script"
        parser_module = __import__(
            'Parser.perfect_filtre',
            globals(), locals(), ['perfect_filtre']
        )
        setattr(parser_module, 'current_study', a_study)
        template_py_file = '/local/noyret/PERFECT/perfect_platform/PSM/script_tmpl.py'
        this_params = parser_module.analyse( template_py_file )
        print "this_params ", this_params
        parser_module.perf_filter( this_params, "/local/noyret/new_script_eficas.py" )
        print "fin parser_module"

        
        #a_study.run_study()
        #a_study.wait()
        
        ## 8th: process the study execution output
        #print INDENT + 60*"-"
        #print ">>> Execution finished."
        #print INDENT + "Final status of the execution:", a_study.get_status()
        
        ## if DEBUG_MODE is set, and the study is finished with an error,
        ## prints information on the failed last module
        #if a_study.get_execution_status() == ExecutionStatus.Failed and DEBUG_MODE:
            #print ">>> Standard messages of the last module:"
            #print a_study.get_execution_stack()[-1][0]
            #print ">>> Error messages of the last module:"
            #print a_study.get_execution_stack()[-1][1]
            #sys.exit(1)
        
        ## if SAVE_STUDY is set, saves the study
        #if SAVE_STUDY:
            #print ">>> Saving the study"
            #a_study.save()
        
        ## if TEST_MODE is set, return a code depending on the return flag
        #if TEST_MODE:
            #return_flag = a_study.get_final_dict()['return_flag'].value
            #discrepency = a_study.get_final_dict()['discrepency'].value
            #print ">>> Comparison with reference curve(s) returned the value:", \
                    #discrepency
            #if return_flag:
                #print INDENT + "which is under the criterion"
                #sys.exit( 0 )
            #else:
                #print INDENT + "which is not under the criterion"
                #sys.exit( 1 )
        
        # End of script

        return 'a faire'
    
