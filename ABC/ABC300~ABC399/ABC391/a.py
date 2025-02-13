from collections import defaultdict

mapping = defaultdict(int)
mapping["N"] = "S"
mapping["S"] = "N"
mapping["E"] = "W"
mapping["W"] = "E"
D = input()
ans = []
for d in D:
    ans.append(mapping[d])
print(*ans, sep="")
