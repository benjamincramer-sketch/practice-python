# %%
# Chaper 6 Part 3
aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]: #affects only the first 3 aliens, the rest are unchanged
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]: #print first 5 , to see how the first 3 are changed
    print(alien)

print('.....')

## List into a Dict. 
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],
         }

for topping in pizza['toppings']:  #i initially did not have ticks on toppings and it was syntax error
    print(topping)
#for crust in pizza['crust']:
 #   print(crust)  ##it printed weird becuase its not a list and loope dthe word thick
 #instead this works:
print(pizza['crust'])
###
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
    }

for name, languages in favorite_languages.items(): # remember key, value so = name, language
# also .items() as a modifier, wihtout it is error = too many values to unpack
    print('\n' + name.title() + 's favorite languages are:')
    for language in languages:
        print('\t' + language.title())
#pretty straigt forward, the above code prints key and then values for each key

# %%