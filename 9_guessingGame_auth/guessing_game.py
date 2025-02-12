from random import randint


def get_range():
    num1, num2 = input('Enter min: '), input('Enter max: ')
    if check_user_input(num1) and check_user_input(num2):
        num1 = int(num1)
        num2 = int(num2)
        if 5 > len(range(num1, num2)) or len(range(num1, num2)) > 30:
            print('Enter valid range!')
        else:
            return num1, num2
    else:
        print('Input should be a number!')


def check_user_input(number: str) -> bool:
    return True if number.isdigit() else False


def hidden_numbers(start: int, end: int) -> list:
    numbers = set()
    while len(numbers) < 3:
        numbers.add(randint(start, end))
    return list(numbers)


def user_numbers() -> list:
    result = []
    for i in range(1, 4):
        result.append(input(f'Enter {i} number or type exit to finish the game: '))
        if 'exit' in result:
            break
    return result


def is_winner(hidden_num: list, user_num: list) -> int:
    correct_counter = 0
    for i in range(len(user_num)):
        for j in range(len(hidden_num)):
            if int(user_num[i]) == hidden_num[j]:
                correct_counter += 1
    return correct_counter


def main() -> None:
    while True:
        user_range = get_range()
        if user_range is not None:
            num1, num2 = user_range
            hidden = hidden_numbers(num1, num2)
            while True:
                usernum = user_numbers()
                if 'exit' in usernum:
                    break
                if is_winner(hidden, usernum) == 3:
                    print('You win!')
                    break
                else:
                    print(f'{is_winner(hidden, usernum)} numbers are correct. Try again.')
            break


if __name__ == '__main__':
    main()
