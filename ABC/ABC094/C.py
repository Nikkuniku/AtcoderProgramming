n= int(input())
x = list(map(int,input().split()))

y = sorted(x)

from bisect import bisect_left
border=n//2-1

if n==2:
    print(x[1])
    print(x[0])
    exit(0)


for i in range(n):
    index = bisect_left(y,x[i])

    if index<=border:
        print(y[border+1])
    else:
        print(y[border])
