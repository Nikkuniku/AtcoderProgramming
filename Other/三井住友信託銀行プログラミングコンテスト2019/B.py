from math import floor
N=int(input())
for x in range(N+1):
    tmp = floor(x*1.08)
    if tmp==N:
        exit(print(x))
else:
    print(':(')