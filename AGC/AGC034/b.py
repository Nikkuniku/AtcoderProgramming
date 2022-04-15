from collections import deque
s = list(input())


def solve1(s):
    n = len(s)
    d = deque()
    ans = 0
    a_cnt = 0
    for i in range(n):
        p = s[i]
        if p == 'A':
            a_cnt += 1
        d.append(p)
        if len(d) >= 3:
            v = d[-3]
            t = d[-2]
            u = d[-1]
            if t == 'A' and u == 'B':
                continue
            elif t == 'A' and u == 'A':
                continue
            elif t != 'A' and u == 'A':
                a_cnt = 1
                continue
            elif v == 'A' and t == 'B' and u == 'C':
                # for j in range(len(d)-3, -1, -1):
                #     if d[j] == 'A':
                #         a_cnt += 1
                #     else:
                #         break
                d.clear()
                ans += a_cnt
                d.append('A')
                # for _ in range(a_cnt):
                #     d.append('A')
                #     ans += 1
            else:
                a_cnt = 0

    return ans


print(solve1(s))
