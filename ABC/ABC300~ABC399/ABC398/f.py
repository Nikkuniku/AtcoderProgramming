# 偶数長含めた回文の長さを求める
# R[2*i] = L: S[i]を中心とする奇数長の最大回文
# R[2*i+1] = L: S[i:i+2]を中心とする偶数長の最大回文
# ダミー文字を挟むが、各 R[i] は実際の回文の文字列長と一致する
def manacher(S):
    C = []
    for a in S:
        C.append(a)
        C.append(0)
    C.pop()

    L = len(C)

    R = [0] * L

    i = j = 0
    while i < L:
        while j <= i < L - j and C[i - j] == C[i + j]:
            j += 1
        R[i] = j
        k = 1
        while j - R[i - k] > k <= i < L - k:
            R[i + k] = R[i - k]
            k += 1
        i += k
        j -= k

    for i in range(L):
        if i & 1 == R[i] & 1:
            R[i] -= 1
    return R


S = input()
N = len(S)
T = []
M = manacher(S)
l, r = 1 << 60, -1
# 奇数長
for i in range(N):
    if i + (M[2 * i] - 1) // 2 == N - 1:
        l = min(l, i - (M[2 * i] - 1) // 2)
        r = max(r, i + (M[2 * i] - 1) // 2)
# 偶数長
for i in range(N - 1):
    if i + M[2 * i + 1] // 2 == N - 1:
        l = min(l, i + 1 - (M[2 * i + 1]) // 2)
        r = max(r, i + (M[2 * i + 1]) // 2)
ans = list(S)
rev = []
for i in range(N):
    if l <= i <= r:
        continue
    rev.append(S[i])
while rev:
    ans.append(rev.pop())
print(*ans, sep="")
