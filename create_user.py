import argon2

from is_it_rick import config, database
from is_it_rick.common import *
from is_it_rick.data_structures import User

print(
    'Create a new user\n' + 
    '-----------------\n')

user_name = input('Enter username: ')

# Check for duplicate username immediately to avoid making
# people enter extra details if the program is going to quit
users = database.load(config.USER_DATABASE_FILE)
existing_user = find_in_iterable(users, lambda x: x.name == user_name)
if existing_user is not None:
    print('A user already exists with that username')
    quit()

user_password = input('Enter password: ')
user_is_admin = bool(input('Enter value of "admin" (true/false): '))

user_password_hash = argon2.PasswordHasher().hash(user_password)

user = User(user_name, user_password_hash, is_admin=user_is_admin)

users.append(user)
database.save(config.USER_DATABASE_FILE, users)

print('Successfully created user')