import pytest

kitchen = ["steve", "spoon", "knife"]
ids = ['word_title', 'word_upper', 'word_lower']


def get_addition(a, b):
    return a == b


def get_title_word(word):
    return word.title()


def get_upper_word(word):
    return word.upper()


def get_lower_word(word):
    return word.lower()


@pytest.mark.joint
@pytest.mark.param
@pytest.mark.parametrize("stuff", ["knife", "boots", "pan"])
def test_1(stuff):
    assert stuff in kitchen


@pytest.mark.param
@pytest.mark.parametrize("k,v", [(1, 1), (2, 2), (3, 3)])
def test_2(k, v):
    result = get_addition(k, v)
    assert result
    print(k)
    print(v)
    pass


@pytest.mark.param
@pytest.mark.parametrize('word', ['String', 'STRING', 'string'], ids=ids)
class Test3:

    def test_get_title_word(self, word):
        assert get_title_word(word) == 'String'

    def test_get_upper_word(self, word):
        assert get_upper_word(word) == 'STRING'

    def test_get_lower_word(self, word):
        assert get_lower_word(word) == 'string'
