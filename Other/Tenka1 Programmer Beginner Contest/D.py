N = int(input())
isOK = False
for p in range(N+2):
    if N == p*(p-1)//2:
        isOK = True
        break
if not isOK:
    print('No')
    exit()

ans = [[] for _ in range(p)]
k = 0
for i in range(p):
    for j in range(i+1, p):
        k += 1
        ans[i].append(k)
        ans[j].append(k)

print('Yes')
print(p)
for c in ans:
    print(len(c), *c)
