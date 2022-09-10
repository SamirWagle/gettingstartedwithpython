#program to print fibonacci series
a=0
b=1
c=int(input("Enter the number of terms: "))
for i in range(0,c):
    print("i is",i)    
    d=a+b
    a=b
    b=d
    print(d)
#boolean checks
print(bool(0)) #false
print(bool(5>6 ))
print(bool(6>5))
print("ISINSTANCE CHECK")
print("Given nymber is of checking data type or not???")
print("integer",isinstance(a, int)) #True     
print("string",isinstance(a, str)) #false

