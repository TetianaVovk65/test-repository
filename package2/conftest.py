import pytest


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\n Start class")
    yield
    print("\n End class")


@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("\n Start function")
    yield
    print("\n End function")
