s = input()
n = len(s)
ans = 'No'
if n == 1:
    ans = s*6
elif n == 2:
    ans = s*3
else:
    ans = s*2
print(ans)
