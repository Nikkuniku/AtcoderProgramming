n = int(input())
a = list(map(int, input().split()))
csum = [0]
for i in range(n):
    csum.append(csum[-1]+a[i])
for i in range(n):
    csum[i+1] += csum[i]
cmax = [0]
m = 0
for i in range(n):
    if a[i] > m:
        m = a[i]
    cmax.append(m)

for i in range(1, n+1):
    ans = csum[i]+i*cmax[i]
    print(ans)
