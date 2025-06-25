import pytest
from definition_4f77d5fce9034598b104ab553d13d2ab import calculate_idiosyncratic_risk

@pytest.mark.parametrize("fhc, fcr, fus, w_cr, w_us, expected", [
    # Typical valid inputs with normal weights
    # Using example from spec: Alex Chen scenario
    (1.262, 0.95, 1.0, 0.4, 0.6, 61.85),
    # Alex's new FUS = 0.65 example
    (1.262, 0.95, 0.65, 0.4, 0.6, 48.6),
    # Brenda's example (Research Scientist)
    (0.3*0.85*0.9*0.95* (1 - 0.015*20), 1.0, 1.0, 0.4, 0.6, 9.6),

    # Edge cases for weights and factors
    # Minimum weights and factors (lowest values)
    (0.0, 0.0, 0.0, 0.0, 0.0, 5.0),
    # Weights sum to less than 1 (should work anyway)
    (1.0, 0.5, 0.5, 0.1, 0.1, 25.0),  # raw = 1.0*(0.1*0.5+0.1*0.5)=0.1, scaled: 5.0 (min floor)

    # Weights sum to more than 1
    (2.0, 1.0, 1.0, 1.0, 1.0, 100.0),  # raw=2*(1*1 + 1*1) =4 -> cap at 100

    # Raw score exactly on lower bound for normalization (0.1 raw)
    (0.2, 0.0, 0.0, 0.4, 0.6, 5.0),  # raw=0.2*(0 + 0)=0 but minimum threshold after scale is 5.0
    # Raw score exactly on upper bound for normalization (2.0 raw)
    (2.0, 1.0, 1.0, 0.4, 0.6, 100.0), 

    # Floating point precision check
    (1.0, 0.3333333, 0.6666667, 0.4, 0.6, 50.0),

    # Very large factors to trigger upper bound cap
    (10.0, 5.0, 5.0, 0.4, 0.6, 100.0),

    # Negative factors - expecting function to handle or raise exception
    (1.0, -0.5, 0.5, 0.4, 0.6, 5.0),  # negative fcr treated in formula, expected floor 5.0

])
def test_calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us, expected):
    try:
        result = calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us)
        if isinstance(expected, float):
            # Allow small floating tolerance
            assert abs(result - expected) < 0.05
        else:
            # If expected is exception class, we should fail here since we got a result
            pytest.fail(f"Expected exception {expected} but got result {result}")
    except Exception as e:
        if isinstance(expected, type) and issubclass(expected, Exception):
            assert isinstance(e, expected)
        else:
            # Unexpected exception
            raise

@pytest.mark.parametrize("inputs", [
    # Testing non-numeric inputs
    ('a', 0.5, 0.5, 0.4, 0.6),
    (1.0, 'b', 0.5, 0.4, 0.6),
    (1.0, 0.5, 'c', 0.4, 0.6),
    (1.0, 0.5, 0.5, 'd', 0.6),
    (1.0, 0.5, 0.5, 0.4, 'e'),
    # Mixed None types
    (None, 0.5, 0.5, 0.4, 0.6),
    (1.0, None, 0.5, 0.4, 0.6),
    (1.0, 0.5, None, 0.4, 0.6),
    (1.0, 0.5, 0.5, None, 0.6),
    (1.0, 0.5, 0.5, 0.4, None),
])
def test_calculate_idiosyncratic_risk_invalid_inputs(inputs):
    fhc, fcr, fus, w_cr, w_us = inputs
    with pytest.raises((TypeError, ValueError)):
        calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us)

@pytest.mark.parametrize("fhc, fcr, fus, w_cr, w_us", [
    # Weights are negative
    (1.0, 0.5, 0.5, -0.4, 0.6),
    (1.0, 0.5, 0.5, 0.4, -0.6),
    (1.0, 0.5, 0.5, -1.0, -0.5),
])
def test_calculate_idiosyncratic_risk_negative_weights(fhc, fcr, fus, w_cr, w_us):
    # Depending on implementation, might raise or allow
    # Here we expect it to not raise error but output normalized value at least 5.0
    result = calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us)
    assert result >= 5.0 and result <= 100.0

@pytest.mark.parametrize("fhc, fcr, fus, w_cr, w_us", [
    # All zeros for factors and weights
    (0.0, 0.0, 0.0, 0.0, 0.0),

    # Very large weights
    (1.0, 1.0, 1.0, 10.0, 10.0),

    # Weights sum to zero but factors positive
    (1.0, 1.0, 1.0, 0.0, 0.0),
])
def test_calculate_idiosyncratic_risk_variants(fhc, fcr, fus, w_cr, w_us):
    result = calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us)
    assert isinstance(result, float)
    assert 5.0 <= result <= 100.0

