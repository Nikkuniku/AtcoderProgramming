N,K,M =map(int,input().split())
Tests = list(map(int,input().split()))

effort = N*M - sum(Tests)

if effort> K:
    print('-1')
else:
    if effort<0:
        print(0)
    else:
        print(effort)