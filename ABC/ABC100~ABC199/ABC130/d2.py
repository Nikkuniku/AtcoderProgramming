N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
right = 0
tmp_sum = 0
for left in range(N):
    while right < N and tmp_sum + A[right] < K:
        tmp_sum += A[right]
        right += 1
    ans += N - right
    if right == left:
        right += 1
    else:
        tmp_sum -= A[left]
print(ans)
