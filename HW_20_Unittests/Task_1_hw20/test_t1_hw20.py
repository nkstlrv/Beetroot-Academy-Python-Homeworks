from module_to_test_t1_hw20 import to_integer, to_float, to_boolean, to_string, TypeDecorators



def test_to_integer():
    assert to_integer(12.6) == "<class 'float'> to int = 12"
    assert to_integer(12) == "<class 'int'> to int = 12"
    assert to_integer(True) == "<class 'bool'> to int = 1"
    assert to_integer(None) == "Type Error --> Can not convert this type to the int: <class 'NoneType'>"
    assert to_integer("1233.55") == "Value Error --> Can not convert this type to the int: <class 'str'>"
    assert to_integer(['list']) == "Type Error --> Can not convert this type to the int: <class 'list'>"
    assert to_integer({'dicr': 12}) == "Type Error --> Can not convert this type to the int: <class 'dict'>"
    assert to_integer(TypeDecorators) == "Type Error --> Can not convert this type to the int: <class 'type'>"


def test_to_float():
    assert to_float(12.6) == "<class 'float'> to float = 12.6"
    assert to_float(12) == "<class 'int'> to float = 12.0"
    assert to_float(4/8) == "<class 'float'> to float = 0.5"
    assert to_float(False) == "<class 'bool'> to float = 0.0"
    assert to_float(None) == "Type Error --> Can not convert this type to the float: <class 'NoneType'>"
    assert to_float(['list', 1, 2]) == "Type Error --> Can not convert this type to the float: <class 'list'>"
    assert to_float({'dicr': 12}) == "Type Error --> Can not convert this type to the float: <class 'dict'>"
    assert to_float(TypeDecorators) == "Type Error --> Can not convert this type to the float: <class 'type'>"


def test_to_string():
    assert to_string(12.6) == "<class 'float'> to string = 12.6"
    assert to_string(0) == "<class 'int'> to string = 0"
    assert to_string(True) == "<class 'bool'> to string = True"
    assert to_string(None) == "<class 'NoneType'> to string = None"
    assert to_string("String") == "<class 'str'> to string = String"
    assert to_string(['list']) == "<class 'list'> to string = ['list']"
    assert to_string({'a': 'b'}) == "<class 'dict'> to string = {'a': 'b'}"
    assert to_string({1, 2, 3}) == "<class 'set'> to string = {1, 2, 3}"
    assert to_string(TypeDecorators) == "<class 'type'> to string = <class 'module_to_test_t1_hw20.TypeDecorators'>"


def test_to_bool():
    assert to_boolean(True) == "<class 'bool'> to bool = True"
    assert to_boolean(False) == "<class 'bool'> to bool = False"
    assert to_boolean(1) == "<class 'int'> to bool = True"
    assert to_boolean(0) == "<class 'int'> to bool = False"
    assert to_boolean(23.66) == "<class 'float'> to bool = True"
    assert to_boolean(0.0) == "<class 'float'> to bool = False"
    assert to_boolean([1, 2, 3]) == "<class 'list'> to bool = True"
    assert to_boolean({'a': 2}) == "<class 'dict'> to bool = True"
    assert to_boolean({1, 2, 3}) == "<class 'set'> to bool = True"
    assert to_boolean(TypeDecorators) == "<class 'type'> to bool = True"

