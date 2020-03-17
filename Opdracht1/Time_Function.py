import time
import numpy as np

def time_measurer(func, lst, n=1): # Time measurer of sort function With ability to run it mutiple times
    l = np.zeros(n)
    for i in range(n):
        start = time.time()
        func(lst.copy())
        end = time.time()
        l[i] = end-start
    return l.mean()

def sort_timer(func):
    np.random.seed(seed=420)
    lst_1 = np.random.randint(low=1, high=10000, size=1000).tolist()
    lst_2 = np.random.randint(low=1, high=10000, size=10000).tolist()
    lst_3 = np.random.randint(low=1, high=10000, size=30000).tolist()

    print("Results with buckets_sort")
    for lst in [lst_1,lst_2,lst_3]:
        print(f"  Random list (n={len(lst)})\t\t{round(time_measurer(func,lst.copy(),5),6)}")