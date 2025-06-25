import pytest
from definition_8bb356cf313e497db4b624c51a2e4cdd import calculate_expected_loss

@pytest.mark.parametrize("p_claim, lpayout, expected", [
    # Normal cases
    (0.0, 0.0, 0.0),                              # zero probability, zero payout
    (0.0, 10000.0, 0.0),                         # zero probability, positive payout
    (0.5, 0.0, 0.0),                             # positive probability, zero payout
    (1.0, 10000.0, 10000.0),                     # probability 1, positive payout
    (0.25, 40000.0, 10000.0),                    # fractional probability, payout

    # Edge values on boundaries
    (1e-12, 1e-12, 1e-24),                       # very small floating values
    (1.0, 1e-12, 1e-12),                         # max probability, very small payout
    (1e-12, 1.0, 1e-12),                         # very small probability, payout =1
    (0.999999999999, 999999.999999, 999999.0),  # probability very close to 1, large payout

    # Larger values
    (0.7, 1000000.0, 700000.0),
    (0.333, 30000.0, 9990.0),

    # Invalid input types and values, expecting exceptions
    (-0.1, 10000.0, ValueError),                  # negative probability invalid
    (1.1, 10000.0, ValueError),                   # probability >1 invalid
    (0.5, -10000.0, ValueError),                  # negative payout invalid
    ('0.5', 10000.0, TypeError),                   # string instead of float probability
    (0.5, '10000', TypeError),                     # string instead of float payout
    (None, 10000.0, TypeError),                    # None instead of probability
    (0.5, None, TypeError),                         # None instead of payout
    ([0.5], 10000.0, TypeError),                   # list instead of float probability
    (0.5, [10000.0], TypeError),                   # list instead of float payout
])
def test_calculate_expected_loss(p_claim, lpayout, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_expected_loss(p_claim, lpayout)
    else:
        result = calculate_expected_loss(p_claim, lpayout)
        assert isinstance(result, float)
        # Allow a small floating point tolerance
        assert abs(result - expected) < 1e-6
