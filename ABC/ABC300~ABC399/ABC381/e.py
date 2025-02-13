from atcoder.segtree import SegTree

N, Q = map(int, input().split())
S = input()
cum1 = []
cum2 = [0] * N
for i in range(N):
    if i == 0:
        if S[i] == "1":
            cum1.append(1)
        else:
            cum1.append(0)
    else:
        cum1.append(cum1[-1] + (1 if S[i] == "1" else 0))
for i in range(N - 1, -1, -1):
    if i == N - 1:
        if S[i] == "2":
            cum2[i] = 1
    else:
        cum2[i] = cum2[i + 1] + (1 if S[i] == "2" else 0)
cnt = [0] * N
for i in range(N):
    if S[i] == "/" and 0 <= i < N - 1:
        cnt[i] = min(cum1[i - 1], cum2[i + 1])
print(cum1)
print(cum2)
print(cnt)
Seg = SegTree(max, 0, cnt)
ans = []
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    temp = Seg.prod(L, R)
    j = Seg.max_right(R, lambda p: p >= temp)
    if L > 0:
        cnt1 = cum1[L - 1]
    else:
        cnt1 = 0
    if R < N - 1:
        cnt2 = cum2[R + 1]
    else:
        cnt2 = 0
    if temp > 0:
        temp = temp * 2 + 1
        temp -= 2 * max(cnt1, cnt2)
    ans.append(temp)
print(*ans, sep="\n")
