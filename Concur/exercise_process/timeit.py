import time

def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s 函數執行時長:%.6f"%(f.__name__, end_time-start_time))
        return res
    return wrapper