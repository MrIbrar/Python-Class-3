# 2 numbers input lo aur unka sum print karo.
num1 = float(input("Enter the 1st Number"))
num2 = float(input("Enter the 2nd Number"))
print("Sum of numbers is: ",(num1+num2))


# Ek number input lo, aur uska table (1-10) print karo.
num = 12
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(num," x ",i," = ", num*i)


# User se number lo aur batao Even hai ya Odd
num = int(input("Enter the number: "))
if(num%2==0):
    print("The given number is Even")
else:
    print("The given number is Odd")


# 1 se lekar N tak ke numbers ka total sum nikalo. (Use loop)
num = int(input("Enter the number: "))
sum = 0
for i in range(1, num+1):
    sum= sum+i

print("1 to ",num," sum is: ",sum)

another method to solve the Question:

num = int(input("Enter the number:"))
sum = 0
for i in range(1, num+1):
    sum+=i

print("1 to ",num," sum is ",sum)



# User se ek string lo aur usko reverse karke print karo.
str = input("Enter the User Name: ")
reversed_str = str[::-1]
print("Reverse string is; ", reversed_str)


Function likho jo kisi number ka factorial return kare.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result
num = int(input("Enter the Number: "))
print("Factorial of number ",num," is: ",factorial(num))


# Function banao jo check kare ki number prime hai ya nahi.
def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
num = int(input("Check the number: "))
if prime(num):
    print("These ",num," is prime number")
else:
    print("These ",num," is not a  prime number")
    
    
# N terms tak fibonacci series print karo (using loop and function).
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n+1):
        print(a, end=" ")
        a, b = b, a + b

terms = int(input("Fibonacci series ke liye kitni terms chahiye: "))
print(f"{terms} terms of Fibonacci series:")
fibonacci_series(terms)
