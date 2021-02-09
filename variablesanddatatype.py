# -*- coding: utf-8 -*-

#list
#values are ordered and mutable
print("list")
lis = [1,2,3,4,5,6,7]
lis.insert(1,100)
for i in lis:
    print(i)

#tuple 
#values are ordered and immutable
print("tuple")
tup = (1,7,8,10,2)
for i in tup:
    print(i)

#set
#values are unordered , Unique and immutable.
print("set")
se = {1,2,2,25,17,3,3,5}
for i in se:
    print(i)

#dictonary
print("dictonary")
di = {"k1":1,"k2":2,"k3":3}
print(di["k1"])
#if the key is not there get method will return none.
print(di.get("K4"))
print(di.get("k1"))