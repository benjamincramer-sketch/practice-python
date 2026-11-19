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
#tyring git to make a repo of my work so far, hope it will work
empty_thing = [] #adding 'nothing' will make the first one print
if 'nothing' in empty_thing:
    for empty in empty_thing: # using for would be if we had multiple items and you wanted to print each one out below.  You can also do a if item = 'something' then print
        print('nothing coming right up in' + empty_thing)
else:
    print('Its empty! Theres nothing')  ##it prints here because list is empty

### This example was alluded to in teh above example.  it loops thorugh the list printing the true and hten goes to the else to print that
trial_1 = ['trial1', 'trial2', 'trial3']
for trials in trial_1:
    if trials == 'trial2':
        print ('We are just going to print: Trial1 and Trial3')
    else:
        print ('I guess we could print trial2')
print('________________')
######
### ------------ Multiple Lists ----------###
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#available could be a tuple as it wont change
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' +requested_topping + '.')
    else:
        print('SOrry, we dont have ' + requested_topping + '.')

print('\nFinished making your pizza')

# %%
