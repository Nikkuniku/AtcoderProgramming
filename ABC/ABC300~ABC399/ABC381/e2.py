N, Q = map(int, input().split())
S = input()
v1, v2, v3 = [], [], []
for i, v in enumerate(S):
    if v == "1":
        v1.append(i)
    elif v == "/":
        v2.append(i)
    elif v == "2":
        v3.append(i)


def solve(m, l, r):
    from bisect import bisect_left, bisect_right

    if m == 0:
        cnt = bisect_right(v2, r) - bisect_left(v2, l)
        return cnt > 0
    # 1がm個あるか調べる
    cnt1 = bisect_left(v1, r) - bisect_left(v1, l)
    if cnt1 < m:
        return False
    j = v1[bisect_left(v1, l) + m - 1]
    # スラッシュ/を見つける
    slash_idx = bisect_left(v2, j)
    if slash_idx == len(v2):
        return False
    k = v2[slash_idx]
    if k > r - 1:
        return False
    # 2がm個あるか調べる
    cnt2 = bisect_right(v3, r) - bisect_left(v3, k)
    return cnt2 >= m


ans = []
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    left = 0
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        if solve(mid, L, R):
            left = mid
        else:
            right = mid
    if left == 0 and not solve(left, L, R):
        ans.append(0)
    else:
        ans.append(2 * left + 1)
print(*ans, sep="\n")
