N,M,Q=map(int,input().split())

from itertools import combinations_with_replacement
A=[0]*N
conditions = []

for i in range(Q):
    con =list(map(int,input().split()))
    conditions.append(con)

c = combinations_with_replacement(range(1,M+1),N)

total =0
for seq in c:
    total_tmp=0
    for q in conditions:
        if seq[q[1]-1] - seq[q[0]-1] == q[2]:
            total_tmp += q[3]

    total = max(total,total_tmp )

print(total)

