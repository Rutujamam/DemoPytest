import pytest

class Test_004:
    @pytest.mark.group1
    def test_mul_006(self):
        a=5
        b=6
        mul = a*b
        if mul == 30:
            assert True
        else:
            assert False
