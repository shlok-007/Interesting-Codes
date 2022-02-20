first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

def MatrixScr(a,r,c):
      s=''
      for i in range(0,c):
            for j in range(0,r):
                  t=a[j][i]
                  s+=t
      def mat(s,n):
            t=''
            q=''
            while(n<len(s) and s[n].isalnum()):
                  t+=s[n]
                  n+=1
            while(n<len(s) and not s[n].isalnum()):
                  q+=s[n]
                  n+=1
            t+=' '
            return t,n,q
      e=''
      n=0
      q=''
      while(n<len(s)):
            t=mat(s,n)
            n=t[1]
            e+=t[0]
            while(e==' '):
                  q+=t[2]
                  break
      while(e.strip()==''):
            print(q)
            break
      try:
            while(not e.strip()==''):
                  print(q+e.strip()+t[2])
                  break
      except:
            while(not e.strip()==''):
                  print(q+e.strip())
                  break

MatrixScr(matrix,n,m)
