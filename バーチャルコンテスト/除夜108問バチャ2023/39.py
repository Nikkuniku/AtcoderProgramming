N, A, B = map(int, input().split())
patterna = []
patternb = []
for i in range(N*B):
    if (i//B) % 2 == 0:
        patterna.append('.')
        patternb.append('#')
    else:
        patterna.append('#')
        patternb.append('.')
a = ''.join(patterna)
b = ''.join(patternb)
ans = []
for i in range(N*A):
    if (i//A) % 2 == 0:
        ans.append(a)
    else:
        ans.append(b)
print(*ans, sep="\n")
