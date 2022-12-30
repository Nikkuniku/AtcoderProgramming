from collections import Counter

N=int(input())
int_s = list(map(int,input().split()))

c=Counter(int_s)

product =1
for i in list(c.values()):
    product*=i

if product==1:
    print('YES')
else:
    print('NO')