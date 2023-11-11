K = int(input())
N = 50
ans = [i for i in range(N)]
for i in range(N):
    ans[i] += K // N
for i in range(K % N):
    for j in range(N):
        if i == j:
            ans[j] += N
        else:
            ans[j] -= 1
print(N)
print(*ans)
