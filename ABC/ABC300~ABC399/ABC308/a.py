S = list(map(int, input().split()))
ans = 'Yes'
for s in S:
    if not 100 <= s <= 675:
        ans = 'No'
    if s % 25 != 0:
        ans = 'No'
for i in range(1, len(S)):
    if S[i-1] > S[i]:
        ans = 'No'
print(ans)
