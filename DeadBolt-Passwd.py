import random as rand
import clipboard as cb
import os

# pswd chars range(33 - 126) ASCII
# special chr 33 - 47, 58 - 64, 91 - 96, 123 - 126
# numbers     48 - 57
# Upper case  65 - 90
# Lower case  97 - 122

name = os.environ['USERPROFILE']

if not os.path.isdir(f"{name}\\DeadBolt\\"):
    os.mkdir(f"{name}\\DeadBolt\\")
    print(f'Created: {name}\\DeadBolt\\')
if not os.path.isdir(f"{name}\\DeadBolt\\Passwd\\"):
    os.mkdir(f"{name}\\DeadBolt\\Passwd\\")
    print(f'Created: {name}\\DeadBolt\\Passwd\\')


Acct = input('Site name: ')
user = input('User name: ')
print('Default is 128, Just press enter to continue or choose new length then enter')
pwdL = input('pswd len: ')

if pwdL == '':
    pwdL = 128

pswd = ''

pswd += chr((rand.randint(33, 47) or rand.randint(58, 64) or rand.randint(91, 96) or rand.randint(123, 126)))
pswd += chr(rand.randint(48, 57))
pswd += chr(rand.randint(65, 90))
pswd += chr(rand.randint(97, 122))

for _ in range(int(pwdL) - 4):
    pswd += chr(rand.randint(33, 126))

cb.copy(pswd)
print('PSWD copied to clipboard')
exit()

file = open(rf"{name}\DeadBolt\Passwd\{Acct}-{user}.txt", 'w')
file.write(pswd)
file.close()

print(rf'PSWD saved to {name}\DeadBolt\Passwd\{Acct}-{user}.txt')
