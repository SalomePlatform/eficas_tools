import N_MACRO
import N_FORM_ETAPE

class FORM(N_MACRO.MACRO):
    """
       Cette classe sert à définir dans le catalogue des objets de type
       FORMULE pour ASTER.
       Elle surcharge la classe MACRO
    """
    class_instance=N_FORM_ETAPE.FORM_ETAPE

