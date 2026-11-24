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

    # %%