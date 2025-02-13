N = int(input())
A, B = map(int, input().split())

if A == B:
    if N % (A + 1) == 0:
        print("Aoki")
    else:
        print("Takahashi")
else:
    if N <= min(A, B):
        print("Takahashi")
    else:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
