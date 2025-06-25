import pytest
from definition_3860c547bdc046fcb8063e3057d9c8cd import calculate_fcr

@pytest.mark.parametrize("sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3, expected", [
    # Typical valid inputs with equal weights
    (0.5, 0.5, 0.5, 0.33, 0.33, 0.34, 0.5 * 0.33 + 0.5 * 0.33 + 0.5 * 0.34),
    # Weights sum to 1 exactly
    (0.8, 0.1, 0.1, 0.6, 0.3, 0.1, 0.8*0.6 + 0.1*0.3 + 0.1*0.1),
    # Weights sum to less than 1 (should still compute linear sum)
    (0.9, 0.05, 0.05, 0.2, 0.3, 0.1, 0.9*0.2 + 0.05*0.3 + 0.05*0.1),
    # Weights sum to more than 1 (should still compute linear sum)
    (0.4, 0.4, 0.2, 0.5, 0.5, 0.5, 0.4*0.5 + 0.4*0.5 + 0.2*0.5),
    # Zero scores and weights
    (0.0, 0.0, 0.0, 0.33, 0.33, 0.34, 0.0),
    # Negative scores (possibly invalid but test to catch error or output)
    (-0.1, 0.2, 0.3, 0.33, 0.33, 0.34, -0.1*0.33 + 0.2*0.33 + 0.3*0.34),
    # Negative weights (should handle or raise error)
    (0.5, 0.5, 0.5, -0.33, 0.33, 0.34, 0.5 * -0.33 + 0.5*0.33 + 0.5*0.34),
    # Scores above 1 (allowed for robustness)
    (1.5, 0.0, -0.5, 0.33, 0.33, 0.34, 1.5*0.33 + 0.0*0.33 + (-0.5)*0.34),
    # Very large scores and weights
    (1e6, 2e6, 3e6, 0.2, 0.3, 0.5, 1e6*0.2 + 2e6*0.3 + 3e6*0.5),
    # Weights are zero except one
    (0.1, 0.9, 0.5, 1.0, 0.0, 0.0, 0.1*1.0 + 0.9*0.0 + 0.5*0.0),
    (0.1, 0.9, 0.5, 0.0, 1.0, 0.0, 0.1*0.0 + 0.9*1.0 + 0.5*0.0),
    (0.1, 0.9, 0.5, 0.0, 0.0, 1.0, 0.1*0.0 + 0.9*0.0 + 0.5*1.0),
    # All weights zero
    (0.3, 0.3, 0.3, 0.0, 0.0, 0.0, 0.0),
    # Inputs as integers instead of floats
    (1, 2, 3, 0.1, 0.2, 0.7, 1*0.1 + 2*0.2 + 3*0.7),
])
def test_calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3, expected):
    try:
        result = calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)
        # Allow small floating point tolerance
        assert abs(result - expected) < 1e-9
    except Exception as e:
        # For invalid inputs we expect specific exceptions
        # We will identify these below
        # Inputs that are invalid types (str, None, etc) handled in separate tests
        pytest.fail(f"Unexpected exception {e} for inputs: {(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)}")

@pytest.mark.parametrize("args", [
    # Non-numeric sentiment_score
    ("a", 0.5, 0.5, 0.33, 0.33, 0.34),
    # Non-numeric financial_health_score
    (0.5, "b", 0.5, 0.33, 0.33, 0.34),
    # Non-numeric growth_ai_adoption_score
    (0.5, 0.5, "c", 0.33, 0.33, 0.34),
    # Non-numeric weights
    (0.5, 0.5, 0.5, "w1", 0.33, 0.34),
    (0.5, 0.5, 0.5, 0.33, None, 0.34),
    (0.5, 0.5, 0.5, 0.33, 0.33, []),
    # None inputs
    (None, 0.5, 0.5, 0.33, 0.33, 0.34),
    (0.5, None, 0.5, 0.33, 0.33, 0.34),
    (0.5, 0.5, None, 0.33, 0.33, 0.34),
    # All None
    (None, None, None, None, None, None),
])
def test_calculate_fcr_invalid_types(args):
    with pytest.raises((TypeError, ValueError)):
        calculate_fcr(*args)

@pytest.mark.parametrize("sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3", [
    # NaN values
    (float('nan'), 0.5, 0.5, 0.33, 0.33, 0.34),
    (0.5, float('nan'), 0.5, 0.33, 0.33, 0.34),
    (0.5, 0.5, float('nan'), 0.33, 0.33, 0.34),
    (0.5, 0.5, 0.5, float('nan'), 0.33, 0.34),
    (0.5, 0.5, 0.5, 0.33, float('nan'), 0.34),
    (0.5, 0.5, 0.5, 0.33, 0.33, float('nan')),
])
def test_calculate_fcr_nan_values(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3):
    # Depending on implementation, could raise or ignore NaNs
    # We accept ValueError or AssertionError or math domain errors
    with pytest.raises((ValueError, TypeError)):
        calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)

@pytest.mark.parametrize("sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3", [
    # Infinite values
    (float('inf'), 0.5, 0.5, 0.33, 0.33, 0.34),
    (0.5, float('-inf'), 0.5, 0.33, 0.33, 0.34),
    (0.5, 0.5, float('inf'), 0.33, 0.33, 0.34),
    (0.5, 0.5, 0.5, float('inf'), 0.33, 0.34),
    (0.5, 0.5, 0.5, 0.33, float('-inf'), 0.34),
    (0.5, 0.5, 0.5, 0.33, 0.33, float('inf')),
])
def test_calculate_fcr_infinite_values(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3):
    with pytest.raises((OverflowError, ValueError, TypeError)):
        calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)
