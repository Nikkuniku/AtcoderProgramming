def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


N = int(input())
X = input()
F = [0]*200000
for i in range(1, 200000):
    p = i % popcount(i)
    cnt = 1
    if p != 0:
        p = p % popcount(p)
        cnt += 1
    F[i] = cnt
m = X.count('1')
ans = []
if m > 1:
    zerotoone = [pow(2, i, m+1) for i in range(N)][::-1]
    onetozero = [pow(2, i, m-1) for i in range(N)][::-1]
    A, B = 0, 0
    for i in range(N):
        A += int(X[i])*pow(2, N-1-i, m+1)
        B += int(X[i])*pow(2, N-1-i, m-1)
    for i in range(N):
        tmp = 0
        cnt = 1
        if X[i] == '0':
            tmp = (A+zerotoone[i]) % (m+1)
        else:
            tmp = (B-onetozero[i]) % (m-1)
        while tmp != 0:
            tmp = tmp % popcount(tmp)
            cnt += 1
        ans.append(cnt)
else:
    if X == '0':
        ans.append(1)
    else:
        A = 0
        for i in range(N):
            A += int(X[i])*pow(2, N-1-i, 2)
        for i in range(N):
            tmp = 0
            cnt = 0
            if X[i] == '0':
                tmp = (A+pow(2, N-1-i, 2)) % 2
                cnt += 1
            while tmp != 0:
                tmp = tmp % popcount(tmp)
                cnt += 1
            ans.append(cnt)
print(*ans, sep="\n")
