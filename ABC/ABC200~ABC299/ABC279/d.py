from math import floor, ceil
A, B = map(int, input().split())


def f(k):
    return B*k + A/(1+k)**(1/2)


low = -1
high = 1 << 80
cnt = 1000
while cnt:
    c1 = (low * 2 + high) // 3
    c2 = (low + high * 2) // 3

    # //もしf(c2)のほうが良い(小さい)なら、駄目な方lowを更新する
    if f(c1) > f(c2):
        low = c1
    else:
        high = c2
    cnt -= 1

ans = f(low)
print(ans)
