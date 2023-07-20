N,L=map(int,input().split())
T=[]
A=[0]*N
for i in range(N):
    a=int(input())
    A[i]=a
    T.append((i,a))
T.sort(key=lambda x:x[1],reverse=True)
now=0
for i,a in T:
    if L-(a+now)>0:
        now+=L-(a+now)
print(now)
        