N, R, C = map(int, input().split())
S = input()
T = set()
T.add((R, C))
fx, fy = 0, 0
ans = []
for i, s in enumerate(S):
    if s == "N":
        fx -= 1
        R -= 1
    elif s == "W":
        fy -= 1
        C -= 1
    elif s == "E":
        fy += 1
        C += 1
    else:
        fx += 1
        R += 1
    T.add((R, C))
    if (fx, fy) in T:
        ans.append(1)
    else:
        ans.append(0)
print(*ans, sep="")
