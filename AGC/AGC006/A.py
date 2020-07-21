n=int(input())
s=input()
t=list(input())

import re 


ans=s

k=-1
for i in range(n):
    tmp=''.join(t[:i+1])

    if tmp in ans:
        k=i

if k<n-1:
    ans+=''.join(t[k+1:])

print(len(ans))
