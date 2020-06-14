tx_a,ty_a ,tx_b , ty_b ,t,v = map(int,input().split())
n=int(input())

takahashi_mae=[tx_a,ty_a]
takahashi_ato=[tx_b,ty_b]


def dist(array1,array2):
    return (((array2[0]-array1[0])**2) + ((array2[1]-array1[1])**2))**0.5

flg = 0
for _ in range(n):
    x,y=map(int,input().split())
    girl = [x,y]
    D = dist(takahashi_mae,girl) + dist(takahashi_ato,girl)

    d_taka = t*v

    if D<=d_taka:
        flg+=1


if flg==0:
    print('NO')
else:
    print('YES')