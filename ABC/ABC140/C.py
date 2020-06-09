N=int(input())
B=list(map(int,input().split()))

from collections import deque


A=deque([])

for i in range(N-1):
    B_i = B[i]

    #初回は2つ入れる
    if i==0:
        A.append(B_i)
        A.append(B_i)

    #初回以降
    else:
        if B_i<=pre_B_i:
            A.pop()
            A.append(B_i)
            A.append(B_i)
        else:
            A.append(B_i)

    #前に入れたものの記録
    pre_B_i = B[i]

print(sum(A))