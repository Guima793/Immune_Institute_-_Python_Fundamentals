#This program takes a list of names and ages.
# At the end of the program, sorts and prints out the names and their respective ages sortted from oldest to youngest.

# In this program, the values entered are supposed to refer to a ship's crewlist.

crewlist = dict() # We degine an empty dictionary

print("Enter * as the value for the name to exit the program.") #We tell the user how to stop entering values.

while True: #We start a loop.

    name = input('Enter your name: ') # We ask the user for a nanme.

    if name == "*": #If the name is equal to the exit character, the program exits the loop.
        break
    else:
        while True: #We anter a segond loop which asks the user for an age and ensures that the age is a usable value.
            age = input('Enter your age: ')
            try:
                age = int(age)
            except ValueError:
               print('Please enter a whole number.')
            else:
                break
        crewlist[name]=age #We add the new key:value pair to the dictionary and go back to the top fo the loop.

crewlist = sorted(crewlist.items(), key = lambda x:x[1], reverse = True) #We sort our dictionary in descending order according to it s values.

print(crewlist) #We print the dictionary