n, q = map(int, input().split())
othelo = [0]*n
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    othelo[l] += 1
    if r+1 < n:
        othelo[r+1] -= 1

ans = []
for i in range(1, n):
    othelo[i] += othelo[i-1]
for j in range(n):
    if othelo[j] % 2 == 0:
        ans.append('0')
    else:
        ans.append('1')
print(''.join(ans))
