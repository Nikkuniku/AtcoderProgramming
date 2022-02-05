from collections import defaultdict
d=defaultdict(lambda:0)
n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    d[a[i]]+=1
p=d[100]
q=d[200]
r=d[300]
s=d[400]

ans= p*s + q*r
print(ans)