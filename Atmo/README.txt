pyxbgen -u modele_atmo.xsd -m atmo --write-for-customization
/local/PyXB-1.2.6/scripts/pyxbgen  -u modele_atmo.xsd -m atmo --write-for-customization
/local/PyXB-1.2.6/scripts/pyxbgen  -u model_atmo_ext.xsd -m atmo_ext --write-for-customization


/local/PyXB-1.2.6/scripts/pyxbgen  -u modele_atmo.xsd -m atmo --write-for-customization --default-namespace-public --archive-to-file=model_atmo.wxsd 
/local/PyXB-1.2.6/scripts/pyxbgen  -u model_atmo_ext.xsd -m atmo_ext --write-for-customization --archive-path=.:+
