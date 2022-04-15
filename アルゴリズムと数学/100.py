import decimal 
q=int(input())

def mat_mul(a, b) :
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
    return c

def pow_mat(A, n):
    p = [[0]*len(A) for _ in range(len(A))]

    # 基本行列にする
    for i in range(len(A)):
        p[i][i] = 1

    while n > 0:
        if n & 1:
            p = mat_mul(A, p)
        A = mat_mul(A, A)
        n >>= 1
    return p


for _ in range(q):
    X,Y,Z,T=map(decimal.Decimal,input().split())
    T=int(T)
    M=[[1-X,Y,0],[0,1-Y,Z],[X,0,1-Z]]
    M=pow_mat(M,T)
    a=sum(M[0])
    b=sum(M[1])
    c=sum(M[2])
    print(a,b,c)