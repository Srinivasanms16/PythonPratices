# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:47:41 2021

@author: SAmarna
"""

#import module
#from module import members

#import student as st

from student import student

#Inheritating the Class
class school(student):

    #similar to constructor.
    def __init__(self,std,fname,lname):
        super().__init__(fname,lname)
        self.standard = std

    #this printInfo will override the printInfo in parent.
    def printInfo(self):
        print("Standard is "+self.standard)
        super().printInfo()
    
        
        
