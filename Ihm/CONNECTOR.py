# -*- coding: iso-8859-15 -*-
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
"""
  La classe CONNECTOR sert à enregistrer les observateurs d'objets et à délivrer
  les messages émis à ces objets.

  Le principe général est le suivant : un objet (subscriber) s'enregistre aupres du 
  connecteur global (theconnector) pour observer un objet emetteur de messages (publisher) 
  sur un canal donné (channel). Il demande à etre notifie par appel d'une fonction (listener).
  La séquence est donc :

     - enregistrement du subscriber pour le publisher : theconnector.Connect(publisher,channel,listener,args)
     - émission du message par le publisher : theconnector.Emit(publisher,channel,cargs)

  args et cargs sont des tuples contenant les arguments de la fonction listener qui sera appelée
  comme suit::

     listener(cargs+args)
"""
import traceback
from copy import copy

class CONNECTOR:

  def __init__(self):
    self.connections={}

  def Connect(self, object, channel, function, args):
    ###print "Connect",object, channel, function, args
    idx = id(object)
    if self.connections.has_key(idx):
       channels = self.connections[idx]
    else:
       channels = self.connections[idx] = {}

    if channels.has_key(channel):
       receivers = channels[channel]
    else:
       receivers = channels[channel] = []

    info = (function, args)
    if info in receivers:
       receivers.remove(info)
    receivers.append(info)
    ###print "Connect",receivers
    

  def Disconnect(self, object, channel, function, args):
    try:
       receivers = self.connections[id(object)][channel]
    except KeyError:
       raise ConnectorError, \
            'no receivers for channel %s of %s' % (channel, object)
    try:
       receivers.remove((function, args))
    except ValueError:
       raise ConnectorError,\
          'receiver %s%s is not connected to channel %s of %s' \
          % (function, args, channel, object)

    if not receivers:
       # the list of receivers is empty now, remove the channel
       channels = self.connections[id(object)]
       del channels[channel]
       if not channels:
          # the object has no more channels
          del self.connections[id(object)]

  def Emit(self, object, channel, *args):
    ###print "Emit",object, channel, args
    try:
       receivers = self.connections[id(object)][channel]
    except KeyError:
       return
    ###print "Emit",object, channel, receivers
    # Attention : copie pour eviter les pbs lies aux deconnexion reconnexion
    # pendant l'execution des emit
    for func, fargs in copy(receivers):
       try:
          apply(func, args + fargs)
       except:
          traceback.print_exc()

_the_connector =CONNECTOR()
Connect = _the_connector.Connect
Emit = _the_connector.Emit 
Disconnect = _the_connector.Disconnect

if __name__ == "__main__":
   class A:pass
   class B:
     def add(self,a):
       print "add",a

   a=A()
   b=B()
   Connect(a,"add",b.add,())
   Emit(a,"add",1)
