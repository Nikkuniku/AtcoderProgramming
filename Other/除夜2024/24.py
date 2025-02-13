from collections import Counter

S = input()
C = Counter(S)
m = C.most_common()[1][0]
for i in range(len(S)):
    if S[i] == m:
        print(i + 1)
        break
