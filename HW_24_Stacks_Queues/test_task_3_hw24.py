from task_3_hw24 import MyExtendedStack, MyQueue
import pytest


# Testing the Stack

@pytest.fixture
def create_stack():
    s = MyExtendedStack(5)
    s.my_push(1)
    s.my_push(2)
    s.my_push(3)
    s.my_push(4)
    s.my_push(5)
    return s


def test_get_nonexisting_element_from_stack(create_stack):
    assert create_stack.stack == [1, 2, 3, 4, 5]
    with pytest.raises(ValueError) as e:
        create_stack.get_from_stack('test')
    assert "No given item in stack" == str(e.value)


def test_get_element_from_stack(create_stack):
    assert create_stack.get_from_stack(3) == 3
    assert create_stack.stack == [1, 2, 4, 5]


def test_get_element_from_stack_if_there_are_more_than_one_instance_of_it(create_stack):
    create_stack.my_push('test')
    create_stack.my_push('test')
    create_stack.my_push('test')
    assert create_stack.stack == [4, 5, 'test', 'test', 'test']
    assert create_stack.get_from_stack('test') == 'test'
    assert create_stack.stack == [4, 5]


# Testing Queue

@pytest.fixture
def create_queue():
    q = MyQueue()
    q.my_append('h')
    q.my_append('e')
    q.my_append('l')
    q.my_append('l')
    q.my_append('o')
    return q


def test_get_nonexisting_element_from_queue(create_queue):
    assert create_queue.queue == ['h', 'e', 'l', 'l', 'o']
    with pytest.raises(ValueError) as e:
        create_queue.get_from_queue('test')
    assert "No given item in queue" == str(e.value)


def test_get_element_from_queue(create_queue):
    assert create_queue.get_from_queue('e') == 'e'
    assert create_queue.queue == ['h', 'l', 'l', 'o']


def test_get_element_from_queue_if_there_are_more_than_one_instance_of_it(create_queue):
    assert create_queue.get_from_queue('l') == 'l'
    assert create_queue.queue == ['h', 'e', 'o']
