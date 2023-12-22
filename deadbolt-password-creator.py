"""
This script is a practical tool for generating and storing extremely secure passwords.
It enhances the user experience by automatically copying the password to the clipboard
 and keeping a record of account details for future reference.
The only drawback is the file storing the secret information is not encrypted
 and can be viewed by simply opening the text file on your computer.
This is an excellent way to ensure you have your passwords if your browser failed to store them,
 and it automatically generates a very secure password so your account can't easily be hacked!
"""

# pswd chars range(33 - 126) ASCII
# special chr 33 - 47, 58 - 64, 91 - 96, 123 - 126
# numbers     48 - 57
# Upper case  65 - 90
# Lower case  97 - 122

import random as rand  # Import the random module for generating random numbers.
import clipboard as cb  # Import the clipboard module for copying text to the clipboard.
import os  # Import the os module for interacting with the operating system.

# Get the current working directory.
current_directory = os.getcwd()

# Create a new directory for storing passwords if it doesn't exist.
if not os.path.isdir(f"{current_directory}/DeadBolt/"):
    os.mkdir(f"{current_directory}/DeadBolt/")
    file = open(rf"{current_directory}/DeadBolt/Secret.txt", 'w')
    file.write(f'Accout\tUser\tPasswd')
    file.close()
    print(f'Created: {current_directory}/DeadBolt/Secret.txt')

# User input for account and user name.
acct = input('Site name: ')
user = input('User name: ')
print('Default is 32, just press enter to continue or choose custom length.')
pwd_len = input('passwd len: ')

# Set default password length.
if pwd_len == '':
    pwd_len = 32

# Initialize password string.
passwd = ''

# Generate a random password starting with special characters, numbers, uppercase and lowercase letters.
passwd += chr((rand.randint(33, 47) or rand.randint(58, 64) or rand.randint(91, 96) or rand.randint(123, 126)))
passwd += chr(rand.randint(48, 57))
passwd += chr(rand.randint(65, 90))
passwd += chr(rand.randint(97, 122))

# Fill the rest of the password length with random characters.
for _ in range(int(pwd_len) - 4):
    passwd += chr(rand.randint(33, 126))

# Copy the generated password to the clipboard.
cb.copy(passwd)
print('Password is copied to clipboard')

# Open the file for appending the new account details.
file = open(rf"{current_directory}/DeadBolt/Secret.txt", 'a')
file.write(f'\n{acct}\t{user}\t{passwd}')
file.close()

# Notify the user of the saved password.
print(rf'Password saved to {current_directory}/DeadBolt/Secret.txt')
