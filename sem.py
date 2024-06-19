# python fourth tpye in variable fist is a set , seacund is a list, and third is  tuple, fourth is dirctory
# fist set symbol of {}
# where is not allowed value duplicatoin 
# a={27,27,'arvind'}
# print(a)
# print(type(a))
#Secound is a list symbol of[]
# Dublication are allowed
# a=['Arvind',60,4.7]
# print(type(a))
# print(a)
#third and last is tuple symbole of()
# a=(10,'arvind',45.0)
# print(type(a))
# print(a)
# fourth is a directory it is not allowed in key duplicatoin 
# a=('age:18',)
# print(type(a))
# print(a)
# conditoinal statement if else,elif
# a=int(input("Enter the number :"))
# if a%2==0:
#     print('even')
# elif a<18:
#     print('not adalt')
# else:
#     print('odd')

# itrative statment loops like for, while, do while
# a=int(input("Enter the number"))
# for number in range(1,11):
#     print(a*number)

# while loop
# password='ARVIND12'
# password=input("Enter the password")
# while password!=password:
#    password=input("Enter the password:")
# else:
#     print('Unloock!!')

# today topic discussed in a module in python 
# module is first.file are created to import a seaound file to use a fucntoin 
# program write a first file to use all functoin in import a funtoimn are used 
# write a from import first file call only for functoin to print a data one file to outher file is called a 
# module 

# def fun():
#     print("arvind")
#     # print(a+b)


# what is a exceptoin 
# exceptoin is nothing but runtime error and it occure due to incrrect implemetatoin of logic 
# then a discused what is a file handling so 
# file handling nothing but a frist of all runtime error its a machnisum to solve a runtime error 
# thoeritical are = file handling  its a machcanisum througth which can handle runtime error 
# three type handle a runtime error 
# first try
# seound is except
# third is else 
# let eg

# a=int(input("Enter the no."))
# b=int(input("Enter the secound no"))
# try:
#     c=a/b
#     print("result:",c)
# except:
#     print(" cant divisible a values")

#     print("i am a devloper ")

# file handling 
# first is khown what is a file 
# so, file is nothig but a name of memory in locatoin to store a data permanatly.
# what is a file handling is nothing but its a machenisum througth which can a handle a (create , delet, read
# write append, etc ) the file
# first is main () is open()its a function to use with files and its take two parameter 
# file mode ________                  file opration 
# r=read                                create
# w=write                                 read 
# a=append                                 write
# rt=read and write both                   copy
# b=binary mode                            delet
 
# lets eg
# syn. 
# f=open("","")
#    passing a two parameter in function frist is path of folter to copy to paste a and its a locatoin in file
# and name of who create a file 
# secound is say what opreatoin to perform in file pass a w,r,rt,c,b any pass
# importent note // are complesary in path and all perform then close() its used to close a file
# eg
# using write()
# f=open("C:\\Users\\ankes\\OneDrive\\Desktop\\ap.html\\A.text","w")
# f.write("we are learn a python \n arvind is a dev")
# print("data wrote sucssesfully ")

# using read()
# f=open("C:\\Users\\ankes\\OneDrive\\Desktop\\ap.html\\A.text","r")
# (f.read(30)) means display only for 30 words
# print(f.read(30))
# (f.readline()) means display only for a single lines
# print(f.readline())
# (f.readlines()) means display for a all lines
# print(f.readlines())
# print("data read sucssesfully ")

# using copy
# f2=open("C:\\Users\\ankes\\OneDrive\\Desktop\\ap.html\\A.text","r") 
# f3=open("C:\\Users\\ankes\\OneDrive\\Desktop\\ap.html\\b.text","w")
# for i in f2:
#  f3.write(i)

# f2 .close()
# print("file clossed")

# using delit()

#today topic discussed a constructor 
# constractor noting but spocial type of functoin that gets automaticali called when class of object 
# created ,constructor are two type in python first is defoult constructor and secound is paremitterise 
# constructor 
# syn.
# def __init__(self):
# code
# eg
# class A:
#     age=18
#     def __init__(self):
#        name="arvind"
#        print(name,"",self.age)
# obj=A()

# defult constructor 
# defult constructor also called a empty construtor becouse it dont have a any parametter
# a we do not define any constructor the compailer automatically call  the defoult constructor 
# syn 
# class class_name:
# def __init__(self):
# code
# eg.
# class A: 
#     name="arvind"
#     age=18
#     def __init__(self):
#       print(self.name)
#     def show(self):
#       print(self.age)
    
# obj=A()
# obj.show()

# paramitterise constructor 
# paramitterise constructor accept arguments along with self  is known as paramitterise constuctor
# eg
# class A:
#     name2="arvind"
#     def __init__(self,age,name,address):
#         address="faridabad"
#         print(age,name,address,self.name2)
#     def Show(self):
#             print(self.name2)

# obj=A(18,"arvind",None)
# obj.Show()

# Modifires in python
# modifire is acces modifire are used to set the limit of memebr accessbility 
# lets eg.
# var (its a puclicly access in anyone)
# _var (its a used a single uderscore to protected its only for used inside the class and outside the class
# not acces the outhe class)
# __var (its a privet and when used to double undersore its used only for a inside the class not a outside the 
# class and other )
# eg.

# class A:
#     a=10
#     _b=20
#     __c=None
#     print(a,"",_b,"",__c)
# class B(A):
#     pass
# obj=B()
# print(obj.a)
# print(obj._b)
# # print(obj.__c)

# Multithreading in python
# multithreading is a techniqe which allow of a cpu to excute multliple threade of one process at a same time
# Multithreading 
# the perpose of multithreading is to run a multiple taske and fuuncroin at same time
# thread
# thread is a predefined class in a threading module 
# thread is a  basic unit of cpu and it is known for independent excutoin 
# thread class mathord
# 1.run() 2.start() 3.join() 4.is a live() 5.set name()  6.getname()
# two type of thraed first is single thread and seacund is a multithread 
# eg of single thread
# class A:
#     def run(self):
#         for i in range(5):
#             print("arvind")
# class B:
#     def run(self):
#         for i in range(5):
#          print("govind")
# t1=A()
# t2=B()
# t1.run()
# t2.run()

# eg Multithreading 
# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("arvind")
#             sleep(1)
# class B(Thread)  :
#     def run(self):
#         print("govind")  
#         sleep(1)        
            
# t1=A()
# t2=B()
# t1.start()
# t2.start()

# will be dicussed oops in python means object oriented programing langunage system 
# topics 
# object, and class
# inharitance 
# polymorisum
# abstractoin 
# encupsulation 

# first is object and class
# object - object is a physical type and real wourld entity  that woek on class
# note--each object has a district role or resposiblity
# object create a space on memory as perivt class member
# eg acces a funtion 

# class A:
#     age=18
#     def fun(self):
#         "arvind"
#         name="learn coding"
#         print(name)

# obj=A()
# obj.fun()
# print(obj.fun.__doc__)
# print(obj.age)  
# print(A.age) 

# class-class is logical type real would entity and it is a blue print of object 
# real would entity like a behaviar  properties
# eg
# class A:
#     def __init__(self):
#         age=10
#         print(age)
# obj=A()
# obj2=A()

# inheriteance --inharitease in define a class when create a outher class to inharite the all propertise 
# is called a inhritance
# types in inheritance 
# simple inhertitance 
# multiple inheritance
# multi-level inheritance
# hybride inheritance
# hararycal inhertance
# eg
# class A:
#     def fun(self):
#         print("having smartphone  ")
# class son(A):
#     def mem(self):
#         print("its memory are largest ")     
# S=son() 
# S.fun()  
# S.mem()        
#

# polymorphorius 
# polymorisium is a ability to take various form (same objects having diffrent behaviar)
# polymorisum is two type= 1.overloading  2. overriding
# eg.
# print(5+5)=10  ->add
# print("5",+,"5")=55 ->concet
# it is eg of polymorisum 

# Mathord overloding
# Mathod overloading means a whenever contains more then one mathord with same name 
# and differnet type of parametter called mathod overloding
# eg.
# class A:
#     def ap(self,fristname="",lastname=""):
#         print("welcome",fristname,lastname)

# obj=A()
# obj.ap()
# obj.ap("arvind")  
# obj.ap("arvind","govind")   

# Methord overriding
# whenever we write a same name with singnature in parent & child class is called overrinding
# eg
# class A:
#     def gp(self):
#         print("arvind")
# class B(A):
#     def gp(self):
#         super().gp()
#         print("govind")


# obj=B()
# obj.gp()    
            

# Encpsulatoin 
# encapsulatoin is acces to all the variable and mathord globelly by using envapslatoin  we can restrict 
# variable and mathoed acess gloable by making a protected and privet
# note=single underscore_ =_a=protected
# double underscore __=__ a=privet
# eg.
# class A:
#     _a=10
#     __b=20
#     def show(self):
#         print("a=",self._a)
#         print("b=",self.__b)

# obj=A()
# obj.show()     
# 
# Abstarction 
# abstractoin is prosse of hinding the implementatoin details from user and highlight the sevices provid
# the user
# eg
# first.py
# def add()
# a=int(input("enter the no"))  
# b=int(input("enter the no "))
# sum=a+b
# print("additoin of two no",sum)

# secound.py
# def sub()
# a=int(input("enter the no"))  
# b=int(input("enter the no "))
# sub=a-b
# print("subtractoin of two no",sub)

# main.py
# import first,secound
# first.add()
# seound.sub()

# abstractoin is two type first is abstract class
# secound is interface

# abstract class
# abstract class is that contains one or more abstract method is called abtrct classs
# note:
# an object of an abtract clsss cannot create 
# python provide abc module to work with abstractoin 
# we use @abstractmethod decreator to define abstract method
# eg
# from abc import ABC, abstractmethod
# class car(ABC):
#     def show(self):
#         print("every car has 4 whils")
#     @abstractmethod
#     def  speed(self):
#       pass
# class maruti(car):
#     def speed(self):
#         print("40km per hour")    
# class shujuki(car):
#     def speed(self):
#         print("car is super fast")
# obj=maruti()
# obj.speed()
# obj.show()         


# interface
# interface is also called a abstract class it is a contains a method but not a normal mathod
# note:
# we cant create object of interface 
# we usse interface when an  actoin is commman but implementatoin 
# all child  class should be inharit abstract method
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def show(self):
#         pass
# class squre(shape):
#     def show(self):
#         print("squre of a4 sides")
# class Circle(shape):
#     def show(self):
#         print("circle has round shape")
# obj=squre()
# obj.show()
# a=Circle() 
# a.show()
       
