import json

#TODO I still need rewrite file using JSON nd make corrections according to task specification.
users = {}


def register_user():
    name = input('Think of your username: ')
    pw = input('Create strong password: ')

    if not check_username(name):
        users[name] = pw
    else:
        print(f'Username {name} already exists!')


def authenticate():
    name = input('Enter username: ')
    pw = input('Enter password: ')

    if check_username(name) and check_password(name, pw):
        return True
    else:
        print('Check your credentials and try again!')


def check_username(name):
    if name in users:
        return True


def check_password(name, pw):
    if pw == users[name]:
        return True


def print_to_file():
    file = open('users.txt', 'w')
    for user, pw in users.items():
        print(user, pw, file=file)


if __name__ == '__main__':
    while True:
        prompt = input('Welcome! If you are new here enter 1 to register, else enter 2 to login. Enter exit to close '
                       'the program. \n')

        match prompt:
            case 'exit':
                print_to_file()
                break
            case '1':
                register_user()
                continue
            case '2':
                authenticate()
                while True:
                    prompt = input('Type 1 to edit your age.\nType 2 to logout of system.\nType exit to close the '
                                   'program. \n')
                    if prompt == '1':
                        age = input('Enter new age: ')
                        continue
                    if prompt == 'exit':
                        print_to_file()
                        break
                    if prompt == '2':
                        break
                    break
            case _:
                print(f'Incorrect input: {prompt}. Try again.')
                continue
