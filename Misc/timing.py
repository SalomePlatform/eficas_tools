import time
f=open('timing.out','w')
temps={}

def debut(event):
   #temps[event]=time.clock()
   temps[event]=time.time()

def fin(event):
   #temps[event]=time.clock()-temps[event]
   temps[event]=time.time()-temps[event]
   f.write("%s %.4f\n"%(event,temps[event]))
