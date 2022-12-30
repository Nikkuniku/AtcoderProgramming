n=int(input())

ans=[0]
def rec(m,bit):
    if m>n:
        return
    if bit&7==7:
        ans[0]+=1

    rec(10*m+3,bit|1)
    rec(10*m+5,bit|2)
    rec(10*m+7,bit|4)

rec(0,0)

print(ans[0])