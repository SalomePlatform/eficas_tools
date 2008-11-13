indent = 0
indStr = '  '

def srepr(*argl,**argd):
  #parse the arguments and create a string representation
  args = []
  for item in argl:
      args.append('%s' % str(item))
  for key,item in argd.items():
      args.append('%s=%s' % (key,str(item)))
  argstr = ','.join(args)   
  return argstr

def logfunc(f):
  def _method(*argl,**argd):
    global indent
    print indStr*indent+f.__module__+"."+f.__name__+"("+srepr(*argl,**argd)+")"
    indent += 1
    r=f(*argl,**argd)
    indent -= 1
    print indStr*indent+str(r)
    return r
  return _method

def logmeth(f):
  def _method(self,*argl,**argd):
    global indent
    print indStr*indent+str(self)+"."+f.__name__+"("+srepr(*argl,**argd)+")"
    indent += 1
    r=f(self,*argl,**argd)
    indent -= 1
    print indStr*indent+str(r)
    return r
  return _method

if __name__ == "__main__":
  @logfunc
  def g(a,b):
    return a
  class A:
    @logmeth
    def h(self,a):
      return g(a,a)

  g(1,2)
  a=A()
  a.h(1)
