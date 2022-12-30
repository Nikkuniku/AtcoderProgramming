n=int(input())

ans=0
flg=0b000

def rec(num,flg):
    global ans
    if num>n:
        return 0
        
    if num<=n and flg==0b111:
        ans+=1
    
    
    rec(num*10 + 3,flg|0b001)
    rec(num*10 + 5,flg|0b010)
    rec(num*10 + 7,flg|0b100)

rec(0,flg)
print(ans)
