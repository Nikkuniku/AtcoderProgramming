n=int(input())
s=input()

from collections import Counter

c=Counter(s)

# ans = 1
# for i in list(c.values()):
#     ans*=i

r=s.count('R')
g=s.count('G')
b=s.count('B')

cnt=0
for i in range(n):
    for j in range(i+1,n):
        k = j+(j-i)
        if k>=n:
            break
        else:
            if s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]:
                cnt+=1

print((r*g*b)-cnt)