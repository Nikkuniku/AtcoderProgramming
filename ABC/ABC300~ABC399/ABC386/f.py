def isOK(a, b, k):
    if len(a) > len(b):
        a, b = b, a
    M = len(a)
    diff = 0
    for i in range(M):
        j = i + diff
        while i + j < len(b) and a[i] != b[i + j]:
            j += 1
            diff += 1
            if diff > k:
                return False
    return True


K = int(input())
S = input()
T = input()
ans = "No"
if len(S) == len(T):
    if S == T:
        ans = "Yes"
    else:
        diffs = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                diffs += 1
        if diffs <= K:
            ans = "Yes"
elif abs(len(S) - len(T)) <= K:
    for k in range(1, K + 1):
        if isOK(S, T, k):
            ans = "Yes"
print(ans)
