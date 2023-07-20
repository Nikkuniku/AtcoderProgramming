N = int(input())
Box = []
B = [[] for _ in range(6)]
for _ in range(N):
    h, w, d = map(int, input().split())
    B[0].append((h, w, d))
    B[1].append((h, d, w))
    B[2].append((w, h, d))
    B[3].append((w, d, h))
    B[4].append((d, h, w))
    B[5].append((d, w, h))
    Box.append((h, w, d))
for i in range(6):
    B[i].sort(key=lambda x: x[2])
    B[i].sort(key=lambda x: x[1])
    B[i].sort(key=lambda x: x[0])


def binary(K, Arr, j, pl):
    l = pl
    r = len(Arr)
    while r-l > 1:
        mid = (l+r)//2
        if K < Arr[mid][j]:
            l = mid
        else:
            r = mid
    return l


ans = 'No'
for h, w, d in Box:
    for j in range(6):
        L1 = binary(h, B[j], 0, 0)
        L2 = binary(w, B[j], 1, L1-1)
        L3 = binary(d, B[j], 2, L2-1)
        if L3 > N:
            continue
        hn = B[j][L3][0]
        wn = B[j][L3][1]
        dn = B[j][L3][2]
        if h < hn and w < wn and d < dn:
            ans = 'Yes'
            break
print(ans)
