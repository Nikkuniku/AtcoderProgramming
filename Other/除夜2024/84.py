from collections import Counter

N = input()
ans = "No"
C = Counter(N)
if C["1"] == 1 and C["2"] == 2 and C["3"] == 3:
    ans = "Yes"
print(ans)
