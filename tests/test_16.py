import pytest
from definition_fd10ab2670c64b2db03cad559afd7d4d import plot_risk_breakdown

@pytest.mark.parametrize("current_risk_scores, simulated_risk_scores", [
    # Nominal case with simple comparable dictionaries
    (
        {'Idiosyncratic Risk': 61.85, 'Systematic Risk': 65.0, 'Monthly Premium': 28.27},
        {'Idiosyncratic Risk': 48.6, 'Systematic Risk': 47.5, 'Monthly Premium': 25.00}
    ),
    # Case with zeros to test zero or no risk scenario
    (
        {'Idiosyncratic Risk': 0, 'Systematic Risk': 0, 'Monthly Premium': 0},
        {'Idiosyncratic Risk': 0, 'Systematic Risk': 0, 'Monthly Premium': 0}
    ),
    # Large values for stress test
    (
        {'Idiosyncratic Risk': 150, 'Systematic Risk': 200, 'Monthly Premium': 1000},
        {'Idiosyncratic Risk': 140, 'Systematic Risk': 190, 'Monthly Premium': 900}
    ),
    # Missing keys in one of the dicts
    (
        {'Idiosyncratic Risk': 50, 'Systematic Risk': 40},
        {'Idiosyncratic Risk': 45, 'Systematic Risk': 35, 'Monthly Premium': 22}
    ),
    # Extra keys present in dictionaries
    (
        {'Idiosyncratic Risk': 30, 'Systematic Risk': 25, 'Monthly Premium': 20, 'Extra Key': 999},
        {'Idiosyncratic Risk': 28, 'Systematic Risk': 22, 'Monthly Premium': 18, 'Another Extra': 100}
    ),
    # Different numeric types (int and float mix)
    (
        {'Idiosyncratic Risk': 51, 'Systematic Risk': 65.0, 'Monthly Premium': 28},
        {'Idiosyncratic Risk': 49.5, 'Systematic Risk': 47, 'Monthly Premium': 25.5}
    ),
    # Empty dictionaries
    (
        {}, {}
    ),
    # Very large dictionary with many keys but valid keys included
    (
        {**{f"Key{i}": i for i in range(100)}, 'Idiosyncratic Risk': 55, 'Systematic Risk': 60, 'Monthly Premium': 30},
        {**{f"Key{i}": i*2 for i in range(100)}, 'Idiosyncratic Risk': 50, 'Systematic Risk': 55, 'Monthly Premium': 28}
    ),
    # Non-dictionary inputs (should raise error or be handled)
    (
        ["Not", "a", "dict"],
        {"Idiosyncratic Risk": 10, "Systematic Risk": 15, "Monthly Premium": 5}
    ),
    (
        {"Idiosyncratic Risk": 10, "Systematic Risk": 15, "Monthly Premium": 5},
        None
    ),
])
def test_plot_risk_breakdown(current_risk_scores, simulated_risk_scores):
    """
    Test plot_risk_breakdown function with varying inputs, including edge cases and invalid inputs.

    Tests that the function returns a valid Plotly Figure object for valid inputs and raises appropriate exceptions
    or handles errors gracefully for invalid inputs.
    """

    from plotly.graph_objs import Figure
    # Test type and behavior
    if not (isinstance(current_risk_scores, dict) and isinstance(simulated_risk_scores, dict)):
        # Expect an exception due to invalid input types
        with pytest.raises(Exception):
            plot_risk_breakdown(current_risk_scores, simulated_risk_scores)
    else:
        # For dict inputs, test normal function execution
        fig = plot_risk_breakdown(current_risk_scores, simulated_risk_scores)
        # Assert the return type is a Plotly Figure object
        assert isinstance(fig, Figure)
        # Further assert that figure contains data
        assert hasattr(fig, 'data')
        # At least one trace for current and one for simulated risks expected
        assert len(fig.data) >= 1
        # Verify that the bar chart has correct number of bars (keys that overlap or union may be shown)
        # Assuming the function uses all keys from both dicts
        keys = set(current_risk_scores.keys()) | set(simulated_risk_scores.keys())
        assert len(fig.data[0].y) == len(keys)
        assert len(fig.data[-1].y) == len(keys)

        # Check bar chart names match expected series
        assert fig.data[0].name in ["Current", "Simulated"]
        assert fig.data[-1].name in ["Current", "Simulated"]
        assert fig.data[0].name != fig.data[-1].name

