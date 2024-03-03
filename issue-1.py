print("Git is awesome!")

'''
pseudo code
Firstly create a name variant, that asks user to input their name.
Then create an age variant, that asks the user to input their age.
Then create a house_number variant, that asks user to input the house_number.
Then create a street variant, that asks user to input their street.
Finally print message that details all information input by user.
Example (This is {name}, they are {age} years old. They live at {house_number}{street})
'''
    #Comment. Ask user to input their name.
name = input("Please enter your name:").capitalize()
    #Comment. Ask user to input their age.
age = input("Please enter your age:")
    #Comment. Ask user to input their house_number
house_number = input("Please enter your house number:")
    #Comment. Ask user to input their street.
street = input("Please enter your street:").capitalize()

sentence = f"This is {name}, they are {age} years old. They live at {house_number} {street}"
print(sentence)
