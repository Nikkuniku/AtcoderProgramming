from collections import deque

S = deque(list(input()))
ans = "Yes"
if not (S[0] == "<" and S[-1] == ">"):
    ans = "No"
S.popleft()
S.pop()
if ">" in S or "<" in S:
    ans = "No"
print(ans)
