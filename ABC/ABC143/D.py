N=int(input())
Edges = list(map(int,input().split()))

Edges=sorted(Edges)
cnt =0
# for i in c:
#     e1=(i[1] + i[2])
#     e2=(i[0] + i[2])
#     e3=(i[0] + i[1])

#     if i[0] < e1 and i[1] < e2 and i[2] < e3:
#         cnt+=1


import bisect

for a in range(N-2):
    for b in range(a+1,N-1):
        ab = Edges[a] + Edges[b]

        idx = bisect.bisect_left(Edges,ab)

        cnt += max(0,idx-b-1)


print(cnt)