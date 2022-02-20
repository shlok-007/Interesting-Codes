import random as r
a=['SO4','NO3','Cl','Br','I']
b=['NH4','Pb','Cu','Fe','Al','Ni','Co','Zn','Ca','Ba']
while(True):
      i=input('press any alphabet or digit to continue and n to quit=')
      if(i in 'nN'):
            break
      else:
            print(r.choice(b)+r.choice(a))
