def isOK(a, b):
    if len(a) < len(b):
        a, b = b, a
    M = len(a)
    lefts = -1
    right = M
    for i in range(M):
        if i >= len(b):
            break
        if a[i] == b[i]:
            lefts = i
        else:
            break
    for i in range(M - 1, -1, -1):
        if i - 1 < 0:
            break
        if a[i] == b[i - 1]:
            right = i
        else:
            break
    if right - lefts > 2:
        return False
    return True


K = int(input())
S = input()
T = input()
ans = "No"
if len(S) == len(T):
    if S == T:
        exit(print("Yes"))
    diffs = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diffs += 1
    if diffs == 1:
        exit(print("Yes"))
elif abs(len(S) - len(T)) == 1:
    if isOK(S, T):
        ans = "Yes"
print(ans)
