import pytest
from definition_d56bf9c6a01f45209ea8f7fdeb2a6ab1 import calculate_p_systemic

@pytest.mark.parametrize("h_i, beta_systemic, expected", [
    # Normal valid inputs
    (50.0, 0.1, 0.05),
    (100.0, 0.2, 0.2),
    (0.0, 0.1, 0.0),
    (75.5, 0.15, 75.5 / 100 * 0.15),
    (1.0, 1.0, 0.01),

    # Edge cases for h_i (boundary and invalid)
    (-10.0, 0.1, 0.0),            # Negative h_i treated as 0 (assumed)
    (0.0, 0.05, 0.0),            # minimum h_i = 0
    (100.0, 0.0, 0.0),           # beta_systemic = 0 means no systemic risk
    (100.0, -0.1, 0.0),          # negative beta_systemic treated as 0 (assumed)
    (150.0, 0.1, 0.15),          # h_i > 100, possible clamp or treated as is (assuming as is)
    (float('inf'), 0.1, float('inf')),  # Infinite h_i
    (50.0, float('inf'), float('inf')), # Infinite beta_systemic

    # Invalid types - expect exceptions
    ('50', 0.1, TypeError),
    (50.0, '0.1', TypeError),
    (None, 0.1, TypeError),
    (50.0, None, TypeError),

    # Boundary values for beta_systemic near 0 and 1
    (50.0, 0.0001, 50.0 / 100 * 0.0001),
    (50.0, 1.0, 0.5),
    (100.0, 1.0, 1.0),

    # Very small values for h_i and beta_systemic
    (1e-10, 1e-10, 1e-10 * 1e-10 / 100), 
])
def test_calculate_p_systemic(h_i, beta_systemic, expected):
    try:
        result = calculate_p_systemic(h_i, beta_systemic)
        if isinstance(expected, type) and issubclass(expected, Exception):
            pytest.fail(f"Expected exception {expected} but got result {result}")
        else:
            # For floating point comparison, allow small tolerance
            assert abs(result - expected) < 1e-8
    except Exception as e:
        if isinstance(expected, type) and issubclass(expected, Exception):
            assert isinstance(e, expected)
        else:
            pytest.fail(f"Unexpected exception {e} for inputs: h_i={h_i}, beta_systemic={beta_systemic}")
