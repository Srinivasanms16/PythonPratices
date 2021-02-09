# -*- coding: utf-8 -*-

def checkforloop(lis):
    for i in lis:
        print("For loop :"+str(i))
        
def checkforwhile(con):
    i = 0
    while(i<=con):
        if i==100:
            break
        print("While loop :"+str(i))
        i = i+1
    else:
        print("No break")
