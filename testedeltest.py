# Starting of the program
print("""      
Welcome to the personalized birthday wishes card!  
To receive your card please respond to the following questions ;)""")

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

# I have decided to do it hardcoded but to make it more 
age = 2024 - year_recipient

# Printing the card
print(f"""
{name_recipient}, let's celebrate your {age} years of awesomeness!
Wishing you a day filled with joy and laughter as you turn {age}!

{user_message}

With love and best wishes,
{name_sender}
""")