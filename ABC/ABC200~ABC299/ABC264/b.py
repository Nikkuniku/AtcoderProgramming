grid = []
grid.append('000000000000000')
grid.append('011111111111110')
grid.append('010000000000010')
grid.append('010111111111010')
grid.append('010100000001010')
grid.append('010101111101010')
grid.append('010101000101010')
grid.append('010101010101010')
grid.append('010101000101010')
grid.append('010101111101010')
grid.append('010100000001010')
grid.append('010111111111010')
grid.append('010000000000010')
grid.append('011111111111110')
grid.append('000000000000000')
r, c = map(int, input().split())

r -= 1
c -= 1
if grid[r][c] == '0':
    print('black')
else:
    print('white')
