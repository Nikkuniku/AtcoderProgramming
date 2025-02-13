X = int(input())
ans = 1
for i in range(1, X + 1):
    if i**4 == X:
        ans = i
        break
print(ans)
