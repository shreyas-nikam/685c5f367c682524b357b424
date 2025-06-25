import pytest
from definition_9e5f6c8be87a4625be6d785d0514319d import calculate_p_individual_systemic

@pytest.mark.parametrize("v_i_t, beta_individual, expected", [
    # Typical valid inputs
    (50.0, 0.5, 0.25),
    (100.0, 1.0, 1.0),
    (0.0, 0.0, 0.0),
    (25.5, 0.75, 0.19125),
    
    # Edge cases for v_i_t at the boundaries of possible risk scores (0 to 100)
    (0.0, 0.3, 0.0),
    (100.0, 0.3, 0.3),
    (5.0, 0.1, 0.005),
    (99.99, 0.99, 0.9899001),
    
    # Edge cases for beta_individual at boundaries (0 to 1)
    (50.0, 0.0, 0.0),
    (50.0, 1.0, 0.5),
    
    # Floating point precision cases
    (33.3333, 0.6666, 0.222197777778),
    
    # Very small floats near zero
    (1e-10, 0.5, 5e-11),
    (50.0, 1e-10, 5e-11),
    
    # Negative values (should likely raise Exception or handle gracefully)
    (-10.0, 0.5, ValueError),
    (50.0, -0.5, ValueError),
    (-1.0, -0.1, ValueError),
    
    # Values above valid range (should also raise Exception or handled gracefully)
    (150.0, 0.5, ValueError),
    (50.0, 1.5, ValueError),
    (200.0, 2.0, ValueError),
    
    # Non-float inputs (types) should raise TypeError
    ("50", 0.5, TypeError),
    (50.0, "0.5", TypeError),
    (None, 0.5, TypeError),
    (50.0, None, TypeError),
    ([50.0], 0.5, TypeError),
    (50.0, [0.5], TypeError),
])

def test_calculate_p_individual_systemic(v_i_t, beta_individual, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_p_individual_systemic(v_i_t, beta_individual)
    else:
        result = calculate_p_individual_systemic(v_i_t, beta_individual)
        # For float comparisons, allow small tolerance
        assert abs(result - expected) < 1e-7
