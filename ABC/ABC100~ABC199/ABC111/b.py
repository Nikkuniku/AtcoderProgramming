def check(k):
    return len(set(list(str(k)))) == 1


N = int(input())
ans = 999
for i in range(N, 1000):
    if check(i):
        ans = i
        break
print(ans)
