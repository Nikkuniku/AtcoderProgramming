ab, ac, bc = input().split()
ans = -1
if ab == "<":
    if bc == "<":
        ans = "B"
    else:
        if ac == "<":
            ans = "C"
        else:
            ans = "A"
else:
    if bc == "<":
        if ac == "<":
            ans = "A"
        else:
            ans = "C"
    else:
        ans = "B"
print(ans)
