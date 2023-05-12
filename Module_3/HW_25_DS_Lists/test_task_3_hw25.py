from task_3_hw25 import QueueNode, LinkedQueue
import pytest


@pytest.fixture
def linked_queue():
    lq = LinkedQueue()
    lq.append(1)
    lq.append(2)
    lq.append(3)
    lq.append(4)
    lq.append(5)
    return lq


def test_empty_linked_queue():
    eq = LinkedQueue()
    assert eq.head is None
    assert eq.length == 0


def test_pop_empty_queue():
    with pytest.raises(AttributeError) as a:
        eq = LinkedQueue()
        eq.pop_queue()
    assert "'NoneType' object has no attribute 'next'" == str(a.value)


def test_linked_queue(linked_queue):
    assert repr(linked_queue) == "Linked Queue: 5 --> 4 --> 3 --> 2 --> 1 --> "
    assert linked_queue.head is not None
    assert linked_queue.length == 5


def test_append(linked_queue):
    assert linked_queue.append('test') is True
    assert repr(linked_queue) == "Linked Queue: test --> 5 --> 4 --> 3 --> 2 --> 1 --> "
    assert linked_queue.length == 6


def test_queue_pop(linked_queue):
    assert linked_queue.pop_queue() == 1
    assert repr(linked_queue) == "Linked Queue: 5 --> 4 --> 3 --> 2 --> "
    assert linked_queue.length == 4


def test_front_rear(linked_queue):
    assert linked_queue.front() == 5
    assert linked_queue.rear() == 1


def test_front_rear_emptry_queue():
    eq = LinkedQueue()
    with pytest.raises(AttributeError) as a:
        eq.front()
    assert "'NoneType' object has no attribute 'data'" == str(a.value)
    eq.rear() == False

