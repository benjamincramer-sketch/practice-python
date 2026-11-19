# %%
favorite_languages = {
    'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python'
     }

for name in favorite_languages.keys(): # keys() is a method, but not needed, its redundent
    print(name.title()) #loop prints each name

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends: 
        print(' Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')
##tricky code is above
# friends is a list and being searched from a loop.  
#the part with fav_food[name].title got me stuck for a bit
# with no [name], it tries to reach the whole dict. and creates a problem
# since we are looking for a name we have to call [name], the key we want to look for
#print(favorite_languages[name]), prints python. because its last?
# its because that vaule gets over written until the last one 
    if 'erin' not in favorite_languages:
        print('please take our poll') # using not
for name in sorted(favorite_languages):
    print(name.title())  #sorted list
for name in favorite_languages.values(): # values() is a method, but not needed, its redundent
    print(name.title()) #prints values out which is languages




# %%