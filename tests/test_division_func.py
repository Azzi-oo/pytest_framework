from funcs.utils import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result
    
# def test_division_on_more():
#     assert division(20, 2) == 10
    
# def test_division_on_two():
#     assert division(4, 2) == 2

@pytest.mark.parametrize("expected_exception, divider, divisionable",
                                                        [(ZeroDivisionError, 0, 10),
                                                         (TypeError, "1", 20)])
def test_negative_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        assert division(divisionable, divider) 

def test_type_error():
    with pytest.raises(TypeError):
        division(10, "2")
