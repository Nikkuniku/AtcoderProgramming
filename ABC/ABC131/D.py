N=int(input())

works = []

for _ in range(N):
    a,b = map(int,input().split())

    works.append([a,b])

sorted_works = sorted(works,key=lambda x: x[1])


flg = 0
for j in range(N):
    if j==0:
        if sorted_works[j][0]>sorted_works[j][1]:
            flg+=1
    else:
        sorted_works[j][0] += sorted_works[j-1][0]

        if sorted_works[j][0]>sorted_works[j][1]:
            flg+=1


if flg==0:
    print('Yes')
else:
    print('No')