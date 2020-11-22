sx,sy,gx,gy = map(int,input().split())

ans = (sy*gx + gy*sx)/(gy+sy)

print(ans)