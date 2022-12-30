n,k = map(int,input().split())
T = []

for i in range(n):
    T.append(list(map(int,input().split())))

num = [i+1 for i in range(n)]
num.pop(0)

from itertools import permutations

p = list(permutations(num))


ans=0
for c in p:
    cost = 0

    cost+=T[0][c[0]-1]

    for j in range(len(num)-1):

        cost += T[c[j]-1][c[j+1]-1]

    cost+=T[c[-1]-1][0]

    if cost==k:
        ans+=1

print(ans)

