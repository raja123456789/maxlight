"""Created on Mon Mar 25 21:39:37 2019 @author: rajak """
"""Coding Problem !"""

def count(query):
    d=0
    for i in l:
        if(query==i):
            d=d+1
    return d
a=int(input("Enter the size of array:"))
l=[int(n) for n in input("enter the space separated integers:").split()]
if(len(l)>a):
   print("You enter",len(l),"Which is greater than array size..")    
else:
    b=int(input("Enter your query:"))
    occurance=count(b)
    if(occurance!=0):
       print(occurance)
    else:
         print("Not Present")



    