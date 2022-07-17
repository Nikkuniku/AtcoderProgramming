n, k = map(int, input().split())
s = input()

for _ in range(k):
    t = ''
    i = 0
    j = (i+1) % n
    while len(t) < n:
        kekka = set()
        kekka.add(s[i])
        kekka.add(s[j])
        re = ''
        if kekka == set(['R', 'S']):
            re = 'R'
        elif kekka == set(['S', 'P']):
            re = 'S'
        elif kekka == set(['P', 'R']):
            re = 'P'
        else:
            re = min(kekka)
        t += re
        i = (i+2) % n
        j = (j+2) % n
    s = t

ans = s[0]
print(ans)
