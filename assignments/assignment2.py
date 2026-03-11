#Assignment  on lists:
## Create a list of numbers (Eg. 34, 35, 84, 23, 19)
## sort the list in ascending order 
## remove number 23 from the list
## print the list

my_list=[34,35,84,23,19]
my_list.sort()
print(my_list)
my_list.remove(23)
print(my_list)


## Create a list todo list ["wake up", "Exercise", "work"]
## delete the third task using del
## delete the second task using pop
## delete the first task using remove
##print the list
todo_list=["wake up","Exercise","work"]
del todo_list[2]
print(todo_list)
todo_list.pop(1)
print(todo_list)
todo_list.remove("wake up")
print(todo_list)

 

## Create a list of five names
## reverse the order of list
## print list
names=["gouse","nagoorbe","lowshi","jasmin","anshir"]
names.reverse()
print(names)




#Assignment 4
##Create a list of five numbers in random order
##sorrt the list in descending order
## remove the smallest number using pop
##print list
num=[23,12,89,5,34]
num.sort(reverse=True)
print(num)
num.pop(4)
print(num)
 

#Assignment 5
## Create a list of five city names
## insert a new city at the third position
## append a new city at the end
## reverse the list
## remove the exact middle element using del
## print the list

city=["hyderabad","mumbai","chennai","banglore","delhi"]
city.insert(2,"nellore")
print(city)
city.append("karnataka")
print(city)
city.reverse()
print(city)
del city[3]
print(city)
