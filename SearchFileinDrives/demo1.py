import time
def timer(fun):
    def wrapper(*kargrs,**kwargs):
        start_time=time.time()
        result=fun(*kargrs,**kwargs)
        end_time=time.time()
        print(end_time-start_time)

    print(wrapper)
    return wrapper
@timer
def cal(n):
    for i in range(n):
        print(i)

cal(100000)



