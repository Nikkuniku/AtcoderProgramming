n,q =map(int,input().split())
s = input()

d= {}

for k in range(n):
    d[k]=0

total = 0
for j in range(n-1):
    if s[j]=='A' and s[j+1]=='C':
        total+=1
        d[j+1]+=total
    else:
        d[j+1]=total
        
# print(d)

ans = []
for _ in range(q):
    l,r = map(int,input().split())

    ans.append(d[r-1] -d[l-1])


for i in ans:
    print(i)