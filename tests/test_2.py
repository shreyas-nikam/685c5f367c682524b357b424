import pytest
from definition_37222868449845598735486a199711e0 import calculate_fhc

@pytest.mark.parametrize(
    "role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value, expected",
    [
        # Normal Cases: typical valid float inputs
        (1.35, 0.85, 0.90, 0.95, 1.0, 1.35 * 0.85 * 0.90 * 0.95 * 1.0),
        (0.3, 1.00, 1.10, 1.00, 0.7, 0.3 * 1.00 * 1.10 * 1.00 * 0.7),
        (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # all ones, product = 1.0

        # Edge Cases: zero multipliers yield zero result
        (0.0, 0.85, 0.90, 0.95, 1.0, 0.0),
        (1.35, 0.0, 0.90, 0.95, 1.0, 0.0),
        (1.35, 0.85, 0.0, 0.95, 1.0, 0.0),
        (1.35, 0.85, 0.90, 0.0, 1.0, 0.0),
        (1.35, 0.85, 0.90, 0.95, 0.0, 0.0),

        # Edge Cases: Negative multipliers - should calculate product normally,
        # but may not make sense logically, still test for handling
        (-1.35, 0.85, 0.90, 0.95, 1.0, -1.35 * 0.85 * 0.90 * 0.95 * 1.0),
        (1.35, -0.85, 0.90, 0.95, 1.0, 1.35 * -0.85 * 0.90 * 0.95 * 1.0),
        (1.35, 0.85, -0.90, 0.95, 1.0, 1.35 * 0.85 * -0.90 * 0.95 * 1.0),
        (1.35, 0.85, 0.90, -0.95, 1.0, 1.35 * 0.85 * 0.90 * -0.95 * 1.0),
        (1.35, 0.85, 0.90, 0.95, -1.0, 1.35 * 0.85 * 0.90 * 0.95 * -1.0),

        # Inputs as integers should be accepted as well (ints are valid float inputs)
        (1, 1, 1, 1, 1, 1.0),

        # Very large multipliers
        (1e10, 1e5, 1e3, 1e2, 1e1, 1e10 * 1e5 * 1e3 * 1e2 * 1e1),

        # Very small multipliers (close to zero but positive)
        (1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1e-10 * 1e-5 * 1e-3 * 1e-2 * 1e-1),

        # Floating point 'nan' and 'inf' cases - expect the function to propagate these
        (float('nan'), 0.85, 0.90, 0.95, 1.0, float('nan')),
        (1.35, float('nan'), 0.90, 0.95, 1.0, float('nan')),
        (1.35, 0.85, float('nan'), 0.95, 1.0, float('nan')),
        (1.35, 0.85, 0.90, float('nan'), 1.0, float('nan')),
        (1.35, 0.85, 0.90, 0.95, float('nan'), float('nan')),

        (float('inf'), 1.0, 1.0, 1.0, 1.0, float('inf')),
        (1.0, float('inf'), 1.0, 1.0, 1.0, float('inf')),
        (1.0, 1.0, float('inf'), 1.0, 1.0, float('inf')),
        (1.0, 1.0, 1.0, float('inf'), 1.0, float('inf')),
        (1.0, 1.0, 1.0, 1.0, float('inf'), float('inf')),
    ]
)
def test_calculate_fhc(role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value, expected):
    import math

    result = calculate_fhc(role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value)

    if isinstance(expected, float):
        if math.isnan(expected):
            assert math.isnan(result), f"Expected NaN but got {result}"
        elif math.isinf(expected):
            assert math.isinf(result) and (result > 0) == (expected > 0), f"Expected {expected} but got {result}"
        else:
            assert abs(result - expected) < 1e-9, f"Expected {expected} but got {result}"
    else:
        assert result == expected

@pytest.mark.parametrize(
    "invalid_args",
    [
        # Non-float types for each argument
        ("string", 0.85, 0.90, 0.95, 1.0),
        (1.35, "string", 0.90, 0.95, 1.0),
        (1.35, 0.85, "string", 0.95, 1.0),
        (1.35, 0.85, 0.90, "string", 1.0),
        (1.35, 0.85, 0.90, 0.95, "string"),

        # None values for arguments
        (None, 0.85, 0.90, 0.95, 1.0),
        (1.35, None, 0.90, 0.95, 1.0),
        (1.35, 0.85, None, 0.95, 1.0),
        (1.35, 0.85, 0.90, None, 1.0),
        (1.35, 0.85, 0.90, 0.95, None),

        # Boolean values (should be coerced or raise error)
        (True, 0.85, 0.90, 0.95, 1.0),
        (1.35, False, 0.90, 0.95, 1.0),
        (1.35, 0.85, True, 0.95, 1.0),
        (1.35, 0.85, 0.90, False, 1.0),
        (1.35, 0.85, 0.90, 0.95, True),

        # Completely wrong number of arguments (handled by pytest by calling function improperly)
    ]
)
def test_calculate_fhc_invalid_types(invalid_args):
    with pytest.raises(Exception):
        calculate_fhc(*invalid_args)
