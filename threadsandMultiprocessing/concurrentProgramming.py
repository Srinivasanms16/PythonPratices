import concurrent.futures
import time
import mypro


def callmultiThreading():
    with concurrent.futures.ThreadPoolExecutor() as texecuter:
        texecuter.map(callmultiprocessings,range(10))
            


def callmultiprocessings():
    print("calling multiprocessing")
    mypro.callmultiproc()
