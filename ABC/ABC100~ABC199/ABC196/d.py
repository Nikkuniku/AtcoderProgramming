h, w, A, b = map(int, input().split())
perttern = set()


def dfs(s, arr):
    arr.append(s)
    visit[s] = True
    if len(arr) == 2*A:
        perttern.add(make_comb(arr))
        return
    for p in range(h*w):
        if visit[p]:
            continue
        v = p//w
        z = p % h
        if len(arr) % 2 == 1:
            s = arr[-1]
            x = s//w
            y = s % h
            if abs(x-v)+abs(y-z) == 1:
                dfs(p, arr)
                q = arr.pop()
                visit[q] = False
        else:
            dfs(p, arr)
            q = arr.pop()
            visit[q] = False


def make_comb(input_array):
    n = len(input_array)//2
    re = []
    for i in range(n):
        re.append(sorted(input_array[2*i:2*i+2]))
    re.sort()
    r = []
    for i in range(n):
        r.extend(re[i])
    return tuple(r)


for i in range(h*w):
    visit = [False]*h*w
    dfs(0, [])
print(len(perttern))
print(perttern)
