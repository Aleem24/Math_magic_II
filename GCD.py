# GCD: Greatest Common finding Algorithm and the Time Complexity  is O(n)

num1 = int(input("Enter the first number : "))

num2 = int(input("Enter the second number :"))

# Euclidian Algorithm of finding the GCD or HCF

if(num1 < num2):
    while(num1):
        temp = num1
        num1  = num2%num1
        num2 = temp
        print(f"The GCD between {num1} and {num2} is : {num2}")

elif(num2<num1): 
    while(num2):
        temp = num2
        num2  = num1%num2
        num1 = temp
        print(f"The GCD between {num1} and {num2} is : {num1}")
else:
     print(f"The GCD between {num1} and {num2} is : {num1}")
     

