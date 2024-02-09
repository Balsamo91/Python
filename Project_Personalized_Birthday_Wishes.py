########## Starting of the program #######

# Importing module datetime so that I do not need to hardcode anything
import datetime 

print("""      
Welcome to the personalized birthday wishes card!  
To receive your card please respond to the following questions ;)
""")

# Asking for name from sender
print("What's the recipient's name? ")
name_recipient = input()

# Asking for birth Year of Recepient from sender
print("What's the recipient's year of birth? ")
year_recipient = int(input())

#  input personalized message from sender
print("Please now add your personalized message: ")
user_message = input()

# Asking sender to input Sender's name
print("Please now add your name as the sender: ")
name_sender = input()

# From the module I only import the year as date alone will be using also month and day.
# By doing this we avoid "hardcoding" using a static year and then having the code obsolate 
# example ---> age = 2024 - year_recipient
current_year = datetime.date.today().year

# Made a variable in which we substract the current year with user input
age = current_year - year_recipient

# Printing the card using the variables to fill the spots
print(f"""
{name_recipient}, let's celebrate your {age} years of awesomeness!
Wishing you a day filled with joy and laughter as you turn {age}!

{user_message}

With love and best wishes,
{name_sender}
""")