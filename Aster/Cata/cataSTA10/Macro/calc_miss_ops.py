#@ AJOUT calc_miss_ops Macro
# -*- coding: iso-8859-1 -*-
# RESPONSABLE COURTOIS M.COURTOIS

import os


def calc_miss_ops(self, OPTION, **kwargs):
    """Macro CALC_MISS :
    Préparation des données et exécution d'un calcul MISS3D
    """
    from Utilitai.Utmess  import UTMESS, MessageError
    from Miss.miss_utils  import MISS_PARAMETER
    from Miss.miss_calcul import CalculMissFactory
    
    ier = 0
    # La macro compte pour 1 dans la numerotation des commandes
    self.set_icmd(1)

    # conteneur des paramètres du calcul
    param = MISS_PARAMETER(initial_dir=os.getcwd(), **kwargs)
    
    # création de l'objet CALCUL_MISS_xxx
    option_calcul = "TOUT"
    if OPTION["TOUT"] != "OUI":
        option_calcul = OPTION["MODULE"]
    calcul = CalculMissFactory(option_calcul, self, param)

    try:
        calcul.prepare_donnees()
        calcul.execute()
        calcul.post_traitement()
    except MessageError, err:
        UTMESS('F', err.id_message, valk=err.valk, vali=err.vali, valr=err.valr)

