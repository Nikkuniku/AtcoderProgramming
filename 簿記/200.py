S = 100000
p = 0.4
YEAR = 5


def calc(a, b, p):
    return (a - b) * p


res = [0]
history = [S]
for i in range(YEAR + 10):
    temp = calc(S, res[-1], p)
    res.append(res[-1] + temp)
    history.append(S - res[-1])
print(res)
print(history)
