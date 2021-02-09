# -*- coding: utf-8 -*-

#Creating class
class student:
    id = 122
    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname
        
    def printInfo(self):
        print("firstname is "+self.fname)
        print("lastname is "+self.lname)
        print("Stident ID is "+str(self.id))
