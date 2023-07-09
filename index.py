def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multipilcation(a,b):
    return a*b
def division(a,b):
    return a/b
print("a . addition ")
print("b . subtraction")
print("c . multiplication")
print(" d.Division")
c=input("c=\n")
num_1=int(input())
num_2=int(input())
if c=="a":
    print(addition(num_1,num_2))
if c=="b":
    print(subtraction(num_1,num_2))
if c=="c":
    print(multipilcation(num_1,num_2))
if c=="d":
    print(division(num_1,num_2))  