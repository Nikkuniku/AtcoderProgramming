from math import sqrt

N = int(input())
for x in range(1, N):
    y = str(int(sqrt(x)))
    x_str = str(x)
    if x_str.startswith(y):
        print(x, y)


def solve(N):
    res = 0
    s = 99
