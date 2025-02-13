def isParindrome(n):
    digit = []
    while n > 0:
        digit.append(n % 10)
        n //= 10
    for i in range(len(digit)):
        if digit[i] != digit[len(digit) - 1 - i]:
            return False
    return True


N = int(input())
ans = 1
for x in range(1, N):
    if x * x * x > N:
        break
    K = x * x * x
    if isParindrome(K):
        ans = max(ans, K)
print(ans)
