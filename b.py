import time


def func(n):
    if n <= 3:
        return 1
    else:
        return func(n-1)+func(n-2)+func(n-3)+func(n-3)

start=time.time()
func(25)
end=time.time()
elapsed_time=end-start
print(elapsed_time)
start=time.time()
func(26)
end=time.time()
elapsed_time=end-start
print(elapsed_time)