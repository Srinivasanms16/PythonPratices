import concurrent.futures
import time
import mypro


def callmultiThreading():
    with concurrent.futures.ThreadPoolExecutor() as texecuter:
        for _ in range(10):
            texecuter.submit(mypro.fun1,1)


def callmultiprocessings():
    print("calling multiprocessing")
    mypro.callmultiproc()
