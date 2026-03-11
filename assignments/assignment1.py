
#Assignment 1: Personal Information Formatter
#Write a program that asks for a person's name, age, city, and favorite color. Format and display this information in a neat way using f-strings.

name=input("enter your name:")
age=int(input("enter your age:"))
city=input("enter your city name:")
fav_color=input("enter your favourite color:")
print(f"My name is {name}.I am {age} years old.I am currently living in {city}. And my favourite color is {fav_color} ")



#Assignment 2: String Manipulator
#Create a program that asks the user to enter a string, then displays:
#The string in all uppercase
#The string in all lowercase
#The length of the string
#The first and last characters
#The string reversed

str=input("enter the string:")
print(str.upper())
print(str.lower())
print(len(str))
print(str[0],str[-1])
print(str[::-1])

#Assignment 3: String Password Validator
#Write a program that checks if a password meets the following criteria:
#At least 8 characters long
#Contains at least one uppercase letter
#Contains at least one lowercase letter
#Contains at least one digit Display appropriate messages for each check.

password = input("Enter password: ")

upper = lower = digit = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True

if len(password) >= 8:
    print(" Length is OK")
else:
    print(" Password must be at least 8 characters")

if upper:
    print(" Uppercase letter present")
else:
    print(" Add at least one uppercase letter")

if lower:
    print(" Lowercase letter present")
else:
    print("Add at least one lowercase letter")

if digit:
    print(" Digit present")
else:
    print(" Add at least one digit")

#Assignment 4: Character Counter
#Create a program that counts how many vowels (a, e, i, o, u) and consonants are in a string entered by the user. Ignore spaces and punctuation.
text=input("enter  the text:")
vowels="aeiouAEIOU"
v_count,c_count=0,0
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count+=1
        else:
            c_count+=1
print("vowels:",v_count) 
print("consonants:",c_count)               


#Assignment 5: Nickname Generator
#Write a program that creates a nickname for a user based on their full name. It should:
#Ask for their first and last name
#Create a nickname using the first two letters of their first name and the first three letters of their last name
#Display the nickname in all uppercase

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

nickname = first_name[:2] + last_name[:3]

print("Your nickname is:", nickname.upper())