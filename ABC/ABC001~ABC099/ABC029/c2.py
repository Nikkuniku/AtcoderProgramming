n=int(input())

ans=[]
def rec(num):
    if len(num)==n:
        ans.append(num)
        return 

    rec(num+'a')
    rec(num+'b')
    rec(num+'c')

rec('')
print(*ans,sep="\n")