K = int(input())
hh = 21 + (K // 60)
mm = K % 60
hh = str(hh).zfill(2)
mm = str(mm).zfill(2)
print(hh + ":" + mm)
