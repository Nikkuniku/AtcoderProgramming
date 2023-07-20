from bisect import bisect_left as bl
N = int(input())
AC = []
for i in range(N):
    x, y = map(int, input().split())
    if y == 0 or (y < x+1 and len(AC)-bl(AC, i-x) >= y):
        AC.append(i)
print(len(AC))
