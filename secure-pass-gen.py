#Creating a secure password generator using secrets instead of random module

import secrets 
import string
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']     #defining a list of symbols
PasswordLength = int(input("Enter the length of the password required: "))
NumberOfSymbol = int(input("Enter the number of symbols you want in the password: "))
Numbers = int(input("Enter the amount of numbers you want in the password: "))

alphabet = string.ascii_letters+string.digits #define a string of alphanum

password = secrets.choice(alphabet)
for i  in range(1,PasswordLength+1):
    if NumberOfSymbol>0:    #check reuqired amount of symbols
        password += secrets.choice(symbols)
        NumberOfSymbol-=1
    elif Numbers > 0 :      #check required amount of numbers
        password += secrets.choice(string.digits)
        Numbers-=1

    else:
        password+=secrets.choice(alphabet)
#shuffle the password to the rquired length
password="".join(secrets.choice(password) for i in range (PasswordLength))

#display the password generated

print(f"The generated password is {password}")
