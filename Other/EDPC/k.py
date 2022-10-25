n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [False]*(k+1)
for m in range(min(a), k+1):
    Flg = False
    for i in range(n):
        if m-a[i] >= 0:
            if not dp[m-a[i]]:
                Flg = True
                break

    if Flg:
        dp[m] = True

if dp[k]:
    print('First')
else:
    print('Second')
