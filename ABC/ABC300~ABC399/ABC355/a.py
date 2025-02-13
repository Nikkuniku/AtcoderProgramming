A, B = map(int, input().split())
S = set([1, 2, 3])
S.discard(A)
S.discard(B)
ans = -1
if len(S) == 1:
    ans = min(S)
print(ans)
