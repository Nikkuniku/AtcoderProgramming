S = input()
T = input()
ones = "AB,BC,CD,DE,AE".split(",")
S = "".join(sorted([S[i] for i in range(2)]))
T = "".join(sorted([T[i] for i in range(2)]))
ans = "No"
if (S in ones and T in ones) or (S not in ones and T not in ones):
    ans = "Yes"
print(ans)
