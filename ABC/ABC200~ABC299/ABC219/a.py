X = int(input())
ans = 'expert'
if X < 40:
    ans = 40-X
elif X < 70:
    ans = 70-X
elif X < 90:
    ans = 90-X
print(ans)
