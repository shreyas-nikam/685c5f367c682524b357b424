import pytest
from definition_afc255540dec41fb8d1a278df4a3829e import calculate_p_claim

@pytest.mark.parametrize("p_systemic, p_individual_systemic, expected", [
    # Typical valid inputs
    (0.1, 0.5, 0.05),           # Normal probabilities, expected product
    (0.0, 0.5, 0.0),            # Zero systemic probability
    (0.1, 0.0, 0.0),            # Zero individual probability
    (0.0, 0.0, 0.0),            # Both zero

    # Boundary values at edges of valid probability domain
    (1.0, 1.0, 1.0),            # Both max probability
    (1.0, 0.0, 0.0),            # One max, one zero
    (0.0, 1.0, 0.0),

    # Very small probabilities close to zero but valid
    (1e-10, 1e-10, 1e-20),

    # Probabilities slightly above 1 - expect behavior (assuming domain check or no domain check)
    (1.1, 0.5, 0.55),
    (0.5, 1.1, 0.55),
    (1.1, 1.1, 1.21),

    # Negative inputs - should normally raise error or handle gracefully
    (-0.1, 0.5, ValueError),
    (0.5, -0.1, ValueError),
    (-0.1, -0.1, ValueError),

    # Non-numeric types - should raise TypeError or ValueError
    ("0.1", 0.5, TypeError),
    (0.5, "0.1", TypeError),
    (None, 0.5, TypeError),
    (0.5, None, TypeError),

    # Completely invalid types
    ([], 0.5, TypeError),
    (0.1, {}, TypeError),
    (object(), 0.5, TypeError),

    # Extremely large numbers (float('inf'))
    (float('inf'), 0.5, ValueError),
    (0.5, float('inf'), ValueError),
    (float('inf'), float('inf'), ValueError),

    # NaN inputs
    (float('nan'), 0.5, ValueError),
    (0.5, float('nan'), ValueError),

])
def test_calculate_p_claim(p_systemic, p_individual_systemic, expected):
    try:
        result = calculate_p_claim(p_systemic, p_individual_systemic)
        if isinstance(expected, type) and issubclass(expected, Exception):
            pytest.fail(f"Expected exception {expected} but got result {result}")
        else:
            # For floating point comparisons allow small tolerance
            assert abs(result - expected) < 1e-12
    except Exception as e:
        if not (isinstance(expected, type) and issubclass(expected, Exception)):
            pytest.fail(f"Unexpected exception {type(e)}: {e}")
        else:
            assert isinstance(e, expected)
