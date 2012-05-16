# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
class CatalogDescription:
    
    def __init__(self, identifier, cata_file_path, file_format = "python",
                 default = False, code = None,ss_code=None, user_name = None,
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
                
        :type  ss_code: string
        :param ss_code: scheme associated to this catalog (Map only)

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
