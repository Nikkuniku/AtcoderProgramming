N = int(input())
S = input()
SW = ['S', 'W']


def solve(s1, s2):
    # 0:sheep
    # 1:wolf
    res = [s1, s2]
    for i in range(1, N-1):
        if res[i] == 0:
            if S[i] == 'o':
                res.append(res[i-1])
            else:
                res.append(1 ^ res[i-1])
        else:
            if S[i] == 'o':
                res.append(1 ^ res[i-1])
            else:
                res.append(res[i-1])
    f = False
    if res[-1] == 0:
        if S[-1] == 'o':
            if res[-2] == res[0]:
                f = True
        else:
            if res[-2] != res[0]:
                f = True
    else:
        if S[-1] == 'o':
            if res[-2] != res[0]:
                f = True
        else:
            if res[-2] == res[0]:
                f = True
    g = False
    if res[0] == 0:
        if S[0] == 'o':
            if res[-1] == res[1]:
                g = True
        else:
            if res[-1] != res[1]:
                g = True
    else:
        if S[0] == 'o':
            if res[-1] != res[1]:
                g = True
        else:
            if res[-1] == res[1]:
                g = True
    if f and g:
        return f, ''.join([SW[c] for c in res])
    else:
        return f and g, -1


answer = -1
P = [(0, 0), (0, 1), (1, 0), (1, 1)]
for x, y in P:
    flag, res = solve(x, y)
    if flag:
        answer = res

print(answer)
