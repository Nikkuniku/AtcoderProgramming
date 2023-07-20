N = input()
ans = 'No'
tmp = 0
for i in range(len(N)):
    tmp += int(N[i])
    tmp %= 9
if tmp == 0:
    ans = 'Yes'
print(ans)
