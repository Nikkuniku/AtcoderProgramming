N = int(input())
k = 1
while N > pow(2, k):
    k += 1
people = [[] for _ in range(k)]
for i in range(N):
    j = i + 1
    for m in range(k):
        if j & (1 << m):
            people[m].append(j)
print(k, flush=True)
for m in range(k):
    print(len(people[m]), *people[m], flush=True)
S = input()[::-1]
ans = int(S, 2)
if ans == 0:
    ans = N
print(ans)
