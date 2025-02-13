A, B = map(int, input().split())
N = 100
forblack = [["."] * N for _ in range(N // 2)]
forwhite = [["#"] * N for _ in range(N // 2)]
A -= 1
B -= 1
for i in range(N // 2):
    for j in range(N):
        if i % 2 == 0 and j % 2 == 0 and B:
            forblack[i][j] = "#"
            B -= 1
        if i % 2 != 0 and j % 2 == 0 and A:
            forwhite[i][j] = "."
            A -= 1
ans = forblack + forwhite
print(N, N)
for c in ans:
    print(*c, sep="")
