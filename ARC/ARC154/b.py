from collections import Counter
N = int(input())
S = input()
T = input()
if Counter(S) != Counter(T):
    print(-1)
    exit()


def judge(s, t):
    i = 0
    j = 0
    while 1:
        if s[i] == t[j]:
            i += 1
        j += 1
        if i == len(s):
            return True
        if j == len(t):
            return False


r = N-1
l = -1
while r-l > 1:
    mid = (l+r)//2
    s = S[mid:]
    if judge(s, T):
        r = mid
    else:
        l = mid
ans = r
print(ans)
