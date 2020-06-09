k = int(input()) 
s = input()

n = len(s)

if n<=k:
    print(s)
else:
    print(s[:(k)]+'...')