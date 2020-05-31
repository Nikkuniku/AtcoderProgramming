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

n = len(a)

arr1=[1,2]
arr2=[3,4,5]
arr3=[6,7,8,9]
arr4=[10,11,12,13]
arr5=[14,15,16,17,18]
arr6=[19,20,21,22,23,24]
arr7=[25,26,27,28,29,30,31]
arr8=[32,33,34,35,36,37,38,39]
arr8=[40,41,42,43,44,45,46,47,48]
arr9=[49,50,51,52,53,54,55,56,57,58]
arr10=[59,60,61,62,63,64,65,66,67,68,69]


cnt =0
for i in range(n):
    if a[i][1] in arr1:
        cnt+=1
    elif a[i][1] in arr2:
        cnt+=2
    elif a[i][1] in arr3:
        cnt+=3
    elif a[i][1] in arr4:
        cnt+=4
    elif a[i][1] in arr5:
        cnt+=5
    elif a[i][1] in arr6:
        cnt+=6
    elif a[i][1] in arr7:
        cnt+=7
    elif a[i][1] in arr8:
        cnt+=8
    elif a[i][1] in arr9:
        cnt+=9
    elif a[i][1] in arr10:
        cnt+=10
print(cnt)
