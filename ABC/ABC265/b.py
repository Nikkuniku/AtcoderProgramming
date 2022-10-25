n, m, t = map(int, input().split())
a = list(map(int, input().split()))
bonus = [0]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    bonus[x-1] += y

i = 0
while t > 0:
    t += bonus[i]
    t -= a[i]
    if t <= 0:
        break
    i += 1
    if i == n-1:
        print('Yes')
        exit()
print('No')
