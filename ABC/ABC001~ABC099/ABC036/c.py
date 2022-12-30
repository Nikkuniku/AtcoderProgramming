n=int(input())
d={}
ans=[]
for _ in range(n):
    a=int(input())
    d[a]=1
    ans.append(a)

d_order={}
p=sorted(list(d.keys()))
for i in range(len(p)):
    d_order[p[i]]=i

for j in range(n):
    print(d_order[ans[j]])