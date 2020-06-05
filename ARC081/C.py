n=int(input())
a=list(map(int,input().split()))

d={}


for i in range(n):
    if a[i] in d:
        d[a[i]]+=1
    else:
        d[a[i]]=1

can = list(d.items())

edge=[]
for i in range(len(can)):
    if can[i][1]<2:
        continue
    else:
        edge.append(can[i])

if len(edge)==0:
    print(0)
    exit(0)
elif len(edge)==1 and edge[0][1]<4:
    print(0)
    exit(0)
elif len(edge)==1 and edge[0][1]>=4:
    print(edge[0][0]**2)
    exit(0)

edge = sorted(edge,key=lambda x: x[0],reverse=True)

k=len(edge)

s=1
if edge[0][1]>=4:
    print(edge[0][0]**2)
else:
    print(edge[0][0]*edge[1][0])
