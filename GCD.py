# GCD: Greatest Common finding Algorithm and the Time Complexity  is O(n)

num1 = int(input("Enter the first number : "))

num2 = int(input("Enter the second number :"))

# Euclidian Algorithm of finding the GCD or HCF
def gcd(num1,num2):
        while(num1):
         temp = num1
         num1  = num2%num1
         num2 = temp
        return num2
        
lcm = (num1*num2)/gcd(num1,num2)

print(f"The LCM is = {lcm}")

    









     

