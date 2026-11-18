#%%
#Working wtih lists
Things = []
Things.append('Shoe')
Things.append('Hat')
Things.append('glove')
Things.append('coat')
print(Things)
for thing in Things:
    print(thing.upper())
    print(" Here is an item: " + thing.title())
    #so it repeats the 2 prints and then goes ot the next item in list to print those 2 and so on
for number in range(1,6):
    print(number)
#this next one puts these numbers into a list, not just prints them like the previous one
numbers = list(range(1,12,2))  #you coudl leave the 3 numbrer out the "2".  Adding the 2 makes it onlyu print +2 to each number and skips the rest
print(numbers)

squares= []
for value in range(1,11):
    square = value**2 #this is an action you are doing to each value
    squares.append(square) #this appends each item/number in the loop
print(squares)
    #print(square) #this only retutns the value of 100.  not sure why, but its the last number in range that gets squared. maybe the value is left at 100 and skips the earliar ones since its not printing the lopped values.
print("-------------------------")
squares_1 = []
doubles_1 = []
for value in range(1,11):
    squares_1.append(value**2)  #this just simplifies squares.  you dont need to create a "square" variable
    doubles_1.append(value*2)
   # Things.append('Stuff')

print(squares_1) #make sure this is not indented or it will print out alot more lists
print(doubles_1)
#print(Things)
digits = [1,2,3,4,5,6,7]
#max(digits) 
#min(digits) 
#sum(digits)
squares = []
#list comprehensions
squares = [value**2 for value in range (1,11)]
print (squares)
print('_____________________________________')
#slicing lists
players = ['charles', 'marina', 'michael', 'florence', 'eli']
print (players[1]) #we know this one already
print (players[0:3]) #first three
print (players[1:4]) #index 1 to 3 , end before 4 and starting on 1
print (players[:4]) #1st 4
print (players[2:]) # staring at index 2 and to the end
print (players[-3:]) #last 3
#lopping a slice
for player in players[:3]: #PRINTS  at 0 to 2 stopping b4 the 3rd
    print(player.title())
#coping a list
My_fav = ['here', 'we', 'are']
Your_fav = My_fav[:] #this copies the list
My_fav.append('new one')
Your_fav.append('old one')
print ('my favorite' + str(My_fav))
print (Your_fav) #this copied and used the append for its own var diffreent than My_fav
# Tuples vs Lists.  Tuples use Parentheses instead of Brackets.  
# also Tuples are Immutable, can not be changed
dimensions = (200,45)
print(dimensions[0]) #similar to lists using the bracket for the index
dimensions_1 = [200, 45] #same result as
print(dimensions_1[0])  # above but a list
#the difference is:
#dimensions[0] = 500 #gets an error as you cant change this value
dimensions_1[0] = 500
print (dimensions_1) # here the value does now change, as it is a list and not a tuple
#looping a Tuple
#you can assign a new vaule if you make the tuple a variable
print('old numbers' + str(dimensions))
dimensions = (34, 67)
for dimension in dimensions:
    print("Here it is " + str(dimension))
#tuples for numbers that dont need to change.  lists for dynamic items
#code style pep8 guildlines 
# %%
