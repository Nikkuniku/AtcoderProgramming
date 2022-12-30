n,k=map(int,input().split())

d={}
for _ in range(n):
    a_i,b_i=map(int,input().split())
    if a_i in d:
        d[a_i]+=b_i
    else:
        d[a_i]=b_i
a=[]
b=[]
d=sorted(d.items(),key=lambda x: x[0])
prev=0
for key,value in d:
    a.append(key)
    b.append(prev+value)
    prev+=value

for j in range(len(b)):
    if k<=b[j]:
        break

print(a[j])
