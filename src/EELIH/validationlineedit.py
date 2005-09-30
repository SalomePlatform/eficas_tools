# -*- coding: iso-8859-1 -*-

# modules PyQt
from qt import *

class ValidationLineEdit:
    """
    crée un validateur pour un lineedit
    """
    def __init__(self, min, max, decimal, widget):
        """
        min = valeur minimale à saisir
        max = valeur maximale à saisir
        decimal = nombre de chiffres après la virgule autorisé
        widget = widget associé au validateur
        """
        self.widget = widget
        if min == None and max == None and decimal == None:
            val = QDoubleValidator(self.widget)
        else:
            val = QDoubleValidator(min, max, decimal, self.widget)
        self.widget.setValidator(val)
    
    def isValid(self):
        """
        si les données saisies dans le widget vérifient le validateur,
        le widget devient blanc sinon le widget est rose
        """
        correct = 0
        if self.widget.hasAcceptableInput():
            self.widget.setPaletteBackgroundColor(QColor(255, 255, 255))
            correct = 1
        else:
            self.widget.setPaletteBackgroundColor(QColor(255, 170, 255))
        
        return correct
    
