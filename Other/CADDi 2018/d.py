n = int(input())
odd_FLG = False

for _ in range(n):
    a = int(input())
    if a % 2 == 1:
        odd_FLG = True

ans = 'first'
if not odd_FLG:
    ans = 'second'
print(ans)
