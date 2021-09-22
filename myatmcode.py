# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:23:13 2018

@author: rajak
"""
print("\t\t\t\t\t\twelcome to my atm")
class Bank_account():
    def __init__(self,account_balance):
        self.account_balance=account_balance
    def withdraw(self,a):
        self.a=a
        if self.account_balance<self.a:
            print("insuficient fund")
        elif self.a>25000:
            print("invalid entry please put lesser amount")
        else:
            self.account_balance -=a
            print("your current balence is:",self.account_balance)
    def deposite(self,b):
        self.account_balance +=b
        print("your current balence is:",self.account_balance)
x=int(input("enter your balance:"))
obj=Bank_account(x)
c=int(input("enter your pin:"))
if c==1234:
    print("""Please choose your option
       1.check your current balence
       2.deposite amount
       3.withdraw amount""")
    d=int(input("enter your choise:"))
    if d==1:
        print("your current balence is:",obj.account_balance)
    elif d==2:
        r=int(input("enter your deposite amount:"))
        print("your new current balence is:",obj.account_balance+r)
    elif d==3:
        l=int(input("enter your withdraw amount:"))
        if l>obj.account_balance:
            print("insufficient fund")
        else:
            print("your new current balence is:",obj.account_balance-l)   
else:
    print("wrong pin ,please try again......")
input("press any key for exit")
            