import json

users = []


def register_user() -> None:
    user_email = input('Enter your email: ')
    user_password = input('Create strong password: ')

    if not check_username(user_email):
        if check_if_the_same_password(user_password):
            users.append(dict(email=user_email, password=user_password))
    else:
        print(f'Username {user_email} already exists!')


def authenticate():
    user_email = input('Enter email: ')
    user_password = input('Enter password: ')

    if check_password(user_email, user_password):
        return user_email
    else:
        print('Check your credentials and try again!')


def check_username(email):
    for user in users:
        if user["email"] == email:
            return True
    return False


def check_if_the_same_password(password):
    rep_password = input("Please, repeat password: ")
    if password == rep_password:
        return True
    else:
        print("Passwords do not match!")
        return False


def check_password(email, password):
    for user in users:
        if user["email"] == email and user["password"] == password:
            return True
    return False


def add_age(user_email) -> None:
    user_age = input('Enter new age: ')
    for user in users:
        if user["email"] == user_email:
            user.update(age=user_age)


def update_json_file():
    with open('users.json', 'w') as json_file:
        json.dump(users, json_file, indent=4)


def get_data_from_json():
    with open('users.json', 'r') as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    users = get_data_from_json()
    while True:
        prompt = input('Welcome! If you are new here enter 1 to register, else enter 2 to login. Enter exit to close '
                       'the program. \n')

        match prompt:
            case 'exit':
                update_json_file()
                break
            case '1':
                register_user()
                continue
            case '2':
                current_user = authenticate()
                if current_user is not None:
                    while True:
                        prompt = input('Type 1 to edit your age.\nType 2 to logout of system.\nType exit to close the '
                                       'program. \n')
                        if prompt == '1':
                            add_age(current_user)
                            continue
                        if prompt == 'exit':
                            update_json_file()
                            break
                        if prompt == '2':
                            break
                        break
            case _:
                print(f'Incorrect input: {prompt}. Try again.')
                continue
