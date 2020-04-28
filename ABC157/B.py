import sys
import math
# input処理を高速化する
input = sys.stdin.readline

BingoCard = []

for i in range(3):
    a =  list(map(int,input().split()))
    BingoCard.append(a)

N = int(input())

for i in range(N):
    b_i = int(input())

    for j in range(3):
        for k in range(3):
            if BingoCard[j][k] == b_i:
                BingoCard[j][k] =0

#ビンゴかどうか判定
if BingoCard[0] ==[0,0,0]:
    print('Yes')
elif BingoCard[1] ==[0,0,0]:
    print('Yes')
elif BingoCard[2] ==[0,0,0]:
    print('Yes')
elif [n[0] for n in BingoCard] ==[0,0,0]:
    print('Yes')
elif [n[1] for n in BingoCard] ==[0,0,0]:
    print('Yes')
elif [n[2] for n in BingoCard] ==[0,0,0]:
    print('Yes')
elif [BingoCard[n][n] for n in range(3)] ==[0,0,0]:
    print('Yes')
elif [BingoCard[n][2-n] for n in range(3) ] ==[0,0,0]:
    print('Yes')
else:
    print('No')

# print(*BingoCard,sep="\n")