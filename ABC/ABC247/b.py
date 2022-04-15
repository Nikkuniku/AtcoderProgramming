from socket import MSG_CTRUNC


n = int(input())
sei = []
mei = []
for _ in range(n):
    a, b = input().split()
    sei.append(a)
    mei.append(b)
ans = 'Yes'
for i in range(n):
    a = sei[i]
    b = mei[i]
    s_cnt = 0
    m_cnt = 0
    for j in range(n):
        if i == j:
            continue
        if a == sei[j]:
            s_cnt += 1
        if a == mei[j]:
            s_cnt += 1
        if b == sei[j]:
            m_cnt += 1
        if b == mei[j]:
            m_cnt += 1
    if s_cnt > 0 and m_cnt > 0:
        ans = 'No'


print(ans)
