from collections import deque
n = int(input())
if n == 0:
    print(0)
    exit(0)

d = deque()
while n != 0:
    if n % 2 == 0:
        d.appendleft('0')
    else:
        d.appendleft('1')
        n -= 1
    n //= -2
print(''.join(d))
