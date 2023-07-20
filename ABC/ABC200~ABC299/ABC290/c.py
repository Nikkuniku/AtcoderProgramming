N, K = map(int, input().split())
A = set(list(map(int, input().split())))
ans = 0
cnt = 0
for x in range(N+1):
    if cnt <= K:
        if x in A:
            cnt += 1
            ans = max(ans, x)
        else:
            ans = max(ans, x)
            break
    else:
        break

print(ans)
