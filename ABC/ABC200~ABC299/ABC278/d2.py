from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
add_index = set()
adds = defaultdict(int)
init = -1
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        while add_index:
            s = add_index.pop()
            adds[s] = 0
        init = query[1]
    elif q == 2:
        add_index.add(query[1])
        adds[query[1]] += query[2]
    else:
        if init == -1:
            base = A[query[1]-1]
        else:
            base = init
        res = base + adds[query[1]]
        ans.append(res)
print(*ans, sep="\n")
