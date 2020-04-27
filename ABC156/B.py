N,K = map(int,input().split())

def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)

print(len(base10to(N,K)))