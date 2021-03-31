# -*- coding: utf-8 -*-


# we should always filter the main script when your using Process . because when we exccute some code in Multiprocessing in window 
# while creating new process it will load the main script . So we add if condition with __name__ == __main 
#then it will excute only once , when new process are created this code will not execute only code which we want to execute in
# child process will run.
#this will happen only in windows and Multiprocessing not for Multithreading and not for linux os.
#for other we dont want to add if __name__ == __main__

print(__name__)
if __name__ == "__main__":
    try:
        import camelcase
        #Python can import the modules(files) in the current working directroy or some specific folder present in sys.path
        #To import the module(file) from other directory we have use sys package.
        #sys.path.insert the path of the folder where the modules or files resides.
        import sys
        sys.path.insert(1,"./Classes")
        from classandInheritance import school
        from Conditions import greatestof3
        from functions import calculator,printname
        import looping as loop
        sys.path.insert(2,"./Classes/child")
        import dates as dt
        sys.path.insert(3,"./threadsandMultiprocessing")
        import concurrentProgramming as cp


        #class and Inheritance
        myobj = school("LKG","Nithin","Shivaa")
        myobj.printInfo() 

        print(f"Biggest number is :{str(greatestof3(10,20,9))}")

        #function returns multiple values.
        sum,diff,mul,div = calculator(10,20)
        print("Sum is :",sum)
        print("Diff is :",diff)
        print("Mul is :",mul)
        print("Div is :",div)

        printname("srinivasan")

        #loop
        loop.checkforloop([1,2,3,4,5,6,7,8])
        loop.checkforwhile(10)

        #pipenv package
        cc = camelcase.CamelCase()
        print(cc.hump("Hello World"))

        #datetime in pythion
        print(dt.daresult)

        #get user input and format the string
        name = input("Enter you name :")
        message = "hello , {0} "
        print(message.format(name))
    except Exception as e:
        #e will have exception message.
        print(e)
    else:
        print("No issues")
    finally:
        print("finally block")

        cp.callmultiThreading()
        cp.callmultiprocessings()
    