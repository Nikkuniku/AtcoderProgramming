from collections import Counter
c = list(map(int, input().split()))
C = Counter(c)
v = list(C.values())
v.sort()
if v == [2, 3]:
    print('Yes')
else:
    print('No')
