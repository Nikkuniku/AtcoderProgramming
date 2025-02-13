N = int(input())
S = [input() for _ in range(N)]
ans = "Yes"
for i in range(N - 1):
    if i < N - 2 and S[i] == "sweet" and S[i + 1] == "sweet":
        ans = "No"
print(ans)
