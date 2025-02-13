S = input()
N = int(S[-3:])
T = set([i + 1 for i in range(349)])
T.discard(316)
ans = "No"
if N in T:
    ans = "Yes"
print(ans)
