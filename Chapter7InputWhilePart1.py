# %%
#Chapter 7 User Input! and While....
#practice = input()
#print('This is my first try ' + practice)
prompt = 'some text leading up to a prompt'
response = input(prompt)
print(response)
response # returns as '21' if you ented a number i.e., 21, sees it as a string not a number
response =int(response)
response ##this results in it being a true number
