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

class CatalogDescription:
    
    def __init__(self, identifier, cata_file_path, file_format = "python",
                 default = False, code = None, user_name = None,
                 selectable = True, file_format_in = "python"):
        """
        This class can be used to describe an Eficas catalog.

        :type  identifier: string
        :param identifier: unique identifier for the catalog
                
        :type  cata_file_path: string
        :param cata_file_path: path of the file containing the catalog itself
                
        :type  file_format: string
        :param file_format: format of the files generated when using this
                            catalog
                
        :type  default: boolean
        :param default: indicate if this catalog is the default one (appear on
                        the top of the catalogs list)
                
        :type  code: string
        :param code: Deprecated. Used to indicate the code associated to this
                     catalog
                
        :type  user_name: string
        :param user_name: name of the catalog as it will appear in the list
                
        :type  selectable: boolean
        :param selectable: indicate if this catalog appears in the list.
                           Setting this parameter to False is useful to keep
                           old catalogs to edit existing files but to forbid
                           to use them to create new files.
                
        """
        self.identifier = identifier
        self.cata_file_path = cata_file_path
        self.file_format = file_format
        self.default = default
        self.code = code
        if user_name is None:
            self.user_name = identifier
        else:
            self.user_name = user_name
        self.selectable = selectable
        self.file_format_in = file_format_in

    @staticmethod
    def create_from_tuple(cata_tuple):
        #print "Warning: Describing a catalog with a tuple is deprecated. " \
        #      "Please create a CatalogDescription instance directly."
        desc = CatalogDescription(code = cata_tuple[0],
                                  identifier = cata_tuple[1],
                                  cata_file_path = cata_tuple[2],
                                  file_format = cata_tuple[3])
        if len(cata_tuple) == 5:
            if cata_tuple[4] == "defaut":
                desc.default = True
            else:
                desc.file_format_in = cata_tuple[4]
        return desc
