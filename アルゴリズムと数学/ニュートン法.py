a=float(input())
k=1000
def bibun(x):
    return 10*(x**9)

def y(x):
    return x**10

def seppen(x):
    return y(x)-bibun(x)*x

for _ in range(100):
    b=seppen(a)
    x=(k-b)/bibun(a)
    print(x)
    a=x

print('実際の値')
print(10**(0.3))