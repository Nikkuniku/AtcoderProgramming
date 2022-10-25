n = int(input())
a = list(map(int, input().split()))

ans = 0
csum = [0]
for i in range(n):
    csum.append(csum[-1]+a[i])
    ans += (n-1)*(a[i]**2)

for i in range(n):
    ans -= 2*(a[i]*(csum[-1]-csum[i+1]))

print(ans)
