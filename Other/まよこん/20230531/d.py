X = input()
res = [0]
for i in range(len(X)):
    p = int(X[i])+res[-1]
    res.append(p)
res = res[::-1]
for i in range(len(res)-1):
    Y = res[i]
    res[i] = Y % 10
    res[i+1] += Y//10
if res[-1] == 0:
    res.pop()
res = res[::-1]
ans = [str(res[i]) for i in range(len(res))]
print(''.join(ans))
