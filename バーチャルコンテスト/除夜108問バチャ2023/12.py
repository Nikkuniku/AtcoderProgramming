K = int(input())
hh = 21
mm = 00
hh += K//60
mm += K % 60

print(str(hh)+':'+str(mm).zfill(2))
