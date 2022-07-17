from collections import deque
n = int(input())
t = deque(input())

ans = pow(10, 10)
if n == 1:
    if t[0] == '1':
        ans *= 2
    print(ans)
    exit(0)

if t[0] == '1' and t[1] == '0':
    t.appendleft('1')
elif t[0] == '0' and t[1] == '1':
    t.appendleft('1')
    t.appendleft('1')
elif t[0] == '1' and t[1] == '1':
    pass
else:
    ans = 0
    print(ans)
    exit(0)

if t[-2] == '1' and t[-1] == '0':
    pass
elif t[-2] == '0' and t[-1] == '1':
    t.append('1')
    t.append('0')
elif t[-2] == '1' and t[-1] == '1':
    t.append('0')
else:
    ans = 0
    print(ans)
    exit(0)
n = len(t)
k = ''.join(t).count('110')
if n == 3*k:
    ans = pow(10, 10)-k+1
else:
    ans = 0
print(ans)
