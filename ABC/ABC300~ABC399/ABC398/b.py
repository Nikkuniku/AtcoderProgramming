from collections import Counter

A = list(map(int, input().split()))
C = Counter(A)
ans = "No"
P = list(C.values())
for i in range(len(P)):
    for j in range(i + 1, len(P)):
        a = P[i]
        b = P[j]
        if b < a:
            a, b = b, a
        if 2 <= a and 3 <= b:
            ans = "Yes"
print(ans)
