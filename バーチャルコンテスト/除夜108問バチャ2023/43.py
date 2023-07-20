N = int(input())
A = [input() for _ in range(N)]
ans = 'correct'
for i in range(N):
    for j in range(N):
        if A[i][j] == 'W':
            if A[j][i] != 'L':
                ans = 'incorrect'
        elif A[i][j] == 'L':
            if A[j][i] != 'W':
                ans = 'incorrect'
        elif A[i][j] == 'D':
            if A[j][i] != 'D':
                ans = 'incorrect'
print(ans)
