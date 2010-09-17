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

import os

from generator_python import PythonGenerator


def entryPoint():
    """
    Return a dictionary containing the description needed to load the plugin
    """
    return {'name' : 'file_from_template',
            'factory' : FileFromTemplateGenerator}


class FileFromTemplateGenerator(PythonGenerator):
    """
    This generator creates an output file from a template (file with holes) in
    addition to Eficas .comm file. The parts to replace in the template must be
    in the form %KEYWORD%, where KEYWORD may be either the name of the Eficas
    element (short form, for instance MY_MCSIMP) or the "path" to the Eficas
    element (long form, for instance MYPROC.MYBLOC.MY_MCSIMP).
    
    To use this generator, the configuration of the code must implement two
    methods: get_extension() that must return the extension of the output file
    and get_template_file() that must return the path of the template file. Be
    sure also that your catalog is coherent with your template file.
    """
    
    def gener(self, obj, format = 'brut', config = None):
        self.config = config
        self.kw_dict = {}
        self.text = PythonGenerator.gener(self, obj, format)
        self.generate_output_from_template()
        return self.text
    
    def generate_output_from_template(self) :
        """
        Generate the output text from the template file and the keywords
        """
        templateFileName = self.config.get_template_file()
        if not os.path.isfile(templateFileName):
            raise Exception("Template file %s does not exist." %
                            templateFileName)
        f = file(templateFileName, "r")
        template = f.read()  
        f.close()
        self.output_text = self.replace_keywords(template)

    def generMCSIMP(self, obj) :
        """
        Save object value in the keyword dict for further use, then generate
        the text corresponding to the MCSIMP element.
        """
        short_keyword = obj.nom.strip()
        long_keyword = ""
        for i in obj.get_genealogie()[:-1]:
            long_keyword += i + "."
        long_keyword += short_keyword
        self.kw_dict[short_keyword] = obj.valeur
        self.kw_dict[long_keyword] = obj.valeur
        return PythonGenerator.generMCSIMP(self, obj)

    def replace_keywords(self, template_string):
        result = template_string
        for item in self.kw_dict.iteritems():
            replace_str = "%" + item[0] + "%"
            result = result.replace(replace_str, str(item[1]))
        return result
    
    def writeDefault(self, basefilename):
        output_filename = os.path.splitext(basefilename)[0] + \
                          self.config.get_extension()
        f = open(output_filename, 'w')
        f.write(self.output_text)
        f.close()
