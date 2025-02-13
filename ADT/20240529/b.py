S = input()
T = "Monday,Tuesday,Wednesday,Thursday,Friday".split(",")
idx = T.index(S)
ans = 5 - idx
print(ans)
