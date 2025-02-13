from collections import defaultdict

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ng_a = defaultdict(set)
for _ in range(L):
    c, d = map(int, input().split())
    ng_a[c].add(d)
A_ind = sorted([(A[i], i + 1) for i in range(N)])[::-1]
B_ind = sorted([(B[j], j + 1) for j in range(M)])[::-1]
ans = 0
for a, i in A_ind:
    for b, j in B_ind:
        if j in ng_a[i]:
            continue
        ans = max(ans, a + b)
        break
print(ans)
