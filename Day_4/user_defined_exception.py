#creating custom exception

class Error(Exception):
    pass

class ValueNotValid(Error):
    def __str__(self):
        return "value is invalid "

a=input("Enter the number:")


if isinstance(a,str):
    raise ValueNotValid


