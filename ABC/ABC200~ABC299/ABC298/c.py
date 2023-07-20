from heapq import heapify, heappop, heappush
N = int(input())
Q = int(input())
box = [[] for _ in range(200005)]
num = [[] for _ in range(200005)]
for i in range(N+1):
    heapify(box[i])
    heapify(num[i])

ans = []
ans_num = []
for _ in range(Q):
    query = list(map(int, input().split()))
    m = query[0]
    if m == 1:
        i, j = query[1:]
        heappush(box[j], i)
        heappush(num[i], j)
    elif m == 2:
        i = query[1]
        while box[i]:
            v = heappop(box[i])
            ans.append(v)
        print(*ans)
        while ans:
            v = ans.pop()
            heappush(box[i], v)
    else:
        i = query[1]
        while num[i]:
            v = heappop(num[i])
            ans_num.append(v)
        ans_num = list(set(ans_num))
        print(*ans_num)
        while ans_num:
            v = ans_num.pop()
            heappush(num[i], v)
