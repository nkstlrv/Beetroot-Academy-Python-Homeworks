from  task_2_hw25 import StackNode, LinkedStack
import pytest


@pytest.fixture
def linked_stack():
    ls = LinkedStack(4)
    ls.push(1)
    ls.push(2)
    ls.push(3)
    return ls


def test_empty_linked_stack():
    es = LinkedStack(2)
    assert es.head is None
    assert es.size() == 0
    assert es.empty() is True
    with pytest.raises(AttributeError) as a:
        es.peek()
    assert  "'NoneType' object has no attribute 'data'" == str(a.value)


def test_impossible_max_length():
    with pytest.raises(ValueError) as e:
        il = LinkedStack(-1)
    assert "Max _length must be minimum (1)" == str(e.value)
    with pytest.raises(ValueError) as e:
        il = LinkedStack(0)
    assert "Max _length must be minimum (1)" == str(e.value)


def test_linked_stack(linked_stack):
    assert linked_stack.head is not None
    assert linked_stack.size() == 3
    assert linked_stack.empty() is False
    assert repr(linked_stack) == "Linked Stack: 3 --> 2 --> 1 --> "


def test_push_out_of_max_length(linked_stack):
    assert repr(linked_stack) == "Linked Stack: 3 --> 2 --> 1 --> "
    assert linked_stack.push('test_1') is True
    assert repr(linked_stack) == "Linked Stack: test_1 --> 3 --> 2 --> 1 --> "
    assert linked_stack.push('test_2') is True
    assert repr(linked_stack) == "Linked Stack: test_2 --> test_1 --> 3 --> 2 --> "
    assert linked_stack.size() == 4


def test_pull(linked_stack):
    assert linked_stack.pull() == 3
    assert repr(linked_stack) == "Linked Stack: 2 --> 1 --> "
    assert linked_stack.size() == 2


def test_pull_empty():
    es = LinkedStack(2)
    with pytest.raises(AttributeError) as a:
        es.pull()
    assert "'NoneType' object has no attribute 'next'" == str(a.value)


def test_peek(linked_stack):
    assert linked_stack.peek() == 3