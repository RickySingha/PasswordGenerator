import secrets
import string
import re
alphabet = string.ascii_letters + string.digits + string.punctuation
#function to chheck special symbols
def has_symbol(s):
    pattern = re.compile(r'[' + re.escape(string.punctuation) + ']')
    # Use search to find if any symbol matches the pattern
    return bool(pattern.search(s))


#function to generate the password
def generate_password(length,number_count,special_char_count):
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (sum(c.isdigit() for c in password) >=number_count and sum(has_symbol(c) for c in password) >= special_char_count):
           return password
    


if __name__ == '__main__':
    length = int(input("Enter the length of the password: "))
    number_count = int(input("Enter the count of numbers you want in the password: "))
    special_char_count = int(input("Enter the count of special symbols you want: "))

    password = generate_password(length,number_count,special_char_count)

    print(f'The generarted password is : {password}')