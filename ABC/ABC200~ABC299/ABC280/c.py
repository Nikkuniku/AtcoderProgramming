from collections import deque
S = list(input())
T = list(input())
S = deque(S)
T = deque(T)
ans = 0
while S and T:
    if S[0] == T[0]:
        S.popleft()
        T.popleft()
    else:
        break
    ans += 1
print(ans+1)
