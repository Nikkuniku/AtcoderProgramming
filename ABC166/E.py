N=int(input())
Agents=list(map(int,input().split()))

# from itertools import combinations

# comb = list(combinations([i for i in range(N)],2))

# cnt=0
# for i in comb:
#     if Agents[i[0]] + Agents[i[1]] == abs(i[0] - i[1]):
#         print(i[0],i[1])
#         cnt+=1

# print(cnt)
cnt=0

for i in range(0,N):
    k=Agents[i]-(i+1)
    if k<i:
        k=i+1
    for j in range(k,N):
        if Agents[i]+Agents[j]==abs(i-j):
            # print(i,j,Agents[i],Agents[j])
            cnt+=1

print(cnt)
