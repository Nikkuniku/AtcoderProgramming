a, b = map(int, input().split())
for i in range(1, 999):
    w = (i*(i+1))//2
    e = ((i+1)*(i+2))//2
    if w-a == e-b:
        print(w-a)
        break
