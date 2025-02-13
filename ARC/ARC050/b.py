R, B = map(int, input().split())
x, y = map(int, input().split())
a = R // x
b = B // y
print(a)
print(b)
R -= b
B -= b * y
print(R, B)
