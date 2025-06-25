import pytest
from definition_fe5454e73fbb4625a14314edd2f6adb3 import calculate_systematic_risk

@pytest.mark.parametrize(
    "h_base_t, m_econ, i_ai, w_econ, w_inno, expected",
    [
        # Normal valid inputs with typical weights summing to 1
        (65.0, 1.0, 1.0, 0.5, 0.5, 65.0),
        (30.0, 1.0, 1.0, 0.5, 0.5, 30.0),

        # Economic climate modifier and AI innovation index at extremes
        (50.0, 0.8, 0.8, 0.5, 0.5, 50.0 * (0.5 * 0.8 + 0.5 * 0.8)),
        (80.0, 1.2, 1.2, 0.5, 0.5, 80.0 * (0.5 * 1.2 + 0.5 * 1.2)),

        # Weights zeroing one factor
        (40.0, 1.0, 2.0, 1.0, 0.0, 40.0 * (1.0 * 1.0 + 0.0 * 2.0)),
        (40.0, 1.0, 2.0, 0.0, 1.0, 40.0 * (0.0 * 1.0 + 1.0 * 2.0)),

        # Weights not summing to 1 but should still calculate linear combination
        (20.0, 1.5, 0.5, 0.7, 0.4, 20.0 * (0.7 * 1.5 + 0.4 * 0.5)),

        # Zero base hazard yields zero risk regardless of modifiers
        (0.0, 1.0, 1.0, 0.5, 0.5, 0.0),

        # Negative values (should handle gracefully or raise)
        (-10.0, 1.0, 1.0, 0.5, 0.5, -10.0 * (0.5 * 1.0 + 0.5 * 1.0)),
        (10.0, -1.0, 1.0, 0.5, 0.5, 10.0 * (0.5 * -1.0 + 0.5 * 1.0)),
        (10.0, 1.0, -1.0, 0.5, 0.5, 10.0 * (0.5 * 1.0 + 0.5 * -1.0)),
        (10.0, 1.0, 1.0, -0.5, 0.5, 10.0 * (-0.5 * 1.0 + 0.5 * 1.0)),
        (10.0, 1.0, 1.0, 0.5, -0.5, 10.0 * (0.5 * 1.0 + -0.5 * 1.0)),

        # Zero weights both zero (risk should be zero)
        (50.0, 1.0, 1.0, 0.0, 0.0, 0.0),

        # Very large inputs (to check for overflow or precision issues)
        (1e6, 1.0, 1.0, 0.5, 0.5, 1e6 * (0.5 * 1.0 + 0.5 * 1.0)),
        (1e6, 10.0, 10.0, 0.3, 0.7, 1e6 * (0.3 * 10.0 + 0.7 * 10.0)),

        # Non-float inputs that can convert to float: int values
        (40, 1, 2, 0.5, 0.5, 40 * (0.5 * 1 + 0.5 * 2)),
    ],
)
def test_calculate_systematic_risk(h_base_t, m_econ, i_ai, w_econ, w_inno, expected):
    # We use a tolerance for floating point comparisons
    import math
    result = calculate_systematic_risk(h_base_t, m_econ, i_ai, w_econ, w_inno)
    if isinstance(expected, float):
        assert math.isclose(result, expected, rel_tol=1e-9)
    else:
        assert result == expected

@pytest.mark.parametrize(
    "args",
    [
        # Non-numeric inputs should raise TypeError or ValueError
        ("string", 1.0, 1.0, 0.5, 0.5),
        (None, 1.0, 1.0, 0.5, 0.5),
        (50.0, "string", 1.0, 0.5, 0.5),
        (50.0, None, 1.0, 0.5, 0.5),
        (50.0, 1.0, "string", 0.5, 0.5),
        (50.0, 1.0, None, 0.5, 0.5),
        (50.0, 1.0, 1.0, "string", 0.5),
        (50.0, 1.0, 1.0, None, 0.5),
        (50.0, 1.0, 1.0, 0.5, "string"),
        (50.0, 1.0, 1.0, 0.5, None),

        # Too few or too many arguments (TypeError)
        (),
        (50.0,),
        (50.0,1.0),
        (50.0,1.0,1.0),
        (50.0,1.0,1.0,0.5),
        (50.0,1.0,1.0,0.5,0.5,0.5),
        (50.0,1.0,1.0,0.5,0.5,0.5,0.5),
    ],
)
def test_calculate_systematic_risk_invalid_inputs(args):
    with pytest.raises((TypeError, ValueError)):
        calculate_systematic_risk(*args)
