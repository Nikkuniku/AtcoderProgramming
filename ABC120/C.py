s=input()

l=list(s)

zeros = l.count('0')
ones = l.count('1')

if zeros<=ones:
    print(2*zeros)
else:
    print(2*ones)