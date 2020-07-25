n=int(input())
gr=[]

Xb=[]
Yb=[]
for _ in range(n):
    x,y,p=map(int,input().split())
    gr.append([x,y,p])
    Xb.append(x)
    Yb.append(y)

Xb=list(set(Xb))
Yb=list(set(Yb))
m=len(Xb)+len(Yb)

from itertools import product
pr=list(product([0,1],repeat=m))

comb=[]
for k in range(n+1):
    arr=[ j for j in pr if sum(j)==k]
    comb.append(arr)

print(comb)
for k in range(n+1):
    pate=comb[k]
    ans=10**9
    for c in pate:
        tmp=0
        for i in range(len(Xb)):
            if c[i]==1:
                X=Xb[i]
                



    

