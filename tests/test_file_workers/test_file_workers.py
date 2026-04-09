from funcs.file_workers import read_from_file
import pytest


def create_test_data(test_data):
    test_data = ['one\n', 'two\n', 'three']
    with open("tests/testfile.txt", "a") as f_o:
        f_o.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/testfile.txt")
    
    
def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/testfile.txt")