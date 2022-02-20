s=input('Enter string ')
l=''
lm=''
c=0
cm=0
i=0
while(i<=len(s)-1):
      if(s[i] not in l):
            l=l+s[i]
            c+=1
            i+=1
      else:
            i=i-len(l)+l.index(s[i])+1
            if(c>cm):
                  cm=c
                  lm=l
            c=0
            l=''
if(c>cm):
      cm=c
      lm=l
            
print('Length of longest substring in the given line is ',cm)
print('Longest substring is',lm)
