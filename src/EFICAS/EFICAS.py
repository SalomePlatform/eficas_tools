import EFICAS_ORB__POA
import SALOME_ComponentPy

class EFICAS(EFICAS_ORB__POA.EFICAS_Gen,
              SALOME_ComponentPy.SALOME_ComponentPy_i):
    """
        Pour etre un composant SALOME cette classe Python
        doit avoir le nom du composant et heriter de la
        classe EFICAS_Gen issue de la compilation de l'idl
        par omniidl et de la classe SALOME_ComponentPy_i
        qui porte les services generaux d'un composant SALOME
    """
    def __init__ (self, orb, poa, contID, containerName, instanceName, 
                  interfaceName):
        print "EFICAS.__init__: ",containerName,' ',instanceName
        SALOME_ComponentPy.SALOME_ComponentPy_i.__init__(self, orb, poa,
                    contID, containerName,instanceName, interfaceName, 0 )
        # On stocke dans l'attribut _naming_service, une reference sur
        # le Naming Service CORBA
        self._naming_service=SALOME_ComponentPy.SALOME_NamingServicePy_i(self._orb)

