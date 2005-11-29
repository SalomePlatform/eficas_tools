from __future__ import division
import math

def mkf(value):
    if type(value) in (type(1), type(1L), type(1.5), type(1j),type("hh")):
        return Constant(value)
    elif isinstance(value, Formula):
        return value
    else:
        raise TypeError, ("Can't make formula from", value)

class Formula(object):
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
           return "(%s[%s])" % (self.values[0], self.values[1])
        else:
           return "(%s %s %s)" % (self.values[0], self.op, self.values[1])
    def __repr__(self):
        if self.op == '[]':
           return "(%s[%s])" % (self.values[0], self.values[1])
        else:
           return "(%s %s %s)" % (self.values[0], self.op, self.values[1])
    def eval(self):
        result= self.opmap[self.op](self.values[0].eval(),
                                   self.values[1].eval())
        while isinstance(result,Formula):
              result=result.eval()
        return result

class Unop(Formula):
    opmap = { '-': lambda x: -x,
              'sin': lambda x: math.sin(x),
              'cos': lambda x: math.cos(x) }
    def __init__(self, op, arg):
        self._op = op
        self._arg = mkf(arg)
    def __str__(self):
        return "%s(%s)" % (self._op, self._arg)
    def eval(self):
        return self.opmap[self._op](self._arg.eval())

class Constant(Formula):
    def __init__(self, value): self._value = value
    def eval(self): return self._value
    def __str__(self): return str(self._value)

def cos(f): return Unop('cos', f)
def sin(f): return Unop('sin', f)
