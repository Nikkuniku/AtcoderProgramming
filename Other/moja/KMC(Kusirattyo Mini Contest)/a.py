N = int(input())
C = [0]*26
L = [list(input()) for _ in range(N)]
for i in range(26):
    tmp = 0
    for s in L:
        if chr(97+i) in s:
            tmp += 1
    C[i] = tmp
print(max(C))
