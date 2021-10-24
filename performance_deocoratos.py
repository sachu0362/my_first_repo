# performance decorator.
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')

    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()
