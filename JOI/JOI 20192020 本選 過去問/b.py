from bisect import bisect_right
N, K = map(int, input().split())
S = input()
J, O, I = [], [], []
for i in range(N):
    if S[i] == 'J':
        J.append(i)
    elif S[i] == 'O':
        O.append(i)
    elif S[i] == 'I':
        I.append(i)
M = len(O)
ans = []
for j in range(M-K+1):
    idx_O = O[j]
    idx_O_last = O[j+K-1]
    # Jを見つける
    idx_J = bisect_right(J, idx_O)
    if idx_J < K:
        continue
    P = J[idx_J-K]
    # Iを見つける
    idx_I = bisect_right(I, idx_O_last)
    if len(I)-idx_I < K:
        continue
    Q = I[idx_I+K-1]
    tmp = Q-P-3*K+1
    ans.append(tmp)
print(min(ans) if ans else -1)
