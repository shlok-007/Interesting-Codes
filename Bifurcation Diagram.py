print('plotting your graph...')
import matplotlib.pyplot as p
l1=[]
l2=[]
R=10                           #resolution
scale=25*R
itera=100*R
lc=len(str(1/itera).split('.')[1])
for i in range(itera):         #for values of r(rate)
      r=i/scale
      z1=0.5
      x=[]
      y=[]
      for j in range(500):    #for increasing accuracy in population
            z2=r*z1*(1-z1)
            z1=z2
      for k in range(itera):   #for getting all values of population
            z2=r*z1*(1-z1)
            z=round(z2,lc)
            if(not z in y):
                  x+=[r]
                  y+=[z]
            z1=z2
      l1+=x
      l2+=y
p.xlabel('Rate')
p.ylabel('Population')
p.title('Bifurcation Diagram')
p.scatter(l1,l2,s=0.005,c='blue')
p.show()
            
