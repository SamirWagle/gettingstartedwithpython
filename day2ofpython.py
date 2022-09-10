#using some of the arithmetic operations in python
print(2+3)
a=6
b=9
a+=4
print(a,b)
print(a+b)
print(a-b)
print(a+0.69)
# we use double asterick for power
print(4**4)

#logical operators using in pythons
x = 5
print(x < 3 or x >10) #false
print(x < 3 or x >10) #true 
print("Identity operator using in python")
#python identity operators use
#is and is not are two identity operators used in python
#is is used to check if two variables are the same object
#is not is used to check if two variables are not the same object
print(1 is 1)
a=int(55)
print (a is 55)
wagle=["samir","hari","manish", "madan"]
family=["samir","hari","manish", "madan"]
print(wagle is family) #FALSE BECAUSE ALTHOUGH THEY HAVE SAME DATA THEY ARE NOT SAME 
c=wagle
print("now checking whether they are same or not after assigning its value to another variable")
print(c is wagle)

