from collections import defaultdict
s = input()
columns = [[7], [4], [2, 8], [1, 5], [3, 9], [6], [10]]
d = defaultdict(int)
for i, v in enumerate(s):
    d[i+1] = v
ans = 'No'
if d[1] == '1':
    print(ans)
    exit()

for i in range(7):
    for j in range(i+2, 7):
        left = 0
        right = 0
        for p in columns[i]:
            if d[p] == '1':
                left += 1
        for q in columns[j]:
            if d[q] == '1':
                right += 1

        for k in range(i+1, j):
            tmp = 0
            for p in columns[k]:
                if d[p] == '0':
                    tmp += 1

            if left > 0 and right > 0:
                if tmp == len(columns[k]):
                    ans = 'Yes'
                    print(ans)
                    exit()
print(ans)
