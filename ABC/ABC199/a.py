a,b,c=map(int,input().split())

ans='No'
if pow(a,2)+pow(b,2)<pow(c,2):
    ans='Yes'

print(ans)