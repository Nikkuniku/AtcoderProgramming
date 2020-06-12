n=int(input())
s=input()

from collections import deque
w=[0]*n
for i in range(1,n):
    if s[i-1]=='W':
        w[i]=w[i-1]+1
    else:
        w[i]=w[i-1]
e=[0]*n

for j in range(n-2,-1,-1):
    if s[j+1]=='E':
        e[j]=e[j+1]+1
    else:
        e[j]=e[j+1]

ans=10**9

for k in range(n):
    ans =min(ans,e[k]+w[k])

print(ans)