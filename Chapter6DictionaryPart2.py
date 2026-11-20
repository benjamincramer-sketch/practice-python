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
    print(name.title())  #sorted list, you sort the vairble in above line, not sort at print
for name in favorite_languages.values(): # values() is a method, but not needed, its redundent
    print('this is the values = ' + name.title()) #prints values out which is languages
#####
favorite_languages = {}
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title()) ## Set() pulls out duplicates
print("---------------------")
###Nesting, lists in dict and dict in lists 
alienz_0 = {}
alienz_1 = {}
alienz_2 = {}
alienzs = [alienz_0, alienz_1, alienz_2]
for alien in alienzs:
    print(alien) #prints empty brackets, didnt add anything in them to save time
## fleet of aliens
alienzs = [] # ended up defining this as empty anyway to be added by the following code
for alien_number in range(30): #makes 30 aliens, each with a key value
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alienzs.append(new_alien)
###
for alien in alienzs[:5]:
    print(alien)
    print('Total number of aliens: ' + str(len(alienzs)) )
#print(alienzs) shows how each alien is added into a list


# %%