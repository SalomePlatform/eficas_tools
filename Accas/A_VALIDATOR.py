# -*- coding: utf-8 -*-
import types
from Noyau import N_VALIDATOR
from Ihm import I_VALIDATOR

class FunctionVal(I_VALIDATOR.FunctionVal,N_VALIDATOR.FunctionVal):pass
class OrVal(I_VALIDATOR.OrVal,N_VALIDATOR.OrVal):pass
class AndVal(I_VALIDATOR.AndVal,N_VALIDATOR.AndVal):pass
class NoRepeat(I_VALIDATOR.NoRepeat,N_VALIDATOR.NoRepeat):pass
class LongStr(I_VALIDATOR.LongStr,N_VALIDATOR.LongStr):pass
class OrdList(I_VALIDATOR.OrdList,N_VALIDATOR.OrdList):pass
class RangeVal(I_VALIDATOR.RangeVal,N_VALIDATOR.RangeVal):pass
class EnumVal(I_VALIDATOR.EnumVal,N_VALIDATOR.EnumVal):pass
class TypeVal(I_VALIDATOR.TypeVal,N_VALIDATOR.TypeVal):pass
class PairVal(I_VALIDATOR.PairVal,N_VALIDATOR.PairVal):pass
class CardVal(I_VALIDATOR.CardVal,N_VALIDATOR.CardVal):pass
class InstanceVal(I_VALIDATOR.InstanceVal,N_VALIDATOR.InstanceVal):pass

def do_liste(validators):
    """
       Convertit une arborescence de validateurs en OrVal ou AndVal
       validators est une liste de validateurs ou de listes ou de tuples
    """
    valids=[]
    for validator in validators:
        if type(validator) == types.FunctionType:
           valids.append(FunctionVal(validator))
        elif type(validator) == types.TupleType:
           valids.append(OrVal(do_liste(validator)))
        elif type(validator) == types.ListType:
           valids.append(AndVal(do_liste(validator)))
        else:
           valids.append(validator)
    return valids

def validatorFactory(validator):
    if type(validator) == types.FunctionType:
       return FunctionVal(validator)
    elif type(validator) == types.TupleType:
       return OrVal(do_liste(validator))
    elif type(validator) == types.ListType:
       return AndVal(do_liste(validator))
    else:
       return validator

