s=input()
d={}
for i in s:
    n=d.get(i,0)
    n+=1
    d[i]=n
l=[]
for k in d:
    l+=[[d[k],-ord(k),k]]
l.sort(reverse=True)
for j in range(3):
    print(l[j][2],l[j][0])
