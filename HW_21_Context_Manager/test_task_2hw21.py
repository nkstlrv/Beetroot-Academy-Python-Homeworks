from task_1_hw21 import FileManager
import pytest
import os


@pytest.fixture
def create_one_line_txt():
    with FileManager("demo_1.txt", "w") as f_1:
        f_1.write("Writing to the file\n")

    demo_file = open("demo_1.txt", "r")
    yield len(demo_file.readlines())
    demo_file.close()
    os.remove("demo_1.txt")


@pytest.fixture
def create_few_lines_txt():
    with FileManager("demo_2.txt", "w") as f_2:
        f_2.write("Writing to the file\n")

    with FileManager("demo_2.txt", "a") as f_2:
        f_2.write("Writing to the file\n")

    with FileManager("demo_2.txt", "w") as f_2:
        f_2.write("Writing to the file\n")

    demo_file = open("demo_2.txt", "r")
    yield len(demo_file.readlines())
    demo_file.close()
    os.remove("demo_2.txt")


@pytest.fixture
def create_file_with_fstrings():
    with FileManager("demo_3.txt", "w") as f_3:
        f_3.write(f"{FileManager.instance_num}\n")

    with FileManager("demo_3.txt", "a") as f_3:
        f_3.write(f"{FileManager.instance_num}\n")

    with FileManager("demo_3.txt", "a") as f_3:
        f_3.write(f"{FileManager.instance_num}\n")

    with FileManager("demo_3.txt", "r") as f_3:
        last_line = f_3.readlines()[-1][0]

    yield last_line

    os.remove("demo_3.txt")


def test_open_file_count_lines_1(create_one_line_txt):
    assert create_one_line_txt == 1


def test_open_file_count_lines_2(create_few_lines_txt):
    assert create_few_lines_txt == 3


def test_check_deleted_file_context_manager_class_instances_1(create_one_line_txt):
    assert FileManager.instance_num == 1


def test_check_deleted_file_context_manager_class_instances_2(create_few_lines_txt):
    assert FileManager.instance_num == 3


def test_fstring_of_class_instances_file(create_file_with_fstrings):
    assert create_file_with_fstrings == '3'
    assert FileManager.instance_num == 4


def test_if_context_manager_can_open_and_close_file_consequentially():
    with FileManager("demo_4.txt", "w") as fw:
        fw.write('')
    file = open("demo_4.txt", "r")
    file.close()
    assert file.closed is True
    os.remove("demo_4.txt")


def test_open_non_existing_file():
    with pytest.raises(FileNotFoundError):
        FileManager.open_existing_file('demo_1.txt')
        FileManager.open_existing_file('demo_2.txt')
        FileManager.open_existing_file('demo_3.txt')
        FileManager.open_existing_file('demo_4.txt')
        FileManager.open_existing_file('filename.txt')
        FileManager.open_existing_file('something')




