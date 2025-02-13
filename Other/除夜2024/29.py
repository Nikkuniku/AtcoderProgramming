S = input()
T = input()
if S == T:
    exit(print(0))
S += "*" * 100
T += "*" * 100
for i in range(len(S)):
    if S[i] != T[i]:
        exit(print(i + 1))
