import pytest
from definition_e74dd74a58e9473683ca384b2f64da15 import calculate_h_base_ttv

@pytest.mark.parametrize("k, ttv, h_current, h_target, expected", [
    # Typical cases
    (0, 12, 65, 30, 65.0),
    (6, 12, 65, 30, 47.5),
    (12, 12, 65, 30, 30.0),
    (3, 12, 0, 100, 25.0),
    (12, 24, 20, 80, 50.0),
    (24, 24, 20, 80, 80.0),

    # Edge cases: k = 0 (start)
    (0, 1, 100, 200, 100.0),
    # Edge case: k = TTV (end)
    (1, 1, 100, 200, 200.0),

    # k greater than ttv (should handle gracefully)
    (13, 12, 65, 30, 30.0),  # capped at h_target

    # k less than 0 (invalid input)
    (-1, 12, 65, 30, 65.0),  # treated as 0

    # ttv = 0 (division by zero, expect exception)
    #(0, 0, 65, 30, ZeroDivisionError), # will test separately

    # h_current equals h_target
    (5, 10, 50, 50, 50.0),
    # Large values of hazards
    (5, 10, 1e6, 2e6, 1.5e6),
    # Zero hazards
    (5, 10, 0, 0, 0.0),
])
def test_calculate_h_base_ttv(k, ttv, h_current, h_target, expected):
    if ttv == 0:
        with pytest.raises(ZeroDivisionError):
            calculate_h_base_ttv(k, ttv, h_current, h_target)
    else:
        # Ensure k is bounded between 0 and ttv
        k_effective = max(0, min(k, ttv))
        result = calculate_h_base_ttv(k_effective, ttv, h_current, h_target)
        assert pytest.approx(result, rel=1e-9) == expected


@pytest.mark.parametrize("k, ttv, h_current, h_target", [
    (0, 0, 65, 30),
    (5, 0, 65, 30),
])
def test_calculate_h_base_ttv_zero_ttv(k, ttv, h_current, h_target):
    with pytest.raises(ZeroDivisionError):
        calculate_h_base_ttv(k, ttv, h_current, h_target)


@pytest.mark.parametrize("k, ttv, h_current, h_target", [
    (None, 12, 65, 30),
    (6, None, 65, 30),
    (6, 12, None, 30),
    (6, 12, 65, None),
    ("6", 12, 65, 30),
    (6, "12", 65, 30),
    (6, 12, "65", 30),
    (6, 12, 65, "30"),
])
def test_calculate_h_base_ttv_invalid_types(k, ttv, h_current, h_target):
    with pytest.raises((TypeError, ValueError)):
        calculate_h_base_ttv(k, ttv, h_current, h_target)
