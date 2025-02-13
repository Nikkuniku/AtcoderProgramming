N = int(input())
c = N % 10
N //= 10
b = N % 10
N //= 10
a = N % 10
ans = [100 * b + 10 * c + a, 100 * c + 10 * a + b]
print(*ans)
