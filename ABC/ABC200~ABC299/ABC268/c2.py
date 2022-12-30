n = int(input())
p = list(map(int, input().split()))

ans = [0]*n

for i in range(n):
    for j in [-1, 0, 1]:
        ans[(p[i]+j-i) % n] += 1

print(max(ans))
