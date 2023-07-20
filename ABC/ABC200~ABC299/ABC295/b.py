R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if B[i][j] == '.' or B[i][j] == '#':
            continue
        bomb = int(B[i][j])
        for ni in range(R):
            for nj in range(C):
                if abs(ni-i)+abs(nj-j) <= bomb:
                    if B[ni][nj] == '#':
                        B[ni][nj] = '.'
        B[i][j] = '.'
for b in B:
    print(''.join(b))
