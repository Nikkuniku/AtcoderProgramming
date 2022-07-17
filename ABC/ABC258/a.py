k = int(input())
h = 21 + (k//60)
k %= 60
print(str(h)+':'+str(k).zfill(2))
