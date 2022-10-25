n, k = map(int, input().split())
a = list(map(int, input().split()))
for p in range(k):
    tmp = [0]*(n+1)
    for j in range(n):
        d = a[j]
        tmp[max(j-d, 0)] += 1
        tmp[min(j+d+1, n)] -= 1
    for j in range(n):
        tmp[j+1] += tmp[j]
    if tmp == a:
        break
    a = tmp
a.pop()
print(*a)
