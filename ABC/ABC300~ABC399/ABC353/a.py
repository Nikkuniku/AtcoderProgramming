N = int(input())
H = list(map(int, input().split()))
p = H[0]
ans = -1
for i in range(1, N):
    if H[i] > p:
        ans = i + 1
        break
print(ans)
