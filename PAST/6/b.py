S = input()
ans = "none"
for i in range(0, len(S), 4):
    temp = [S[i + j] for j in range(4)]
    if "".join(temp) == "post":
        ans = (i // 4) + 1
print(ans)
