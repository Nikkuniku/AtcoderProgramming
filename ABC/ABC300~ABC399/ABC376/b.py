N, Q = map(int, input().split())
L, R = 0, 1
ans = 0
for i in range(Q):
    H, T = input().split()
    T = int(T) - 1
    tmp = []
    migi = 0
    hidari = 0
    if H == "R":
        r_migi = R
        r_hidari = R
        while r_migi != T:
            r_migi += 1
            r_migi %= N
            if r_migi == L:
                tmp.append(1e18)
                break
            migi += 1
        if r_migi == T:
            tmp.append(migi)
        while r_hidari != T:
            r_hidari -= 1
            r_hidari %= N
            if r_hidari == L:
                tmp.append(1e18)
                break
            hidari += 1
        if r_hidari == T:
            tmp.append(hidari)
        R = T
    elif H == "L":
        l_migi = L
        l_hidari = L
        while l_migi != T:
            l_migi += 1
            l_migi %= N
            if l_migi == R:
                tmp.append(1e18)
                break
            migi += 1
        if l_migi == T:
            tmp.append(migi)
        while l_hidari != T:
            l_hidari -= 1
            l_hidari %= N
            if l_hidari == R:
                tmp.append(1e18)
                break
            hidari += 1
        if l_hidari == T:
            tmp.append(hidari)
        L = T
    ans += min(tmp)
print(ans)
