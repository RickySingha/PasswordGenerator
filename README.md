# Password Generator

The Password Generator is a command-line application built with Python that creates strong and secure passwords. This program allows users to specify the desired length and complexity of the password, ensuring that generated passwords meet their security requirements.

## How to Use

To run the Password Generator, execute the following command in your terminal:

```bash
python secure-pass-gen.py
```
## Functions
### has_symbol(s)
* Checks whether a given string contains at least one special symbol.

### Parameters:
* `s`: The string to be checked for special symbols.
### Returns:
* True if the string contains at least one special symbol, False otherwise.

## generate_password(length, number_count, special_char_count)
* Generates a random password based on specified parameters.

### Parameters:
* `length`: The length of the password to be generated.
* `number_count`: The minimum count of numbers to include in the password.
* `special_char_count`: The minimum count of special characters to include in the password.
### Returns:
* A randomly generated password that meets the specified length and complexity criteria.

## Dependencies
* `Python 3`: The Password Generator is built using Python 3.
* `secrets`: This module is used for generating cryptographically strong random numbers suitable for managing data such as passwords.
* `string` : Provides constants and functions for working with strings.
* `re`: Provides support for regular expressions. Used for checking the presence of special symbols in passwords.
