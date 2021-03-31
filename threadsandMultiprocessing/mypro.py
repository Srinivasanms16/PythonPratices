from concurrent.futures import ProcessPoolExecutor
from time import sleep


def fun1(sec):
    print("execute start")
    sleep(sec)
    print("execute end")

def callmultiproc():
    #max_workers is maxing number of process you want to create.
    with ProcessPoolExecutor(max_workers=3) as pexecuter:
        for _ in range(10):
            pexecuter.submit(fun1,1)
        
