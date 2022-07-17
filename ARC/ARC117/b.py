n = int(input())
a = list(set(map(int, input().split())))
a.sort(reverse=True)
n = len(a)
ans = 1
MOD = 1000000007
for i in range(n):
    if i+1 < n:
        ans *= (a[i]-a[i+1]+1)
    else:
        ans *= (a[i]+1)
    ans %= MOD
print(ans)
