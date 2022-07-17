n, m = map(int, input().split())
s = []
even = 0
odd = 0
for _ in range(n):
    tmp = 0
    t = input()
    for i in range(m):
        if t[i] == '1':
            tmp += 1

    if tmp % 2 == 0:
        even += 1
    else:
        odd += 1

ans = n*(n-1)//2 - even*(even-1)//2 - odd*(odd-1)//2
print(ans)
