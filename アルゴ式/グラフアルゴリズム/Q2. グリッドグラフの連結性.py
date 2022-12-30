H, W = map(int, input().split())
ans = H*W-1 - ((H-1)*W + (W-1)*H)
print(-ans)
