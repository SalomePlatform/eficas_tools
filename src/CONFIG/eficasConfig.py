import os

# répertoire du logiciel Eficas
eficasPath = ''
if "EFICAS_ROOT" in os.environ:
    eficasPath = os.environ["EFICAS_ROOT"]

