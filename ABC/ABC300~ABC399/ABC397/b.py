S = input()
N = len(S)
ans = 0
i = 0
while i < N:
    if S[i] == "i":
        if i + 1 < N:
            if S[i + 1] == "o":
                i += 1
            else:
                ans += 1
        else:
            ans += 1
    else:
        ans += 1
    i += 1
print(ans)
