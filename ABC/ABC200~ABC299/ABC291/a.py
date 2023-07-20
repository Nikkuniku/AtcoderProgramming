S = input()
ans = -1
for i in range(len(S)):
    if S[i] == S[i].upper():
        ans = i+1
print(ans)
