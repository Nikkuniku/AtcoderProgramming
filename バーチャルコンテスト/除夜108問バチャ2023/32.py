R, C = map(int, input().split())
if R <= 8:
    R = 8-R
else:
    R = R-8
if C <= 8:
    C = 8-C
else:
    C = C-8
ans = 'black'
if max(R, C) % 2 == 0:
    ans = 'white'
print(ans)
