s=list(input())

from collections import Counter

c = dict(Counter(s))

if len(c)==2:
    print('Yes')
else:
    print('No')