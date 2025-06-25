import pytest
import pandas as pd
from definition_abc5baf0b5e74b8e9f90d3edeedd537e import plot_idiosyncratic_risk_by_skills

def sample_df_skill_data():
    # Create a sample dataframe with columns that are likely relevant for the plot
    # Since the original function parameter is df_skill_data, assume the dataframe has columns:
    # 'skill_progress' (0 to 1), 'idiosyncratic_risk', 'premium'
    # We test multiple points including edges 0 and 1 and some mid values
    return pd.DataFrame({
        'skill_progress': [0.0, 0.25, 0.5, 0.75, 1.0],
        'idiosyncratic_risk': [70, 55, 40, 25, 10],   # made-up values reflecting risk decreasing as skill increases
        'premium': [50, 40, 30, 25, 20]                # premium decreasing similarly
    })

@pytest.fixture
def df_empty():
    # Empty dataframe with expected columns but no rows
    return pd.DataFrame(columns=['skill_progress', 'idiosyncratic_risk', 'premium'])

@pytest.fixture
def df_invalid_cols():
    # Dataframe with wrong columns to test error handling
    return pd.DataFrame({
        'wrong_col1': [1,2,3],
        'wrong_col2': [4,5,6]
    })

@pytest.fixture
def df_null_values():
    # Dataframe with null values to test NaN handling
    return pd.DataFrame({
        'skill_progress': [0.0, None, 0.5],
        'idiosyncratic_risk': [70, 55, None],
        'premium': [50, None, 30]
    })

@pytest.fixture
def df_out_of_range():
    # Dataframe where skill_progress goes beyond expected 0-1 range
    return pd.DataFrame({
        'skill_progress': [-0.2, 0.0, 1.0, 1.5, 2.0],
        'idiosyncratic_risk': [70, 66, 10, 5, 2],
        'premium': [50, 45, 20, 15, 10]
    })

@pytest.mark.parametrize("df_input, expect_exception", [
    (None, TypeError),                  # None input: must raise TypeError or handled error
    ([], TypeError),                   # list instead of dataframe
    ({}, TypeError),                   # dict instead of dataframe
])
def test_invalid_type_input(df_input, expect_exception):
    with pytest.raises(expect_exception):
        plot_idiosyncratic_risk_by_skills(df_input)

def test_empty_dataframe(df_empty):
    fig = plot_idiosyncratic_risk_by_skills(df_empty)
    assert fig is not None
    # The figure should be empty or with no data traces
    assert hasattr(fig, 'data')
    assert len(fig.data) == 0 or all(len(trace.x)==0 for trace in fig.data)

def test_dataframe_with_invalid_columns(df_invalid_cols):
    with pytest.raises(KeyError):
        plot_idiosyncratic_risk_by_skills(df_invalid_cols)

def test_dataframe_with_null_values(df_null_values):
    # Depending on implementation, this might either:
    # - handle NaNs gracefully (ignore or interpolate)
    # - or raise an error
    # We test both acceptable behaviors:
    try:
        fig = plot_idiosyncratic_risk_by_skills(df_null_values)
        assert fig is not None
        assert hasattr(fig, 'data')
    except Exception as e:
        assert isinstance(e, (ValueError, TypeError, KeyError))

def test_dataframe_with_out_of_range_values(df_out_of_range):
    fig = plot_idiosyncratic_risk_by_skills(df_out_of_range)
    assert fig is not None
    assert hasattr(fig, 'data')
    # Verify skill_progress values on x-axis are within range or handled properly
    for trace in fig.data:
        if trace.x is not None:
            # They may contain out-of-range values. Just test type correctness
            assert all(isinstance(xi, (float, int)) for xi in trace.x)

def test_typical_use_case():
    df = sample_df_skill_data()
    fig = plot_idiosyncratic_risk_by_skills(df)
    assert fig is not None
    # Check figure has traces and expected number of data points
    assert hasattr(fig, 'data')
    assert len(fig.data) > 0
    for trace in fig.data:
        assert len(trace.x) == len(df)

def test_plot_output_type():
    # Ensure the function returns a Plotly Figure object
    df = sample_df_skill_data()
    fig = plot_idiosyncratic_risk_by_skills(df)
    import plotly.graph_objs
    assert isinstance(fig, plotly.graph_objs._figure.Figure)

def test_input_dataframe_immutable():
    df = sample_df_skill_data()
    df_copy = df.copy()
    plot_idiosyncratic_risk_by_skills(df)
    # Ensure input dataframe is not modified by the plotting function
    pd.testing.assert_frame_equal(df, df_copy)

def test_large_dataframe():
    # Stress test with large data input
    n = 10_000
    df_large = pd.DataFrame({
        'skill_progress': [i / (n - 1) for i in range(n)],
        'idiosyncratic_risk': [max(5, 100 - i*0.01) for i in range(n)],
        'premium': [max(20, 50 - i*0.005) for i in range(n)],
    })
    fig = plot_idiosyncratic_risk_by_skills(df_large)
    assert fig is not None
    assert hasattr(fig, 'data')

