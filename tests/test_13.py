import pytest
from definition_0b6a6dab9f944d78b3c3195bd5ba4de2 import calculate_monthly_premium

@pytest.mark.parametrize(
    "expected_loss, loading_factor, min_premium, expected",
    [
        # Normal case: expected_loss positive, loading_factor positive, min_premium positive
        (1200.0, 1.5, 20.0, max((1200.0 * 1.5) / 12, 20.0)),
        
        # Case where calculated premium is below min_premium
        (100.0, 1.0, 15.0, 15.0),
        
        # Case where calculated premium equals min_premium exactly
        (160.0, 1.5, (160.0 * 1.5) / 12, (160.0 * 1.5) / 12),

        # Zero expected loss -> should floor to min_premium
        (0.0, 2.0, 25.0, 25.0),

        # Zero loading factor, should result in min_premium since the premium is zero
        (500.0, 0.0, 30.0, 30.0),

        # Negative expected loss (should this be handled gracefully?)
        # Assuming function raises ValueError or returns min_premium
        (-100.0, 1.0, 20.0, 20.0),

        # Negative loading factor (invalid, expecting ValueError)
        pytest.param(1000.0, -1.0, 20.0, ValueError, marks=pytest.mark.xfail(raises=ValueError)),

        # Negative min_premium (invalid, expecting ValueError)
        pytest.param(1000.0, 1.0, -20.0, ValueError, marks=pytest.mark.xfail(raises=ValueError)),

        # Very large numbers to test overflow/scaling
        (1e9, 2.0, 1000.0, max((1e9 * 2.0)/12, 1000.0)),

        # Floating point numbers with decimals
        (1234.56, 1.234, 50.5, max((1234.56 * 1.234) / 12, 50.5)),

        # Minimal positive values (close to zero but positive)
        (1e-10, 1e-10, 0.01, 0.01),

        # Minimal positive min_premium just above zero
        (10.0, 1.0, 0.001, max((10.0 * 1.0)/12, 0.001)),
    ],
)
def test_calculate_monthly_premium(expected_loss, loading_factor, min_premium, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_monthly_premium(expected_loss, loading_factor, min_premium)
    else:
        result = calculate_monthly_premium(expected_loss, loading_factor, min_premium)
        assert isinstance(result, float), "Result should be a float"
        assert result >= min_premium, f"Result {result} is less than min_premium {min_premium}"
        assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"
