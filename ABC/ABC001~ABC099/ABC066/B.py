s=input()
n=len(s)-1

while n>1:
    
    if n%2==0:        
        s=s[:n]

        tmp1=s[:n//2]
        tmp2=s[n//2:]

        if tmp1==tmp2:
            print(n)
            exit(0)
    
    n-=1

