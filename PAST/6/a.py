S = input()
ans = "Yes"
for i in range(8):
    if i == 3:
        if S[i] != "-":
            ans = "No"
    else:
        if S[i] == "-":
            ans = "No"
print(ans)
