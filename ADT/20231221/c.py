S = input()
Bs = []
Rs = []
K = -1
for i, v in enumerate(S):
    if v == "B":
        Bs.append(i)
    if v == "R":
        Rs.append(i)
    if v == "K":
        K = i
ans = "Yes"
if Bs[0] % 2 == Bs[1] % 2:
    ans = "No"
if not (Rs[0] < K < Rs[1]):
    ans = "No"
print(ans)
