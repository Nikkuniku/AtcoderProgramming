h_1,m_1,h_2,m_2,k = map(int,input().split())

time1 = h_1 * 60 +m_1

time2 = h_2 * 60 +m_2

time_dif = time2 - time1

print(time_dif-k)