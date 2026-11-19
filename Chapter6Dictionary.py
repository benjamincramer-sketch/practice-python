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

