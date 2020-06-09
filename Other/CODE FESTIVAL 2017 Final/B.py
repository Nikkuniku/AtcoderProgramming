s=input()

n=len(s)

from collections import Counter

c =dict(Counter(s))

under_value = 10**18

for _,Value in c.items():
    under_value = min(under_value,Value)

for key,_ in c.items():
    c[key]-=under_value

print(c)


