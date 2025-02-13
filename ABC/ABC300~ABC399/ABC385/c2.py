N = int(input())
H = list(map(int, input().split()))
ans = 1
for i in range(N):
    h = H[i]
    for l in range(1, N):
        cnt = 1
        j = i + l
        while j < N:
            if H[j] == h:
                cnt += 1
                j += l
            else:
                break
        ans = max(ans, cnt)
print(ans)
