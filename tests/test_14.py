import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_a04997c6bc6648368d8d597845d72ba9 import plot_risk_over_transition

@pytest.fixture
def sample_df_transition_data():
    # Create a valid DataFrame sample to test the plot function.
    # It should have the necessary columns for plotting systematic risk and monthly premium over TTV period.
    data = {
        'Month': list(range(13)),  # 0 to 12 months inclusive
        'H_base': [65 - (x * (65 - 30) / 12) for x in range(13)],  # Linearly interpolate from 65 to 30 over 12 months
        'P_monthly': [max(20.0, 28.27 - x*0.7) for x in range(13)]  # Example premium decreasing from 28.27
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def df_missing_columns():
    # DataFrame missing required columns
    data = {'Month': [0, 1, 2], 'H_base': [65, 60, 55]}
    return pd.DataFrame(data)

@pytest.fixture
def df_non_numeric_columns():
    # DataFrame with non-numeric columns that should be numeric
    data = {
        'Month': [0, 1, 2],
        'H_base': ['high', 'medium', 'low'],
        'P_monthly': ['premium1', 'premium2', 'premium3']
    }
    return pd.DataFrame(data)

@pytest.fixture
def df_empty():
    # Empty DataFrame
    return pd.DataFrame()

@pytest.mark.parametrize("df_data, expected_exception", [
    (None, TypeError),
    ("not a dataframe", TypeError),
])
def test_plot_risk_over_transition_invalid_input_types(df_data, expected_exception):
    with pytest.raises(expected_exception):
        plot_risk_over_transition(df_data)

def test_plot_risk_over_transition_missing_columns(df_missing_columns):
    with pytest.raises(KeyError):
        plot_risk_over_transition(df_missing_columns)

def test_plot_risk_over_transition_non_numeric_columns(df_non_numeric_columns):
    with pytest.raises((ValueError, TypeError)):
        plot_risk_over_transition(df_non_numeric_columns)

def test_plot_risk_over_transition_empty_dataframe(df_empty):
    # If empty DataFrame is accepted or raises an error depends on implementation.
    # Let's expect it to raise a ValueError for empty data.
    with pytest.raises(ValueError):
        plot_risk_over_transition(df_empty)

def test_plot_risk_over_transition_valid(sample_df_transition_data):
    fig = plot_risk_over_transition(sample_df_transition_data)
    assert isinstance(fig, go.Figure)

    # Check that figure has data traces corresponding to expected line charts
    # at least 2 traces: one for H_base, one for P_monthly
    assert len(fig.data) >= 2

    trace_names = [trace.name for trace in fig.data]
    assert any('H_base' in name or 'Systematic Risk' in name for name in trace_names)
    assert any('P_monthly' in name or 'Monthly Premium' in name for name in trace_names)

    # Check x-axis and y-axis labels
    layout = fig.layout
    xaxis_title = layout.xaxis.title.text if layout.xaxis.title.text else ''
    yaxis_title = layout.yaxis.title.text if layout.yaxis.title.text else ''
    assert isinstance(xaxis_title, str)
    assert isinstance(yaxis_title, str)

def test_plot_risk_over_transition_monotonicity(sample_df_transition_data):
    # The systematic risk should be monotonic over transition period when linearly interpolated
    fig = plot_risk_over_transition(sample_df_transition_data)
    # Extract y-values for H_base trace and check monotonic decrease from 65 to 30
    for trace in fig.data:
        if 'H_base' in trace.name or 'Systematic Risk' in trace.name:
            y_vals = trace.y
            # Check monotonic: each next value <= previous (since risk decreases)
            assert all(y_vals[i] >= y_vals[i+1] for i in range(len(y_vals)-1))

def test_plot_risk_over_transition_handles_large_ttv():
    # Create DataFrame with large TTV (say 24 months) and verify plotting works
    data = {
        'Month': list(range(25)),  # 0 to 24 months
        'H_base': [65 - (x * (65 - 30) / 24) for x in range(25)],
        'P_monthly': [max(20.0, 28.27 - x*0.35) for x in range(25)]
    }
    df = pd.DataFrame(data)
    fig = plot_risk_over_transition(df)
    assert isinstance(fig, go.Figure)
    # Ensure number of points is correct
    for trace in fig.data:
        if 'H_base' in trace.name or 'Systematic Risk' in trace.name:
            assert len(trace.x) == 25
            assert len(trace.y) == 25

def test_plot_risk_over_transition_handles_non_uniform_months():
    # DataFrame with non-uniform month intervals
    data = {
        'Month': [0, 2, 5, 7, 12],
        'H_base': [65, 60, 55, 50, 30],
        'P_monthly': [28.27, 26.5, 24, 22, 20]
    }
    df = pd.DataFrame(data)
    fig = plot_risk_over_transition(df)
    assert isinstance(fig, go.Figure)
    # Check that months are the x-axis values as provided
    for trace in fig.data:
        assert all(month in trace.x for month in data['Month'])

def test_plot_risk_over_transition_with_nan_values():
    # DataFrame with some NaN values in critical columns should raise error or handle gracefully
    data = {
        'Month': [0, 1, 2, 3],
        'H_base': [65, None, 55, 50],
        'P_monthly': [28.27, 26.5, None, 20]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        plot_risk_over_transition(df)
