import pytest
from definition_f2b07704afde4f99acda7abf74703d3f import calculate_fexp

@pytest.mark.parametrize("years_experience, expected", [
    (0, 1.0),                        # zero experience, no decay
    (5, 1 - 0.015 * 5),             # positive integer experience
    (10.5, 1 - 0.015 * 10.5),       # positive float experience
    (20, 1 - 0.015 * 20),           # at capping threshold
    (25, 1 - 0.015 * 20),           # above cap: capped at 20
    (100, 1 - 0.015 * 20),          # large number well above cap
    (-1, 1.0),                      # negative experience: treat as 0 or max?
    (-5, 1.0),                      # negative float experience
    (None, TypeError),              # None input type error
    ("10", TypeError),              # string instead of numeric
    ([], TypeError),                # list instead of numeric
    ({}, TypeError),                # dict instead of numeric
    (float('inf'), 1 - 0.015 * 20),# infinite input capped
    (float('-inf'), TypeError),     # negative infinite input error
    (float('nan'), TypeError),      # NaN input error
])
def test_calculate_fexp(years_experience, expected):
    # We handle exceptions expected
    try:
        result = calculate_fexp(years_experience)
        # For floats, allow small diff
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-9
        else:
            assert result == expected
    except Exception as e:
        assert isinstance(e, expected)
