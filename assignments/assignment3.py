#tuple:
# create a tuple with numbers  3, 4, 5, 7, 3, 9, 3, 11
# print how many times 3 appears in the tuple
# print index of 7
numbers=(3,4,5,7,3,9,3,11)
print(numbers.count(3))
print(numbers.index(7))

 

#create a list of five colors - red, yellow, green, blue, black
# convert them into tuple and print it
# convert it back to list and add "white"
# convert it back to tuple and print
colors=["red","yellow","green","blue","black"]
con_tup=tuple(colors)
print(con_tup)
list2=list(con_tup)
list2.append("white")
new_tup=tuple(list2)
print(new_tup)


# create two tuples t1 - 10, 20, 20 & t2 - 40, 50, 60
# Add both tuples and create a new tuple called t3
# print t3

t1=(10,20,20)
t2=(40,50,60)
t3=t1+t2
print(t3)


# create a tuple with items as  - A, B, C
# multiply the tuple by 3 to repeat its elements
# print the final tuple
items=("A","B","c")
final_items=items*3
print(final_items)


# Create a tuple 0 five animal names - dog, cat, elephant, lion, tiger
# remove 'elephant' from it
# Add 'cheetah'
# print the final tuple
animals=("dog","cat","elephant","lion","tiger")
new_list=list(animals)
new_list.remove("elephant")
new_list.append("cheetah")
final_tup=tuple(new_list)
print(final_tup)