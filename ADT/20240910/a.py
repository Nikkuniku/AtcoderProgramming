K = int(input())
H = 21 + (K // 60)
M = K % 60
print(str(H) + ":" + str(M).zfill(2))
