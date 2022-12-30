x=int(input())

cnt = x//500

x-=cnt*500

print(5*(x//5) + 1000*cnt)