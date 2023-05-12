from binary_search import  simple_binary_search
import pytest


def test_normal_search():

    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    assert simple_binary_search(lst=test_list, target=50, lo=0, hi=12) is False
    assert simple_binary_search(lst=test_list, target=-1, lo=0, hi=12) is False
    assert simple_binary_search(lst=test_list, target=7, lo=0, hi=12) == 'Index - 6, Tries - 1'
    assert simple_binary_search(lst=test_list, target=13, lo=0, hi=12) == 'Index - 12, Tries - 4'


