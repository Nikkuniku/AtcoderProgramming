a, b = input().split()
ans = "H"
if a == "H":
    if b == "D":
        ans = "D"
else:
    if b == "H":
        ans = "D"
print(ans)
