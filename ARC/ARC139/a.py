n = int(input())
t = list(map(int, input().split()))
p = 0
for i in range(n):
    tmp = p >> (t[i])
    tmp += 1
    tmp <<= (t[i])
    tmp |= (1 << t[i])
    p = tmp
print(p)
