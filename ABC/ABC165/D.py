import math

A,B,N=map(int,input().split())

def floor_t(A,B,y):
    return math.floor(A*y/B) - A*math.floor(y/B)

#関数の挙動を調べる
# for x in range(1,10*B+1):
#     print('x={} : floor(AX/B)={}'.format(x,math.floor(A*x/B)))

# for x in range(1,10*B+1):
#     print('x={} : floor(X/B)={}'.format(x,A*math.floor(x/B)))

# for i in range(1,10*B+1):
#     print('x={}:f(x)={}'.format(i,floor_t(A,B,i)))

X=min(N,B-1)

print(floor_t(A,B,X))