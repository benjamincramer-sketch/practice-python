# %%
######### Here is the IF  statement chapter ################
age = 18
age == 18 #asks is this true? returns True, but does not show now because of the code below?
if age > 17:
    print('You are getting old')
if age !=15:
    print('Not 15?') #  != Means not euwal to 
car = 'blue'
if car.title() == 'Blue':
    print(car.upper()) #does not print since 'blue' did not match 'Blue' But now it does since i added car.title, making it force to add a Captial letter in front
###
##Using a list to return a value
house_items = []
house_items = ['fork', 'book', 'hat', 'desk', 'chair']
'tv' in house_items # faluse as this is not in the list
'tv' or 'book' in house_items #returns 'tv'
#### trying not
stuff = 'tree'
if stuff not in house_items:
    print('there is not tree here')
else: 
    print('there be a tree here') #does not print as i did not add tree to that list

if len(stuff) > 6:
    print('you have enough stuff')
elif len(stuff) <18:
    print('you dont have enough stuff')
else:
    print('I guess you have exactly 3 things') ##not the best example here
##a concise example follows below
age = 12
if age < 4:
    price =0
elif age <18:
    price=5
else:
    price = 10

print('Your price is $' + str(price) + '.')
# this code saves printing to the last command and checks what hte value of price would be based on age
# you dont need a Else statment, its a general catchall, someitmes you dont want that
#in the above code:
#elif age > 18:  ##that would work better as its specific and not use the final Else
##------------##
# serires of If statments instead of block of code if you need all to pass, rather just find one true statement
if 'chair' in house_items:
    print('found chair') #needs a indent condition to work, cant just have no indent after a If statement
if 'hat' in house_items:
    print('found hat')
print('\n2 items are there')
##checks that both are true, if then else only looks for the first true and then stops
#tyring git to make a repo of my work so far
print('testing git')




# %%
