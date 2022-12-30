n=int(input())

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
if n==1:
    print(0)
    exit(0)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

a = factorization(n)

# print(a)
n = len(a)

cnt =0
for i in range(n):
    k = a[i][1]

    fr=1
    cnt+=1
    for j in range(2,k+1):
        fr+=j
        if k-fr>=0:
            cnt+=1

print(cnt)
