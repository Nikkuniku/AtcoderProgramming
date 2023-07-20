a, b, c, d = map(int, input().split())
ans = 'No'
if (abs(a-b) <= d and abs(b-c) <= d) or (abs(a-c) <= d):
    ans = 'Yes'
print(ans)
