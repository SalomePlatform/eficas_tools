# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *

class ValidationLineEdit:
    """
    cr�e un validateur pour un lineedit
    """
    def __init__(self, min, max, decimal, widget):
        """
        min = valeur minimale � saisir
        max = valeur maximale � saisir
        decimal = nombre de chiffres apr�s la virgule autoris�
        widget = widget associ� au validateur
        """
        self.widget = widget
        if min == None and max == None and decimal == None:
            val = QDoubleValidator(self.widget)
        else:
            val = QDoubleValidator(min, max, decimal, self.widget)
        self.widget.setValidator(val)
    
    def isValid(self):
        """
        si les donn�es saisies dans le widget v�rifient le validateur,
        le widget devient blanc sinon le widget est rose
        """
        correct = 0
        if self.widget.hasAcceptableInput():
            self.widget.setPaletteBackgroundColor(QColor(255, 255, 255))
            correct = 1
        else:
            self.widget.setPaletteBackgroundColor(QColor(255, 170, 255))
        
        return correct
    
