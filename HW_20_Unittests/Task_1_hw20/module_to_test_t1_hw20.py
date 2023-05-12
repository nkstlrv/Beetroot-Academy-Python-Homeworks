class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrapper(*args):
            try:
                return f"{type(args[0])} to int = {int(args[0])}"
            except TypeError:
                return f"Type Error --> Can not convert this type to the int: {type(args[0])}"
            except ValueError:
                return f"Value Error --> Can not convert this type to the int: {type(args[0])}"
            except Exception as ex:
                raise Exception(ex)

        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args):
            try:
                return f"{type(args[0])} to float = {float(args[0])}"
            except TypeError:
                return f"Type Error --> Can not convert this type to the float: {type(args[0])}"
            except ValueError:
                return f"Value Error --> Can not convert this type to the float: {type(args[0])}"
            except Exception as ex:
                raise Exception(ex)

        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args):
            try:
                return f"{type(args[0])} to string = {str(args[0])}"
            except TypeError:
                return f"Type Error --> Can not convert this type to the string: {type(args[0])}"
            except ValueError:
                return f"Value Error --> Can not convert this type to the string: {type(args[0])}"
            except Exception as ex:
                raise Exception(ex)

        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args):
            try:
                return f"{type(args[0])} to bool = {bool(args[0])}"
            except TypeError:
                return f"Type Error --> Can not convert this type to the bool: {type(args[0])}"
            except ValueError:
                return f"Value Error --> Can not convert this type to the bool: {type(args[0])}"
            except Exception as ex:
                raise Exception(ex)

        return wrapper


# Converting to INT
@TypeDecorators.to_int
def to_integer(value):
    return value


# Converting to FLOAT
@TypeDecorators.to_float
def to_float(value):
    return value


# Converting to the STRING
@TypeDecorators.to_str
def to_string(value):
    return value


# Converting to the BOOL
@TypeDecorators.to_bool
def to_boolean(value):
    return value
