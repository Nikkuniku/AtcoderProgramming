from collections import deque

N,K = map(int,input().split())
Monsters = list(map(int,input().split()))

d=deque(sorted(Monsters,reverse=True))

for k in range(K):
    if len(d)!=0:
        d.popleft()

print(sum(d))