from itertools import product
l=list(map(int,input().split()))
l1=[]
for j in range(l[0]):
    l1+=[list(map(int,(input().split())[1:]))]
r=list(map(lambda x:sum([a**2 for a in x])%l[1],product(*l1)))
print(max(r))
