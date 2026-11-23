# %%
#Chapter 7 User Input! and While....
#practice = input()
#print('This is my first try ' + practice)
prompt = 'your age? '
response = input(prompt)

print(response)
response # returns as '21' if you ented a number i.e., 21, sees it as a string not a number
response =int(response)
response ##this results in it being a true number
if response <= 21:
    print('you are younger than 22')
elif response >= 22:
    print('you are 22 or older')


prompt_1 = 'How about a never ending script? if you had enough, just type quit '
inquiry = " " # if this is not here, the loop does not work
while inquiry != 'quit':
    inquiry = input(prompt_1)
    #print(inquiry) lets it print quit which i dont want
if inquiry != 'quit':
    print(inquiry) #prints everythign except quit
    
#________________
prompt = "3rd times a charm " 
active = True
while active:  #while active is true will keep the loop
    message = input(prompt)

    if message == 'quit':
       active = False  ## the falise make the while loop end
    else: 
        print(message) # keeps the loop going, not need the  "" like above code
    #this is more concise than above code, also only pirnts all but quit
# ---- break  and continue  ---------



# %%