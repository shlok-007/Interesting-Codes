print('Note:- Your code may need run to run maximum of 550*(10^(resolution))*(accuracy) times')
r=int(input('Enter Resolution(recommended=10):- '))
a=int(input('Enter Accuracy(recommended=100):- '))
s=float(input('Enter Dot Size(recommended=1):- '))       #dot_size
import matplotlib.pyplot as p
import pandas as po
import time
def MandelBrotSetPlot(r,a,s):
      print('Plotting has started...')
      start=time.time()
      X=[]
      Y=[]
      Z=[]
      ax=p.axes()
      ax.set_facecolor('darkblue')
      print('It may take about 13 minutes')
      for x in range(-20*r,5*r,1):
           for y in range(-11*r,11*r,1):                            #resolution
                  x1=x/(10*r)
                  y1=y/(10*r)
                  z=complex(x1,y1)
                  z1=z
                  for i in range(a):                                #accuracy
                        z2=z1**2+z
                        m=z2.real**2+z2.imag**2
                        if(m>4):
                              X+=[x1]
                              Y+=[y1]
                              Z+=[i]
                              break
                        elif(i==a-1):
                              p.scatter(x1,y1,s=s,c='black')         #size
                              break
                        z1=z2
      print('Enjoy :D')
      d=po.DataFrame({'x':X,'y':Y,'z':Z})
      p.scatter(d.x,d.y,s=s,c=d.z,cmap="plasma")
      p.title('Mandelbrot Set')
      p.xlabel('Real Number Line')
      p.ylabel('Complex Number Line')
      print('The execution took ',time.time()-start,' seconds')
      p.show()

MandelBrotSetPlot(r,a,s)
