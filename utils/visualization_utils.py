
import plotly.express as px
import pandas as pd

def plot_risk_over_transition(df_transition_data):
    """
    Generates a Plotly line chart showing how Systematic Risk and Monthly Premium
    evolve over the TTV period during a career transition.
    df_transition_data should have columns: 'Months Elapsed', 'Systematic Risk', 'Monthly Premium'.
    """
    fig = px.line(df_transition_data, x='Months Elapsed', y=['Systematic Risk', 'Monthly Premium'],
                  title='Systematic Risk & Monthly Premium Over Transition Period',
                  labels={'value': 'Score / Premium ($)', 'variable': 'Metric'},
                  hover_data={'Months Elapsed': True, 'Systematic Risk': ':.2f', 'Monthly Premium': ':.2f'})
    fig.update_layout(hovermode="x unified")
    return fig

def plot_idiosyncratic_risk_by_skills(df_skill_data):
    """
    Generates a Plotly line chart showing the impact of skill acquisition
    on Idiosyncratic Risk and Monthly Premium.
    df_skill_data should have columns: 'Skill Progress', 'Idiosyncratic Risk', 'Monthly Premium'.
    """
    fig = px.line(df_skill_data, x='Skill Progress', y=['Idiosyncratic Risk', 'Monthly Premium'],
                  title='Impact of Skill Acquisition on Idiosyncratic Risk & Premium',
                  labels={'value': 'Score / Premium ($)', 'variable': 'Metric'},
                  hover_data={'Skill Progress': ':.0%', 'Idiosyncratic Risk': ':.2f', 'Monthly Premium': ':.2f'})
    fig.update_layout(hovermode="x unified")
    return fig

def plot_risk_breakdown(current_scores, simulated_scores):
    """
    Generates a bar chart comparing current and simulated risk components
    (e.g., Idiosyncratic Risk, Systematic Risk).
    current_scores and simulated_scores are dictionaries like {'Idiosyncratic Risk': value, 'Systematic Risk': value}.
    """
    data = {
        'Risk Type': ['Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium'] * 2,
        'Value': [
            current_scores['Idiosyncratic Risk'],
            current_scores['Systematic Risk'],
            current_scores['Monthly Premium'],
            simulated_scores['Idiosyncratic Risk'],
            simulated_scores['Systematic Risk'],
            simulated_scores['Monthly Premium']
        ],
        'Scenario': ['Current'] * 3 + ['Simulated'] * 3
    }
    df = pd.DataFrame(data)

    fig = px.bar(df, x='Risk Type', y='Value', color='Scenario', barmode='group',
                 title='Comparison: Current vs. Simulated Risk & Premium',
                 labels={'Value': 'Score / Premium ($)', 'Risk Type': 'Risk Component'},
                 hover_data={'Value': ':.2f'})
    return fig
