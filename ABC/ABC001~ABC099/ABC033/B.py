n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

d={}

for i in a:
    d[i]=1

for j in b:
    if j in d:
        d[j]+=1
    else:
        d[j]=1

num=0
deno=0

for k,v in d.items():
    if v>1:
        num+=1
    deno+=1

print(num/deno)