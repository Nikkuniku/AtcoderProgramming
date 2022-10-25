n = int(input())
a = list(map(int, input().split()))

cnt = 0
a = a+a
dp = [0]*(2*n)
feed = [False]*(2*n)

for i in range(1, n+1):
    if feed[i]:
        continue
    else:
        if a[i-1] <= a[i]:
            dp[i] = a[i-1]
            if not feed[i-1]:
                feed[i-1] = True
                cnt += 1
            if not feed[i]:
                feed[i] = True
                cnt += 1
        else:
            dp[i] = a[i]
            if not feed[i]:
                feed[i] = True
                cnt += 1
            if not feed[i+1]:
                feed[i+1] = True
                cnt += 1

    if cnt == n:
        break

ans = sum(dp)
print(ans)
