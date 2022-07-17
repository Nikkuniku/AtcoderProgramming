h, w, c, q = map(int, input().split())
query = []
for _ in range(q):
    query.append(tuple(map(int, input().split())))

query = list(reversed(query))

colored_row = 0
colored_col = 0
colors = [0]*(c+1)
row_operation = set()
col_operation = set()

for p in query:
    t, n, m = p
    if t == 1:
        if n in row_operation:
            continue
        colors[m] += w-colored_col
        row_operation.add(n)
        colored_row += 1
    else:
        if n in col_operation:
            continue
        colors[m] += h-colored_row
        col_operation.add(n)
        colored_col += 1

print(*colors[1:])
