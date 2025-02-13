N = int(input())
S = input()
T = input()
alp = [[] for _ in range(26)]
for i, v in enumerate(S):
    alp[ord(v) - 97].append(i)
print(alp)


def check(t, k, cnt, r_ind):
    res = True
    for ti in t:
        pass


l = 0
r = 1 << 60
r_ind = -1
S_cnt = 0
while r - l > 1:
    mid = (l + r) // 2
    if check(T, mid):
        l = mid
    else:
        r = mid
print(l)
