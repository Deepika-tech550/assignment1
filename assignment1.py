#Try 5 Different functions of the String in Python.

print("'STRING OPERATIONS'".center(25))
#1. CAPITALIZE
name="deepika"
print(name.capitalize())
#2.index
print(name.index('p'))
#3.find
print(name.find('a'))
#4.center
print(name.center(23))
#5.islower
print(name.islower())

print("*********************************************")
#Try 5 Different functions of the List object in Python
print("'LIST OPERATION'".center(25))


l=[1,2,3,3,4]

a=l.append(5)   #1
print(l)
c=l.count(3)    #2
print(c)
p=l.pop(3)      #3
print(p)
r=l.reverse()   #4
print(l)
s=l.sort()      #5
print(l)
print("***********************************************") 

#Experiment with at least 5 default functions of Dictionary
print("dictionary operations".center(25))

d={1:'Ram',2:"Som",3:"Tom",4:"Raj"}
print(d.get(2))     #1
print(d.keys())     #2
print(d.values())   #3
print(d.popitem())  #4
d[4]="Radha"
print(d)            #5

print("***********************************************")





