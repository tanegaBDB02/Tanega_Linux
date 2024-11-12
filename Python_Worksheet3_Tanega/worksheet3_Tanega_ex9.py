import time

def time_measure(func):
    def wrapper():
        start_time=time.time()
        result=func()
        print(f"{func.__name__} executed in {time.time() - start_time:.4f} seconds")
        return result
    return wrapper

@time_measure
def sample_function():
    time.sleep(2)

sample_function()
