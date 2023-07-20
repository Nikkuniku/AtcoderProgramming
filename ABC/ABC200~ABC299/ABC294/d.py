from heapq import heapify, heappop, heappush
N, Q = map(int, input().split())
notCalled = [i for i in range(1, N+1)]
Called = []
heapify(notCalled)
heapify(Called)

ans = []
gone = [False]*(N+1)
for _ in range(Q):
    event = list(map(int, input().split()))
    q = event[0]
    if q == 1:
        p = heappop(notCalled)
        heappush(Called, p)
    elif q == 2:
        x = event[1]
        gone[x] = True
    else:
        while 1:
            p = heappop(Called)
            if not gone[p]:
                ans.append(p)
                heappush(Called, p)
                break
print(*ans, sep="\n")
