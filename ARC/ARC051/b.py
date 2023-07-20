k = int(input())
b = 1
a = 1
for i in range(k-1):
    a, b = b, a+b
print(a, b)
