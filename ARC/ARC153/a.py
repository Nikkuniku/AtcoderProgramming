N = int(input())
ans = []
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        tmp = e+10*f+100*e+1000*d+10000*d+100000*c+1000000*b+10000000*a+100000000*a
                        ans.append(tmp)
ans.sort()
print(ans[N-1])
