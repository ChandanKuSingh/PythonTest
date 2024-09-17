import t
import pytest
@pytest.mark.parametrize(
    ('input_n', 'expected'),
    (
            (5,25),
            (3,9),
    )
)
def test_square_p(input_n, expected):
    assert t.square(input_n) == expected

def test_square():
    assert t.square(5) == 5