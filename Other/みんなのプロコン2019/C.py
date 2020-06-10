k,a,b = map(int,input().split())

ans=1
cnt=0
if a>=b-1:
    print(ans+k)
    exit(0)

cnt += (a-ans)
ans += (a-ans)


#まとめてa枚をb枚に交換
n = (k-cnt)//2
ans-= a * n
ans+= b * n
cnt+= 2 * n

#残り回数でビスケットをわる
ans += k-cnt

print(ans)