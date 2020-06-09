import heapq

n,m = map(int,input().split())
prod = list(map(int,input().split()))
prod = list(map(lambda x: x*(-1),prod))

heapq.heapify(prod)

for _ in range(m):
    a = heapq.heappop(prod)*(-1)

    a = a//2

    heapq.heappush(prod,(-1)*a)


ans = list(map(lambda x: (-1)*x,prod))

print(sum(ans))