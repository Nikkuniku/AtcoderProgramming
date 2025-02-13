S = input()
T = input()
ans = len(T)
for i in range(len(S)):
    s, t = S[i], T[i]
    if s != t:
        ans = i + 1
        break
print(ans)
