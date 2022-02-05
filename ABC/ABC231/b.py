n=int(input())
can=[]
for _ in range(n):
    can.append(input())

from collections import Counter

c=Counter(can)

print(c.most_common()[0][0])