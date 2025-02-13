X = list(input())
while X[-1] == "." or X[-1] == "0":
    if X[-1] == ".":
        X.pop()
        break
    else:
        X.pop()

print(*X, sep="")
