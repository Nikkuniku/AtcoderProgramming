a, b, c = map(int, input().split())
ans = 'No'
if 4*a*b < (c-a-b)**2 and c-a-b > 0:
    ans = 'Yes'
print(ans)
