N = int(input())
H = list(map(int, input().split()))
for i in range(1, N):
    if H[0] < H[i]:
        exit(print(i + 1))
print(-1)
