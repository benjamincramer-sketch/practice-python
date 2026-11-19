# %%
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print('the alien is ' + alien_0['color'])
alien_0['color'] = 'yellow'
print('the alien is now ' + alien_0['color'])
print('------------------')
## my first loop attempt,  it only prints the category
for alien in alien_0:
    print(alien)
print('----------------------')
new_color = alien_0['color']  #assigning a vairalbe to the item in dict.
print(new_color)
print('-------------')
alien_1 = {} # the empty braces
alien_1['color'] = 'green'
alien_1['points'] = 5 
print (alien_1)
### adding to a dict. that already has info in it. like appending a list
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['speed'] = 'medium'
if alien_0['speed'] == 'slow':
    x_increment = 1
if alien_0['speed'] == 'medium':
    x_increment = 2
if alien_0['speed'] == 'fast':
    x_increment = 3
print ('Original x position ' + str(alien_0['x_position']))
## positional logic
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))
###side thing, not related
for number in range(1,10):
    number += 1
    if number == 8:
        print(number)
#### 
print('==================')
categories_trial = {
    'rob': 'apple',
    'sue': 'grape',
    'harry': 'orange',
    'cal': 'plumb'
    }
print(categories_trial)
print(categories_trial['rob'].title())
###User name /passowrd loops
user_0 = {
    'username':'crambj',
    'first': 'ben',
    'last': 'cramer'
    }
for key, value in user_0.items(): #.items() is a method
    print('\nKey: ' + key)
    print('Value: ' + value)
for k, v in categories_trial.items():
    print('\nPerson: ' + k)
    print('Fruit: ' + v)



# %%