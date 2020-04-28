from collections import Counter

Poors = list(map(int,input().split()))

c = Counter(Poors)

if 1 in list(c.values()) and 2 in list(c.values()):
    print('Yes')
else:
    print('No')