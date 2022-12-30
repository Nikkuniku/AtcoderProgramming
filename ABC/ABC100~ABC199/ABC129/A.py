p,q,r = map(int,input().split())

from itertools import combinations

c = list(combinations([p,q,r],2))

hour =10**18

for i in c:
    hour = min(hour,i[0]+i[1])

print(hour)
    