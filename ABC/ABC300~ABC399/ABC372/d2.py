N = int(input())
H = list(map(int, input().split()))
ans = [0] * N
stc = []
for i in range(N - 2, -1, -1):
    while stc and H[i + 1] > H[stc[-1]]:
        stc.pop()
    stc.append(i + 1)
    ans[i] = len(stc)
print(*ans)
