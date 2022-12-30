from math import ceil
N = int(input())
M = ceil(N/2)
gr = [[] for _ in range(M)]
s = 0
for i in range(N, N//2, -1):
    gr[s].append(i)
    s += 1
for i in range(N//2):
    gr[M-1-i].append((N//2)-i)
ans = set()
for i in range(M):
    for p in gr[i]:
        for j in range(i+1, M):
            for q in gr[j]:
                ans.add((p, q))

print(len(ans))
for edge in ans:
    print(*edge)
