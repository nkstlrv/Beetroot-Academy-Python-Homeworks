from task_2_hw24 import Queue
import pytest


@pytest.fixture
def no_brackets_queue():
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    return q


@pytest.fixture
def queue_with_balanced_brackets():
    q_1 = Queue()
    q_1.append('(')
    q_1.append('(')
    q_1.append('{')
    q_1.append('}')
    q_1.append(')')
    q_1.append(')')
    q_1.append('[')
    q_1.append('1')
    q_1.append(']')
    return q_1


def test_no_brackets_queue(no_brackets_queue):
    assert no_brackets_queue.sequence == [1, 2, 3]
    no_brackets_queue.pull()
    assert no_brackets_queue.sequence == [2, 3]


def test_check_balance_no_brackets(no_brackets_queue):
    with pytest.raises(ValueError) as e:
        no_brackets_queue.check_balance()
    assert "No OPEN brackets detected" == str(e.value)

    no_brackets_queue.append('}')
    no_brackets_queue.append(')')
    no_brackets_queue.append(']')

    with pytest.raises(ValueError) as e:
        no_brackets_queue.check_balance()
    assert "No OPEN brackets detected" == str(e.value)


def test_balanced_queue(queue_with_balanced_brackets):
    assert queue_with_balanced_brackets.check_balance() == "Sequence is balanced"


def test_unbalanced_sequence_1():
    u = Queue()
    u.append('[')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
    u.append(']')
    u.append(']')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
    u.append('[')
    u.append('[')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)


def test_unbalanced_sequence_2():
    u = Queue()
    u.append('(')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
    u.append('(')
    u.append('(')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
    u.append('(')
    u.append('(')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)


def test_unbalanced_sequence_3():
    u = Queue()
    u.append('{')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
    u.append('{')
    u.append('{')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
    u.append('}')
    u.append('}')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)


def test_unbalanced_sequence_mixed_1():
    u = Queue()
    u.append(')')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert 'No OPEN brackets detected' == str(e.value)
    u.append('(')
    u.append(')')
    u.append('(')
    with pytest.raises(ValueError) as e:
        u.check_balance()
    assert "Brackets are not balances" == str(e.value)
