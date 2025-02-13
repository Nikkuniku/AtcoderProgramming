N = int(input())
S = [input() for _ in range(N)]
ans = "Yes"
for i in range(N - 2):
    if S[i] == S[i + 1] == "sweet":
        ans = "No"
        break
print(ans)
