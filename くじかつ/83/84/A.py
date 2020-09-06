n=int(input())
a=list(map(int,input().split()))

e_max = max(a)

p = sum(a)-e_max

if e_max < p:
    print('Yes')
else:
    print('No')