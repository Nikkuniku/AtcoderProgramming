from itertools import permutations, product
n, m = map(int, input().split())
s = [input() for _ in range(n)]
L = 0
for i in range(n):
    L += len(s[i])
T = set(input() for _ in range(m))

p = product([i+1 for i in range(16-L+1)], repeat=n-1)
per = []
for c in p:
    if sum(list(c))+L > 16:
        continue
    per.append(list(c))

p = list(permutations(s))

for c in p:
    for d in per:
        tmp = ''
        if len(d) > 0:
            for j in range(n-1):
                tmp += c[j]
                tmp += '_'*d[j]
            tmp += c[-1]
        else:
            tmp = c[0]
        if tmp not in T and len(tmp) > 2:
            print(tmp)
            exit()
print(-1)
