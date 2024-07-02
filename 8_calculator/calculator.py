from custom_exceptions import UnsupportedOperationError, IncorrectInputError


def check_if_numbers(number) -> float:
    try:
        num = float(number)
    except ValueError:
        raise IncorrectInputError
    else:
        return num


def check_operation(sign: str) -> str:
    operations = ['+', '-', '*', '/', '**']
    if sign not in operations:
        raise UnsupportedOperationError
    else:
        return sign


def calculate(num1: float, num2: float, sign: str) -> float:
    match sign:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '**':
            return num1 ** num2


if __name__ == '__main__':
    try:
        number1 = check_if_numbers(input('Enter number 1: '))
        number2 = check_if_numbers(input('Enter number 2: '))

        operation = check_operation(input('Enter operation: '))

        print(calculate(number1, number2, operation))

    except IncorrectInputError as e:
        print(e)
    except UnsupportedOperationError as e:
        print(e)
    except ZeroDivisionError as e:
        print('Division by zero!')
