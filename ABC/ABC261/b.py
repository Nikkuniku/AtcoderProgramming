n = int(input())
a = [list(input())for _ in range(n)]

ans = 'correct'
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if a[i][j] == 'W':
            if a[j][i] != 'L':
                ans = 'incorrect'
                break
        if a[i][j] == 'D':
            if a[j][i] != 'D':
                ans = 'incorrect'
                break
        if a[i][j] == 'L':
            if a[j][i] != 'W':
                ans = 'incorrect'
                break

print(ans)
