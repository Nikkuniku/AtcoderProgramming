S = input().split('T')
X, Y = map(int, input().split())
yoko = []
tate = []
for i, v in enumerate(S):
    if i % 2 == 0:
        yoko.append(len(v))
    else:
        tate.append(len(v))
if yoko:
    X -= yoko[::-1].pop()
    yoko = yoko[::-1]
    yoko.pop()
    yoko = yoko[::-1]


def f(A, p):
    s = set([0])
    for i in A:
        tmp = set()
        for j in s:
            tmp.add(j+i)
            tmp.add(j-i)
        s, tmp = tmp, s
    return p in s


ans = 'No'
if f(yoko, X) and f(tate, Y):
    ans = 'Yes'
print(ans)
