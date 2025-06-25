import pytest
from definition_37d7a5114a2a429baf7aaf6e968d086c import calculate_fus

@pytest.mark.parametrize("p_gen, p_spec, gamma_gen, gamma_spec, expected", [
    # Basic valid inputs: No training progress
    (0.0, 0.0, 0.7, 0.3, 1.0),
    # Full training progress in both, with normal weights
    (1.0, 1.0, 0.7, 0.3, 1 - (0.7*1.0 + 0.3*1.0)),  # 0.0
    # Partial progress
    (0.5, 0.5, 0.7, 0.3, 1 - (0.7*0.5 + 0.3*0.5)),  # 1 - 0.5 = 0.5
    # More weight on general skill progress
    (0.8, 0.2, 0.8, 0.2, 1 - (0.8*0.8 + 0.2*0.2)),  # 1 - (0.64 + 0.04) = 0.32
    # Edge case: p_gen = 0, p_spec = 1
    (0.0, 1.0, 0.7, 0.3, 1 - (0.7*0.0 + 0.3*1.0)),  # 1 - 0.3 = 0.7
    # Edge case: p_gen = 1, p_spec = 0
    (1.0, 0.0, 0.7, 0.3, 1 - (0.7*1.0 + 0.3*0.0)),  # 1 - 0.7 = 0.3
    # Edge case: gamma_gen and gamma_spec both zero (no weighting)
    (0.5, 0.5, 0.0, 0.0, 1.0),
    # Edge case: gamma_gen + gamma_spec > 1 (allowed in implementation, should just calculate linearly)
    (0.5, 0.5, 1.5, 1.0, 1 - (1.5*0.5 + 1.0*0.5)),  # 1 - (0.75 +0.5) = negative -0.25
    # Edge case: p_gen and/or p_spec out of range (should raise ValueError)
    (-0.1, 0.0, 0.7, 0.3, ValueError),
    (0.0, -0.1, 0.7, 0.3, ValueError),
    (1.1, 0.0, 0.7, 0.3, ValueError),
    (0.0, 1.1, 0.7, 0.3, ValueError),
    # Edge case: gamma_gen and/or gamma_spec negative (should raise ValueError)
    (0.5, 0.5, -0.1, 0.3, ValueError),
    (0.5, 0.5, 0.7, -0.1, ValueError),
    # Edge case: non-float inputs (should raise TypeError)
    ("0.5", 0.5, 0.7, 0.3, TypeError),
    (0.5, "0.5", 0.7, 0.3, TypeError),
    (0.5, 0.5, "0.7", 0.3, TypeError),
    (0.5, 0.5, 0.7, "0.3", TypeError),
    # Edge case: None inputs
    (None, 0.5, 0.7, 0.3, TypeError),
    (0.5, None, 0.7, 0.3, TypeError),
    (0.5, 0.5, None, 0.3, TypeError),
    (0.5, 0.5, 0.7, None, TypeError),
])
def test_calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec)
    else:
        result = calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec)
        # Allow small numeric tolerance for floating point
        assert isinstance(result, float)
        assert abs(result - expected) < 1e-6

