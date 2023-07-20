def summation(x):
    return x*(x+1)//2


N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += summation(b)-summation(a-1)
print(ans)
