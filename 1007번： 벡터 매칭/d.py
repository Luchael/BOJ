import sys,math,itertools
p=sys.stdin.readline
def g(V,v):
 r=[0,0]
 for i in range(len(V)):
  r[0]+=V[i][0]-v[i][0]
  r[1]+=V[i][1]-v[i][1]
 return r
for _ in range(int(p())):
 v=[]
 for N in range(int(p())):
  v.append(list(map(int,p().split())))
 r=math.inf
 C=list(itertools.combinations(v,N//2))
 for i in range(l:=len(C)//2):
  r=min(r,(a:=g(C[i],C[~i]))[0]**2+a[1]**2)
 print(math.sqrt(r))