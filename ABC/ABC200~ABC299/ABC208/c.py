n,k=map(int,input().split())
a=list(map(int,input().split()))

p=k//n
k-=n*p

answer=[p]*n
d={}

for i in range(n):
    d[a[i]]=i

b=list(d.items())
b=sorted(b,key=lambda x:x[0])

for c in range(n):
    if k>0:
        answer[b[c][1]]+=1
        k-=1

print(*answer,sep="\n")