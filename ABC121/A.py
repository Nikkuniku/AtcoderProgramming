H,W = map(int,input().split())
h,w = map(int,input().split())

a = h*W
b = H*w
c = h*w

print(H*W - (a+b-c))