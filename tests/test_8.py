import pytest
from definition_87e25ce3b63c4cac9b0cab54ac16b423 import calculate_payout_amount

@pytest.mark.parametrize(
    "annual_salary, coverage_duration, coverage_percentage, expected",
    [
        # Nominal case: typical valid inputs
        (90000, 6, 0.25, 7500.0),
        (120000, 12, 1.0, 120000.0),
        (60000, 0, 0.5, 0.0),  # zero coverage duration
        (60000, 6, 0.0, 0.0),  # zero coverage percentage

        # Edge cases: coverage duration as 1 month and max reasonable value (e.g., 60 months)
        (50000, 1, 0.5, (50000 / 12) * 1 * 0.5),
        (50000, 60, 0.5, (50000 / 12) * 60 * 0.5),

        # Edge cases: coverage percentage very small and very large (but not exceeding 1)
        (100000, 12, 0.01, (100000 / 12) * 12 * 0.01),
        (100000, 12, 0.99, (100000 / 12) * 12 * 0.99),

        # Annual salary edge cases: very low and very high salaries
        (0.0, 12, 0.25, 0.0),
        (1.0, 12, 0.25, (1.0 / 12) * 12 * 0.25),
        (10**9, 6, 0.5, (10**9 / 12) * 6 * 0.5),

        # Floating point precision test
        (123456.78, 8, 0.33, (123456.78 / 12) * 8 * 0.33),

        # Invalid input types should raise exceptions
        pytest.param("90000", 6, 0.25, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(90000, "6", 0.25, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(90000, 6, "0.25", TypeError, marks=pytest.mark.xfail(raises=TypeError)),

        # Negative values should raise ValueError or handle gracefully
        pytest.param(-90000, 6, 0.25, ValueError, marks=pytest.mark.xfail(raises=ValueError)),
        pytest.param(90000, -6, 0.25, ValueError, marks=pytest.mark.xfail(raises=ValueError)),
        pytest.param(90000, 6, -0.25, ValueError, marks=pytest.mark.xfail(raises=ValueError)),

        # Coverage percentage > 1 or negative test
        pytest.param(90000, 6, 1.5, ValueError, marks=pytest.mark.xfail(raises=ValueError)),
        pytest.param(90000, 6, -0.1, ValueError, marks=pytest.mark.xfail(raises=ValueError)),

        # coverage_duration fractional (should be int strictly)
        pytest.param(90000, 6.5, 0.25, TypeError, marks=pytest.mark.xfail(raises=TypeError)),

        # None values
        pytest.param(None, 6, 0.25, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(90000, None, 0.25, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(90000, 6, None, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
    ],
)
def test_calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage, expected):
    try:
        result = calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage)
        # Allow for floating point rounding error tolerance
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-6
        else:
            # If expected is exception, test should fail to reach here
            pytest.fail("Expected exception but function returned result")
    except Exception as e:
        if isinstance(expected, type) and issubclass(expected, Exception):
            assert isinstance(e, expected)
        else:
            raise
