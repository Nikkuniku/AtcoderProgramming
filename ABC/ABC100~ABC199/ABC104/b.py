from string import ascii_lowercase

S = list(input())
ans = "AC"
if S[0] != "A":
    ans = "WA"
S.pop(0)
cnt = 0
idx = -1
for i in range(1, len(S) - 1):
    if S[i] == "C":
        cnt += 1
        idx = i
if cnt != 1:
    exit(print("WA"))
S.pop(idx)
for s in S:
    if s not in ascii_lowercase:
        ans = "WA"
print(ans)
