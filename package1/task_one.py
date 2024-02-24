import pytest


class Test_Page:

    @pytest.mark.from_class
    def test_1(self):
        print('\ntest1')
        pass

    @pytest.mark.from_class
    def test_2(self):
        print('\ntest2')
        pass

    @pytest.mark.from_class
    def test_test3(self):
        print('\ntest3')
        pass

    @pytest.mark.from_class
    def test_4(self):
        print('\ntest4')
        pass

    @pytest.mark.from_class
    def test_5(self):
        print('\ntest5')
        pass
