N,K = map(int,input().split())
Dices = list(map(int,input().split()))

Dices = list(map(lambda n:(n+1)/2,Dices))
import numpy as np 
Dices = np.cumsum(Dices)
# from collections import deque

# d=deque([])
# total= 0
# for i in range(N):
#     d.append((Dices[i]+1)/2)
#     if len(d)==K:
#         total = max(total,sum(d))
#         d.popleft()

# print(total)

#累積和
S=np.append(0,Dices)
total = 0
# for i in range(N+1):
#     S[i] = sum(Dices[:i])

for j in range(N-K+1):
    total = max(total,S[j+K]-S[j])

print(total)