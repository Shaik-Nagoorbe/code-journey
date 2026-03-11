# sample
print("hello world")

# addition
num1=float(input ("enter the  first number :"))
num2=float(input("enter the second number:"))
result=num1 +num2
print (f"sum : {num1} +{num2}={result}")

# division
num3=float(input("enter the dividend for division:"))
num4=float(input("enter the divisor for division:"))
if num4==0:
    print("Error: division by zero is not allowed")
else:
    result=num3/num4
    print(f"division :{num3}/{num4}:{result}")    

# area of triangle
base=int(input(" enter the base of the triangle:"))
height= int(input("enter the height of the triangle"))
area=1/2 * base * height
print("the area of the triangle:",{area})


# swapping two variables without using third variable
a=int(input("enter  a value:"))
b=int(input("enter  b value:"))
print("before swapping  value of a:",{a})
print("before swapping value of b:",{b})
a,b=b,a
print("after swapping value of a:",{a})
print("after swapping value of b:",{b})


# swapping two variables with using third varible
a=10
b=7
temp=a
a=b
b=temp
print("after swapping value of a:",{a})
print("after sawpping value  of b:",{b})

#write a program to generate a random number
import random
print(f"Random number: {random.randint(1,100)}")
print(f"random number in float:{random.uniform(1,100)}")
print(f"random number inn float using another method:{random .random()}")
text="Hello nagoorbe"
print(f"random word:{random.choice(text)}")

# python program to convert kilometers into miles
kilometers=float(input("enter the  distance in kilometers:"))
#conversion of  one kilometer is equal to 0.621371
conversion_factor=0.621371
miles=kilometers*conversion_factor
print(f"{kilometers} kilometer is equal to {miles}miles")


#program to display the calendar
import calendar
year=int (input("enter the year:"))
month=int(input("enter the month:"))
cal=calendar.month( year,month)
print(cal)


# python program to check if given number is postive or negative or zero
num=int(input("entert the number:"))
if num>0:
    print("postive number")
elif num==0:
    print("zero")
else:
    print("negative number")    


#python program to check the given number is even or odd
num=int(input("eneter the number:"))
if num%2==0:
    print("number is even number")
else:
    print("number is odd number")    

# write a python program to check a leap year
year=int(input("enter the year:"))
if (year%400==0)and (year%100==0):
    print("{0} is a leap year".format(year))
elif(year%4==0) and (year%100!=0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))            


#python program to check the given number is prime number or not
num =int(input("enter the number:"))
flag =False
if num==1:
    print(f"{num} is not a prime number")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")          


# python program to print all prime numbers in an intervavl
start=1
end=10
print("prime numbers between ",start,"and",end, "are:")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:   
            print(num)          


#python program to find the factorial of a number
num= int(input("enter the number:"))
factorial=1
if num<0:
    print("Factorial doesnot exist forr negative numbers")
elif num==0:
    print("factorial of o is 1")
else:
    for i in range (1,num+1):
        factorial =factorial*i
    print(f"the factorial of {num} is {factorial}")     


#display multiplication table
num= int(input(" enter the table number:"))
for i in range(1,11):
    print(num, "*",i, "=",(i*num))

# sum of digits of a number
num=1234
sum_digits=0
while num>0:
    sum_digits+=num%10
    num//=10
print(sum_digits)    

#another method for sum of digits in   number
num=6789
print(sum(map(int,str(num))))


#simple calculator program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter choice (1/2/3/4/5): ")
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == '5':
    result = num1 % num2
    print("Result:", result)
else:
    print("Invalid input! Please select a valid operation.")

#Write a program to find the largest of two numbers using if–else.
num1=int(input("enter the  first number:"))
num2=int(input("enter the  second number:"))
if num1>num2:
    print("num1 is largest number")
else:
    print("num2 is largest number")    

#Write a Python program to check whether a person is eligible to vote.
age=int(input("enter the age of the person:"))
if age>=18:
    print("the person is eligible for vote") 
else:
    print("the person is not eligible for vote")      


#Write a Python program to find the largest of three numbers using conditional statements.
num1=int(input("enter the first number:"))     
num2=int(input("enter the second number:"))     
num3=int(input("enter the third number:"))     
if num1>num2 and num1>num3:
    print(num1,"is greater")
elif num2>num1 and num2>num3:
    print(num2, "is greater")
else:
    print(num3,"is greater")    


#Write a program to check whether a character entered by the user is a vowel or consonant.
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


#leap year or not
year=int(input("enter the year:"))
if (year%4==0 and year%100!=0 ) or year%400==0:
    print("leap year")
else:
    print("not a leap year")

#Write a program to check if a number is divisible by both 3 and 5.
n=int(input("enter the number:"))
if(n%3==0 and n%5==0):
    print(f"{n} is divisible by both 3 and 5")
else:
    print(f"{n} is not divisible by both 3 and 5")      

#Write a Python program to check whether a given number is:
#Multiple of 3
#Multiple of 5
#Multiple of both
#Not a multiple of any    
num=int(input("enter the number:"))
if num%3==0:
    print(f"{num} is multiple of 3")
elif num%5==0:
    print(f"{num} is multiple of 5")
elif num%3==0 and num%5==0 :
    print(f"{num} is multiple of both 3 and 5") 
else:
    print(f"{num} is not multiple of any")           

# program to check the given character is uppercase,lowercase,digit or special character:
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# program to check the number is postive even,postive odd,negative even,negative odd and zero:
num=int(input("enter the number:"))
if num>0:
    if num%2==0:
        print(f"{num} is postiven even")
    else:
        print(f"{num} is postive odd")
elif num<0:
    if num%2==0:
        print(f"{num} is negative even")
    else:
        print(f"{num} is negative odd")
else:
    print("zero")                        


#Write a program to calculate the electricity bill using these rules:
#Units ≤ 100 → ₹5 per unit
#101–200 units → ₹7 per unit
#201–300 units → ₹10 per unit
#Above 300 units → ₹15 per unit
units = int(input("Enter the number of units: "))

if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
elif units <= 300:
    rate = 10
else:
    rate = 15

bill = units * rate
print(f"Total Electricity Bill = ₹{bill}")

#total number of vowels in a string
str=input("enter the string:")
total=0
vowels="aeiouAEIOU"
for ch in str:
    if ch in vowels:
       total=total+1
print("total number of vowels :",total) 

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Finished")


for x in range(3):
    for y in range(2):
        print(x, y)
#to  count number of vowels in a string
str="hello world"
vowels="aeiouAEIOU"
count=0
for i in str:
    if i in vowels:
        count+=1
print(count)    

# Write a Python program to print all even numbers between 1 and 20 using a loop     
for i in range(1,21):
    if i%2==0:
        print(i ,end=" ")

#Write a Python program to find the largest number in a list without using the max() function.
lis=[10, 4, 25, 8, 15]
largest=0
for i in lis:
    if i >largest:
        largest=i
print(largest)        


# Write a Python program to count how many digits are in a number.
num = 5032
count = 0

while num > 0:
    count += 1
    num //= 10

print(count)


#grade calculator
marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0 and 100.")
else:
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Your grade is:", grade)


#print all the even numbers from 1 to 100
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")
# another method:
for i in range(2,101,2):
    print(i,end=" ")  

# sum of all natural numbers upto n
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i 
print("Sum of all natural numbers up to", n, "is:", total)


#maximum of two numbers using function:
def max(x,y):
    if x>y:
        return x
    else:
        return y
x=54
y=45      
print("maximum of two numbers is:",max(x,y))

#factorial of a number:
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

#simple interest:
p=10000
t=10
r=10
si=(p*t*r)/100
print(si)
