N = input()
M = len(N)
S = 0
modulo = [0, 0, 0]
for i in range(M):
    S += int(N[i]) % 3
    S %= 3
    modulo[int(N[i]) % 3] += 1
if S == 0:
    print(0)
elif S == 1:
    if 0 < modulo[1] < M:
        print(1)
    elif 1 < modulo[2] < M:
        print(2)
    else:
        print(-1)
else:
    if 0 < modulo[2] < M:
        print(1)
    elif 1 < modulo[1] < M:
        print(2)
    else:
        print(-1)
