
    #Comment. Ask user to input their name.
full_name = input("Please enter your Full Name:").capitalize()
    #Comment. Ask user to input their age.
age = input("Please enter your age:")
    #Comment. Ask user to input their house_number
house_number = input("Please enter your house number:")
    #Comment. Ask user to input their street.
town = input("Please enter your town:").capitalize()

sentence = f"Hello {full_name}, you are {age} years old and live at {house_number} {town}, we are coming to get you!"
print(sentence)

print (f"thank you for providing your details {full_name} ")