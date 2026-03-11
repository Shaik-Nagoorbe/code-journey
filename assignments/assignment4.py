#Sets:
#my_games = {"cricket", "football", "tennis"}
#friend_games = {"badminton", "cricket", "chess"}
#combine both sets so that you have all unique games between two sets
#print final set
my_games = {"cricket", "football", "tennis"}
friend_games = {"badminton", "cricket", "chess"}
final_set=my_games|friend_games
print(final_set)
#another method:
final_set2=my_games.union(friend_games)
print(final_set2)
 


#games = {"badminton", "cricket", "chess"}
# Try removing "throwball" without throwing any error
# Try removing "throwball" with throwing error if it doesnt exist
games = {"badminton", "cricket", "chess"}
games.discard("throwball")
print(games)
#games.remove("throwball")
#print(games)

 


#my_games = {"cricket", "football", "tennis"}
#friend_games = {"badminton", "cricket", "chess"}
# Find the games that are in first set but not in second set
# print result
my_games = {"cricket", "football", "tennis"}
friend_games = {"badminton", "cricket", "chess"}
result=my_games-friend_games
print(result)
#another method
result2=my_games.difference(friend_games)
print(result2)



 


#my_games = {"cricket", "football", "tennis"}
# use clear() to empty set
# Then using update(), add items - baseball, golf, tennis
# copy it to another set
# print it

my_games = {"cricket", "football", "tennis"}
my_games.clear()
print(my_games)
my_games.update(["baseball","golf","tennis"])
print(my_games)
new_games=my_games.copy()
print(new_games)

