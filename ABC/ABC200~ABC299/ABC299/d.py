N = int(input())
L = 1
R = N
while R-L > 1:
    mid = (L+R)//2
    print('?', mid, flush=True)
    i = input()
    if i == '0':
        L = mid
    else:
        R = mid
print('!', L)
