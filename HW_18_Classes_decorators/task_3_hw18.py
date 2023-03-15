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


if __name__ == "__main__":
    # Converting to INT
    @TypeDecorators.to_int
    def to_integer(value):
        return value


    print(to_integer(12.6))
    print(to_integer(12))
    print(to_integer(True))
    print(to_integer(None))
    print(to_integer("String"))
    print(to_integer(["list", 1]))
    print(to_integer({"a": 23}))

    print("-" * 100)

    # Converting to FLOAT
    @TypeDecorators.to_float
    def to_float(value):
        return value


    print(to_float(99))
    print(to_float(2 / 4))
    print(to_float(False))
    print(to_float(None))
    print(to_float("String"))
    print(to_float(["list", 1]))
    print(to_float({"b": True}))

    print("-" * 100)

    # Converting to the STRING
    @TypeDecorators.to_str
    def to_string(value):
        return value

    print(to_string(657))
    print(to_string(65.7))
    print(to_string("657"))
    print(to_string("Hello"))
    print(to_string(True))
    print(to_string(None))
    print(to_string(["item", 34, None]))
    print(to_string({1, 2, 3}))
    print(to_string({"a": [1, 2, 3]}))

    print("-" * 100)

    # Converting to the BOOL
    @TypeDecorators.to_bool
    def to_boolean(value):
        return value

    print(to_boolean(True))
    print(to_boolean(0))
    print(to_boolean(112))
    print(to_boolean(33.5 / 112))
    print(to_boolean(None))
    print(to_boolean("text"))
    print(to_boolean(["list"]))
    print(to_boolean({"a": False}))
