from task_1_hw24 import MyStack
import pytest


@pytest.fixture
def create_stack_max_vals():
    s_4 = MyStack(3)
    s_4.my_push(1)
    s_4.my_push(2)
    s_4.my_push(3)
    return s_4


@pytest.fixture
def create_reverse_stack_of_max_values():
    s_3 = MyStack(3)
    s_3.my_reverse_push('a')
    s_3.my_reverse_push('b')
    s_3.my_reverse_push('c')
    return s_3


def test_class_without_arguments():
    with pytest.raises(TypeError) as ex_info:
        empty_class = MyStack()
    assert "MyStack.__init__() missing 1 required positional argument: 'max_len'" == str(ex_info.value)


def test_is_empty():
    e_1 = MyStack(1)
    assert e_1.my_is_empty() is True


def test_not_empty():
    e_2 = MyStack(1)
    e_2.my_push('something')
    assert e_2.my_is_empty() is False


# Tests for usual stack
def test_pull_from_empty_list():
    s_1 = MyStack(1)
    with pytest.raises(IndexError) as ex_info:
        s_1.my_pull()
    assert "pop from empty list" == str(ex_info.value)


def test_push(create_stack_max_vals):
    assert create_stack_max_vals.stack == [1, 2, 3]


def test_pull(create_stack_max_vals):
    create_stack_max_vals.my_pull()
    assert create_stack_max_vals.stack == [1, 2]


def test_push_over_max_values(create_stack_max_vals):
    create_stack_max_vals.my_push('test')
    assert create_stack_max_vals.stack == [2, 3, 'test']


# Tests for the reversed stack
def test_reverse_pull_from_empty_list():
    s_2 = MyStack(1)
    with pytest.raises(IndexError) as ex_info:
        s_2.my_reverse_pull()
    assert "pop from empty list" == str(ex_info.value)


def test_reverse_push(create_stack_of_max_values):
    assert create_reverse_stack_of_max_values.stack == ['c', 'b', 'a']


def test_reverse_pull(create_stack_of_max_values):
    create_reverse_stack_of_max_values.my_reverse_pull()
    assert create_reverse_stack_of_max_values.stack == ['b', 'a']


def test_reverse_push_over_max_values(create_stack_of_max_values):
    create_reverse_stack_of_max_values.my_reverse_push('test')
    assert create_reverse_stack_of_max_values.stack == ['test', 'c', 'b']
