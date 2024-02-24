import pytest


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\n Start class")
    yield
    print("\n End class")
