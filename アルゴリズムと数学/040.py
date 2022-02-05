n = int(input())
a = list(map(int, input().split()))
csum = [0]
for i in range(n-1):
    csum.append(csum[-1]+a[i])
m = int(input())
now = 0
ans = 0
for j in range(m):
    b = int(input())-1
    if j != 0:
        distance = abs(csum[b]-csum[now])
        ans += distance

    now = b

print(ans)
