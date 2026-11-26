# %%
# Chapter7BreakContinuePart2
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print ("I'd love to go to " + city.title() + "!")
        ##this loops until you type quit, much faster to write 
        #the prevoius part1 code.  Dont have to use a flag.
        #dont need a "" to start it off, etc.  

##Continue loops
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

####lists dictionaries
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(' veryfiying' + current_user.title())
    confirmed_users.append(current_user)
print('confirmed')

for confirmed_user in confirmed_users:
      
    print(confirmed_user.title())

##using  a flag and Dictionary
responses = {}

polling_active = True

while polling_active:
    name = input("whats your name?")
    response = input("which montain?")

    responses[name] = response

    repeat = input("yes or no")
    if repeat == 'no':
        polling_active = False

    print("Results")
    for name, response in responses.items():
        print(name + " would like " + response)
###loops with active flag unitl 'no'.  variabel = input("text")



    # %%
