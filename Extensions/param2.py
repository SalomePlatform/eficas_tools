# -*- coding: utf-8 -*-
from __future__ import division
import math
import Numeric
import types

def mkf(value):
    if type(value) in (type(1), type(1L), type(1.5), type(1j),type("hh")) :
        return Constant(value)
    elif isinstance(value, Formula):
        return value
    elif type(value) == type([]):
        return Constant(value)
    else:
#        return Constant(value)
        raise TypeError, ("Can't make formula from", value)

#class Formula(object):
class Formula:
    def __len__(self):
        val=self.eval()
        if val is None:return 0
        try:
           return len(val)
        except:
           return 1
    def __complex__(self): return complex(self.eval())
    def __int__(self): return int(self.eval())
    def __long__(self): return long(self.eval())
    def __float__(self): return float(self.eval())
    def __pos__(self): return self  # positive
    def __neg__(self): return Unop('-', self)
    def __add__(self, other): return Binop('+', self, other)
    def __radd__(self, other): return Binop('+', other, self)
    def __sub__(self, other): return Binop('-', self, other)
    def __rsub__(self, other): return Binop('-', other, self)
    def __mul__(self, other): return Binop('*', self, other)
    def __rmul__(self, other): return Binop('*', other, self)
    def __div__(self, other): return Binop('/', self, other)
    def __truediv__(self, other): return Binop('/', self, other)
    def __rdiv__(self, other): return Binop('/', other, self)
    def __pow__(self, other): return Binop('**', self, other)
    def __rpow__(self, other): return Binop('**', other, self)
    def __getitem__(self,i):return Binop('[]',self,i)

class Binop(Formula):
    opmap = { '+': lambda a, b: a + b,
              '*': lambda a, b: a * b,
              '-': lambda a, b: a - b,
              '/': lambda a, b: a / b,
              '**': lambda a, b: a ** b,
              '[]': lambda a, b: a[b] ,
            }
    def __init__(self, op, value1, value2):
        self.op = op
        self.values = mkf(value1), mkf(value2)
    def __str__(self):
        if self.op == '[]':
           return "%s[%s]" % (self.values[0], self.values[1])
        else:
           return "(%s %s %s)" % (self.values[0], self.op, self.values[1])
    def __repr__(self):
        if self.op == '[]':
           return "%s[%s]" % (self.values[0], self.values[1])
        else:
           return "(%s %s %s)" % (self.values[0], self.op, self.values[1])
    def eval(self):
        result= self.opmap[self.op](self.values[0].eval(),
                                   self.values[1].eval())
        while isinstance(result,Formula):
              result=result.eval()
        return result
    def __adapt__(self,validator):
        return validator.adapt(self.eval())


class Unop(Formula):
    opmap = { '-': lambda x: -x,
             }
    def __init__(self, op, arg):
        self._op = op
        self._arg = mkf(arg)
    def __str__(self):
        return "%s(%s)" % (self._op, self._arg)
    def __repr__(self):
        return "%s(%s)" % (self._op, self._arg)
    def eval(self):
        return self.opmap[self._op](self._arg.eval())
    def __adapt__(self,validator):
        return validator.adapt(self.eval())

class Unop2(Unop):
    def __init__(self, nom, op, arg):
        self._nom = nom
        self._op = op
        self._arg=[]
        for a in arg:
           self._arg.append(mkf(a))
    def __str__(self):
        s="%s(" % self._nom
        for a in self._arg:
           s=s+str(a)+','
        s=s+")"
        return s
    def __repr__(self):
        s="%s(" % self._nom
        for a in self._arg:
           s=s+str(a)+','
        s=s+")"
        return s
    def eval(self):
        l=[]
        for a in self._arg:
          l.append(a.eval())
        return self._op(*l)

class Constant(Formula):
    def __init__(self, value): self._value = value
    def eval(self): return self._value
    def __str__(self): return str(self._value)
    def __adapt__(self,validator):
        return validator.adapt(self._value)

class Variable(Formula):
    def __init__(self,name,value):
        self._name=name
        self._value=value
    def eval(self): return self._value
    def __repr__(self): return "Variable('%s',%s)" % (self._name, self._value)
    def __str__(self): return self._name
    def __adapt__(self,validator):
        return validator.adapt(self._value)

def Eval(f):
    if isinstance(f,Formula):
        f=f.eval()
    elif type(f) in (types.ListType, ):
        f=[Eval(i) for i in f]
    elif type(f) in (types.TupleType,):
        f=tuple([Eval(i) for i in f])
    return f


#surcharge de la fonction cos de Numeric pour les parametres
original_ncos=Numeric.cos
def cos(f): return Unop('ncos', f)
Unop.opmap['ncos']=lambda x: original_ncos(x)
Numeric.cos=cos

#surcharge de la fonction sin de Numeric pour les parametres
original_nsin=Numeric.sin
def sin(f): return Unop('nsin', f)
Unop.opmap['nsin']=lambda x: original_nsin(x)
Numeric.sin=sin

#surcharge de la fonction array de Numeric pour les parametres
original_narray=Numeric.array
def array(f,*tup,**args): 
    """array de Numeric met en défaut la mécanique des parametres
       on la supprime dans ce cas. Il faut que la valeur du parametre soit bien définie
    """
    return original_narray(Eval(f),*tup,**args)
Numeric.array=array

#surcharge de la fonction sin de math pour les parametres
original_sin=math.sin
def sin(f): return Unop('sin', f)
Unop.opmap['sin']=lambda x: original_sin(x)
math.sin=sin

#surcharge de la fonction cos de math pour les parametres
original_cos=math.cos
Unop.opmap['cos']=lambda x: original_cos(x)
def cos(f): return Unop('cos', f)
math.cos=cos

#surcharge de la fonction sqrt de math pour les parametres
original_sqrt=math.sqrt
def sqrt(f): return Unop('sqrt', f)
Unop.opmap['sqrt']=lambda x: original_sqrt(x)
math.sqrt=sqrt

#surcharge de la fonction ceil de math pour les parametres
original_ceil=math.ceil
Unop.opmap['ceil']=lambda x: original_ceil(x)
def ceil(f): return Unop('ceil', f)
math.ceil=ceil
