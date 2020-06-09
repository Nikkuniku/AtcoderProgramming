x,y,r=map(int,input().split())
x2,y2,x3,y3 = map(int,input().split())

#表方形の対角線の長さ÷2
r_len = (( (x3-x2)**2 + (y3-y2)**2 )**0.5)/2
#円の半径 
c_len = r

#長辺
r_long = max(x3-x2,y3-y2)
#短辺
r_short = min(x3-x2,y3-y2)
#長方形の座標
c_rect = [(x2+x3)/2 , (y2+y3)/2]

#円の中心と長方形の中心間の距離
dist = ( ( x - c_rect[0]) **2 + (y - c_rect[1]) **2 )**0.5

def d(array):
    return ( ( x - array[0]) **2 + (y - array[1]) **2 )**0.5


# #長方形と円が接しているかの判定
# if dist>r+r_short:
#     print('YES')
#     print('YES')
#     exit(0)

#円が長方形の内部にあるかの判定
if abs(c_rect[0]-x) + r <=(x3-x2)/2 and abs(c_rect[1]-y)  + r <= (y3-y2)/2:
    print('NO')
    print('YES')
    exit(0)

#長方形が円の内部にあるかの判定
if dist<=r:
    l1 = [x2,y3]
    l2 = [x2,y2]
    r1 = [x3,y3]
    r2 = [x3,y2]
    if d(l1)<=r and d(l2)<= r and d(r1)<=r and d(r2) <=r:
        print('YES')
        print('NO') 
        exit(0)



print('YES')
print('YES')