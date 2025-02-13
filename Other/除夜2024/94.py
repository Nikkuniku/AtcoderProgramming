from collections import Counter

S = "wbwbwwbwbwbw" * 500
W, B = map(int, input().split())
L = W + B
ans = "No"
for i in range(20):
    temp = []
    for j in range(L):
        temp.append(S[i + j])
    C = Counter(temp)
    if C["w"] == W and C["b"] == B:
        ans = "Yes"
        break
print(ans)
