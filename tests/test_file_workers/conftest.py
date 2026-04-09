import pytest

cnt = 0

@pytest.fixture(autouse=True)
def clean_test_file():
    global cnt
    with open("tests/testfile.txt", "w") as f_o:
        pass
    print(cnt)
    cnt += 1