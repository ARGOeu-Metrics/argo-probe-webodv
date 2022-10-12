class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


class WarningException(MyException):
    def __str__(self):
        return str(self.msg)


class CriticalException(MyException):
    def __str__(self):
        return str(self.msg)
