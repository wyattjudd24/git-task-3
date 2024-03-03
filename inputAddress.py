
    #Comment. Ask user to input their name.
full_name = input("Please enter your Full Name:").capitalize()
    #Comment. Ask user to input their age.
age = input("Please enter your age:")
    #Comment. Ask user to input their house_number
house_number = input("Please enter your house number:")
    #Comment. Ask user to input their street.
town = input("Please enter your town:").capitalize()

sentence = f"This is {full_name}, they are {age} years old. They live at {house_number} {town}"
print(sentence)
