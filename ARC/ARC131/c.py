n = int(input())
a = list(map(int, input().split()))
g = 0
b = []
for i in range(n):
    g ^= a[i]
    b.append(format(a[i], '08b'))
ans = 'Lose'
for j in range(n):
    if g ^ a[j] == 0:
        ans = 'Win'
        break
print(ans)
k = 10
cnt = [0]*k
for p in a:
    for j in range(k):
        if p & (1 << j):
            cnt[j] += 1

print(*b, sep="\n")
print(cnt)
