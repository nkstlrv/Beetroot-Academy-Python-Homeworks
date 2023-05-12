from task_1_hw25 import MyNode, LinkedList
import pytest


@pytest.fixture
def create_llsit_with_items():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    return ll


def test_empty_llsts():
    el = LinkedList()
    assert el.length == 0
    assert el.head is None


def test_append(create_llsit_with_items):
    assert create_llsit_with_items.length == 3
    create_llsit_with_items.append('test')
    assert create_llsit_with_items.length == 4
    assert repr(create_llsit_with_items) == "Linked list: test -> 3 -> 2 -> 1 -> "


def test_get_index(create_llsit_with_items):
    assert create_llsit_with_items.get_index(3) == 0
    assert create_llsit_with_items.get_index(2) == 1
    assert create_llsit_with_items.get_index(1) == 2
    assert create_llsit_with_items.get_index(33) is False


def test_pop(create_llsit_with_items):
    assert repr(create_llsit_with_items) == "Linked list: 3 -> 2 -> 1 -> "
    assert create_llsit_with_items.pop(0) == 3
    assert repr(create_llsit_with_items) == "Linked list: 2 -> 1 -> "
    assert create_llsit_with_items.pop(1) == 1
    assert repr(create_llsit_with_items) == "Linked list: 2 -> "
    assert create_llsit_with_items.pop(0) == 2
    assert repr(create_llsit_with_items) == "Linked list: "
    assert create_llsit_with_items.pop(1) == False
    assert repr(create_llsit_with_items) == "Linked list: "


def test_insert_out_of_range(create_llsit_with_items):
    assert create_llsit_with_items.insert(99, 'test') is False


def test_insert(create_llsit_with_items):
    assert create_llsit_with_items.insert(2, 'test') is True
    assert repr(create_llsit_with_items) == "Linked list: 3 -> 2 -> test -> 1 -> "
    assert create_llsit_with_items.insert(0, 'test') is True
    assert repr(create_llsit_with_items) == "Linked list: test -> 3 -> 2 -> test -> 1 -> "


def test_slice_empty_llsit():
    e_l = LinkedList()
    assert e_l.slice(0, 0) == []


def test_slice_out_of_range(create_llsit_with_items):
    with pytest.raises(IndexError) as e:
        create_llsit_with_items.slice(0, 9999)
    assert "Ending is out of range" == str(e.value)


def test_slice_start_index_after_or_equal_to_end(create_llsit_with_items):
    with pytest.raises(ValueError) as e:
        create_llsit_with_items.slice(2, 0)
    assert "Impossible slicing" == str(e.value)
    with pytest.raises(ValueError) as e:
        create_llsit_with_items.slice(2, 2)
    assert "Impossible slicing" == str(e.value)


def test_slice(create_llsit_with_items):
    assert repr(create_llsit_with_items.slice(0, 2)) == "Linked list: 3 -> 2 -> "
    assert repr(create_llsit_with_items.slice(1, 2)) == "Linked list: 2 -> "
