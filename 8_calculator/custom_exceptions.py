class UnsupportedOperationError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if not self.message:
            return 'Entered operation is not supported!'


class IncorrectInputError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if not self.message:
            return 'Incorrect type of input! Please, use numbers only.'
