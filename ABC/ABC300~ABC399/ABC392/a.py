a, b, c = map(int, input().split())
ans = "No"
if a * b == c or a * c == b or b * c == a:
    ans = "Yes"
print(ans)
