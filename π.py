pi=3
n=2
a=0
while(True):
      s=(-1)**a
      pi+=s*4*(1/(n*(n+1)*(n+2)))
      print('Getting Closer to π :-',pi)
      n+=2
      a+=1
