id: 685c5f367c682524b357b424_documentation
summary: AI Risk Score - V4 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI Risk Score - V4: Career Path Diversification Codelab

This codelab provides a comprehensive guide to understanding and utilizing the "AI Risk Score - V4: Career Path Diversification" Streamlit application. This application is designed to help individuals quantify and mitigate their exposure to AI-driven job displacement risk, operationalizing the core concepts from the "AI-Q Score: A Multi-Factor Parametric Framework for Quantifying and Mitigating AI-Driven Job Displacement Risk" research.  You'll learn how the app calculates idiosyncratic and systematic risk, simulates career transitions, and visualizes the impact of upskilling.

## Introduction to the AI-Q Score Framework

Duration: 00:05

The AI-Q Score framework is designed to quantify an individual's job displacement risk due to AI advancements. The total risk is broken down into two main components:

1.  **Idiosyncratic Risk ($V_i(t)$)**:  Individual-specific risk that can be managed through skills and company choices.
2.  **Systematic Risk ($H_i$)**: Macro-level risk inherent to an occupation, influenced by the economy and AI innovation.

This application allows users to:

*   Assess their current risk profile.
*   Explore alternative career paths.
*   Simulate the impact of skill acquisition.

<aside class="positive">
Understanding these concepts is crucial for making informed career decisions and building financial resilience in an AI-driven world.  This tool empowers you to proactively manage your career in the face of technological change.
</aside>

## Setting Up the Environment and Running the App

Duration: 00:03

To run the application, you'll need Python 3.6+ and the following libraries:

*   streamlit
*   pandas
*   numpy
*   plotly

You can install these using pip:

```console
pip install streamlit pandas numpy plotly
```

Save the provided code as `app.py`, `utils/data_loader.py`, `utils/risk_calculator.py`, and `utils/visualization_utils.py`.  Ensure you create the `utils` directory and place the files accordingly. Then, navigate to the directory containing `app.py` in your terminal and run:

```console
streamlit run app.py
```

This will open the application in your web browser.

## Understanding the Data Loader (`utils/data_loader.py`)

Duration: 00:05

The `data_loader.py` script contains the `load_synthetic_data` function. This function loads pre-defined synthetic datasets into Python dictionaries, including:

*   `occupations_data`:  Contains `H_base` (Base Occupational Hazard) and `f_role` (Role Multiplier) for different job titles.
*   `education_data`:  Contains `f_level` (Education Level Factor) for different education levels.
*   `education_field_data`: Contains `f_field` (Education Field Factor) for different fields of study.
*   `school_tier_data`: Contains `f_school` (School Tier Factor) for different school tiers.
*   `company_type_data`: Contains `F_CR` (Company Risk Factor) for different company types.
*   `actuarial_parameters`:  Contains parameters like `Annual Salary`, `Coverage Duration`, `Loading Factor`, etc., used in the risk calculation.

```python
import pandas as pd

def load_synthetic_data():
    """
    Loads all pre-defined synthetic datasets into appropriate Python data structures.
    """
    occupations_data = {
        'Data Entry Clerk': {'H_base': 65, 'f_role': 1.35},
        'Paralegal': {'H_base': 70, 'f_role': 1.20},
        'Financial Analyst': {'H_base': 55, 'f_role': 0.85},
        'Software Developer': {'H_base': 40, 'f_role': 0.60},
        'Senior Research Scientist': {'H_base': 30, 'f_role': 0.30},
        'Customer Service Representative': {'H_base': 80, 'f_role': 1.50},
        'Project Manager': {'H_base': 45, 'f_role': 0.70},
        'HR Manager': {'H_base': 50, 'f_role': 0.80},
        'Marketing Specialist': {'H_base': 60, 'f_role': 0.90},
        'Graphic Designer': {'H_base': 58, 'f_role': 0.95},
        'Accountant': {'H_base': 75, 'f_role': 1.30},
        'Nurse': {'H_base': 20, 'f_role': 0.20},
        'Electrician': {'H_base': 15, 'f_role': 0.15},
        'Data Scientist': {'H_base': 35, 'f_role': 0.50},
        'Teacher': {'H_base': 25, 'f_role': 0.25},
    }

    education_data = {
        'High School': {'f_level': 1.15},
        'Associate\'s': {'f_level': 1.10},
        'Bachelor\'s': {'f_level': 1.00},
        'Master\'s': {'f_level': 0.90},
        'PhD': {'f_level': 0.85},
    }

    education_field_data = {
        'Liberal Arts/Humanities': {'f_field': 1.10},
        'Business/Management': {'f_field': 1.05},
        'STEM (Science, Technology, Engineering, Math)': {'f_field': 0.90},
        'Fine Arts/Design': {'f_field': 1.08},
        'Healthcare': {'f_field': 0.88},
    }

    school_tier_data = {
        'Tier 1 (Ivy League/Top Research)': {'f_school': 0.95},
        'Tier 2 (Reputable State/Private)': {'f_school': 1.00},
        'Tier 3 (Local/Community College)': {'f_school': 1.05},
    }

    company_type_data = {
        'Big Tech/Innovative Start-up': {'F_CR': 0.90},
        'Large Established Firm (Non-Tech)': {'F_CR': 1.00},
        'Mid-size Firm': {'F_CR': 1.05},
        'Small Business/Local Enterprise': {'F_CR': 1.15},
        'Government/Non-Profit': {'F_CR': 0.95},
    }

    actuarial_parameters = {
        'Annual Salary': 90000,
        'Coverage Duration': 6,  # months
        'Coverage Percentage': 0.25, # 25% of salary replaced
        'Beta Systemic': 0.10,
        'Beta Individual': 0.50,
        'Loading Factor': 1.5,
        'Minimum Monthly Premium': 20.00,
        'W_CR': 0.4, # Weight for Company Risk Factor in Idiosyncratic Risk
        'W_US': 0.6, # Weight for Upskilling Factor in Idiosyncratic Risk
        'W_ECON': 0.5, # Weight for Economic Climate Modifier in Systematic Risk
        'W_INNO': 0.5, # Weight for AI Innovation Index in Systematic Risk
        'GAMMA_GEN': 0.7, # Weight for General Skill Progress in Upskilling Factor
        'GAMMA_SPEC': 0.3, # Weight for Firm-Specific Skill Progress in Upskilling Factor
        'TTV_DEFAULT': 12, # Default Time-to-Value period in months
    }

    return {
        'occupations_data': occupations_data,
        'education_data': education_data,
        'education_field_data': education_field_data,
        'school_tier_data': school_tier_data,
        'company_type_data': company_type_data,
        'actuarial_parameters': actuarial_parameters
    }
```

This data is used to calculate the various risk factors within the application.

## Exploring the Risk Calculator (`utils/risk_calculator.py`)

Duration: 00:15

The `risk_calculator.py` script contains functions to calculate the various risk factors and scores. Here's a breakdown of the key functions:

*   **`calculate_fexp(years_experience)`**: Calculates the Experience Factor (`f_exp`).
*   **`calculate_fhc(role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value)`**: Calculates the Human Capital Factor (`FHC`).
*   **`calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1=0.33, w2=0.33, w3=0.34)`**: Calculates the Company Risk Factor (`F_CR`).
*   **`calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec)`**: Calculates the Upskilling Factor (`F_US`).
*   **`calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us)`**: Calculates the Idiosyncratic Risk (`V_i(t)`).
*   **`calculate_h_base_ttv(k, ttv, h_current, h_target)`**: Calculates the Base Occupational Hazard with Transition Time-to-Value (TTV) Modifier (`H_base(k)`).
*   **`calculate_systematic_risk(h_base_t, mecon, iai, w_econ, w_inno)`**: Calculates the Systematic Risk (`H_i`).
*   **`calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage)`**: Calculates the Total Payout Amount (`L_payout`).
*   **`calculate_p_systemic(h_i, beta_systemic)`**: Calculates the Probability of a Systemic Event (`P_systemic`).
*   **`calculate_p_individual_systemic(v_i_t, beta_individual)`**: Calculates the Conditional Probability of Job Loss Given a Systemic Event (`P_individual|systemic`).
*   **`calculate_p_claim(p_systemic, p_individual_systemic)`**: Calculates the Annual Claim Probability (`P_claim`).
*   **`calculate_expected_loss(p_claim, lpayout)`**: Calculates the Annual Expected Loss (`E[Loss]`).
*   **`calculate_monthly_premium(expected_loss, loading_factor, min_premium)`**: Calculates the Final Monthly Premium (`P_monthly`).

```python
import numpy as np

def calculate_fexp(years_experience):
    """
    Calculates the Experience Factor (f_exp).
    f_exp = 1 - (0.015 * min(Yrs, 20))
    """
    return 1 - (0.015 * min(years_experience, 20))

def calculate_fhc(role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value):
    """
    Calculates the Human Capital Factor (FHC).
    FHC = f_role * f_level * f_field * f_school * f_exp
    """
    return role_multiplier * edu_level_factor * edu_field_factor * school_tier_factor * fexp_value

def calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1=0.33, w2=0.33, w3=0.34):
    """
    Calculates the Company Risk Factor (F_CR).
    F_CR = w_1 * S_senti + w_2 * S_fin + w_3 * S_growth
    For simplicity, S_senti, S_fin, S_growth will be simulated/fixed in the app.
    """
    return (w1 * sentiment_score + w2 * financial_health_score + w3 * growth_ai_adoption_score)

def calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec):
    """
    Calculates the Upskilling Factor (F_US).
    F_US = 1 - (gamma_gen * P_gen(t) + gamma_spec * P_spec(t))
    """
    return 1 - (gamma_gen * p_gen + gamma_spec * p_spec)

def calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us):
    """
    Calculates the Idiosyncratic Risk (V_i(t)).
    V_raw = FHC * (w_CR * FCR + w_US * FUS)
    V_i(t) = min(100.0, max(5.0, V_raw * 50.0))
    """
    v_raw = fhc * (w_cr * fcr + w_us * fus)
    return min(100.0, max(5.0, v_raw * 50.0))

def calculate_h_base_ttv(k, ttv, h_current, h_target):
    """
    Calculates the Base Occupational Hazard with Transition Time-to-Value (TTV) Modifier (H_base(k)).
    H_base(k) = (1 - k/TTV) * H_current + (k/TTV) * H_target
    """
    if ttv == 0: # Avoid division by zero
        return h_target
    if k >= ttv: # If transition is complete or beyond TTV
        return h_target
    return (1 - k / ttv) * h_current + (k / ttv) * h_target

def calculate_systematic_risk(h_base_t, mecon, iai, w_econ, w_inno):
    """
    Calculates the Systematic Risk (H_i).
    H_i = H_base(t) * (w_econ * M_econ + w_inno * I_AI)
    """
    return h_base_t * (w_econ * mecon + w_inno * iai)

def calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage):
    """
    Calculates the Total Payout Amount (L_payout).
    L_payout = (Annual Salary / 12) * Coverage Duration * Coverage Percentage
    """
    return (annual_salary / 12) * coverage_duration * coverage_percentage

def calculate_p_systemic(h_i, beta_systemic):
    """
    Calculates the Probability of a Systemic Event (P_systemic).
    P_systemic = (H_i / 100) * beta_systemic
    """
    return (h_i / 100) * beta_systemic

def calculate_p_individual_systemic(v_i_t, beta_individual):
    """
    Calculates the Conditional Probability of Job Loss Given a Systemic Event (P_individual|systemic).
    P_individual|systemic = (V_i(t) / 100) * beta_individual
    """
    return (v_i_t / 100) * beta_individual

def calculate_p_claim(p_systemic, p_individual_systemic):
    """
    Calculates the Annual Claim Probability (P_claim).
    P_claim = P_systemic * P_individual|systemic
    """
    return p_systemic * p_individual_systemic

def calculate_expected_loss(p_claim, lpayout):
    """
    Calculates the Annual Expected Loss (E[Loss]).
    E[Loss] = P_claim * L_payout
    """
    return p_claim * lpayout

def calculate_monthly_premium(expected_loss, loading_factor, min_premium):
    """
    Calculates the Final Monthly Premium (P_monthly).
    P_monthly = max((E[Loss] * lambda) / 12, P_min)
    """
    return max((expected_loss * loading_factor) / 12, min_premium)
```

These functions are the core of the AI Risk Score calculation. They take various factors related to an individual's profile, company, and macroeconomic conditions as input and output the corresponding risk scores and monthly premium.

## Understanding the Visualization Utilities (`utils/visualization_utils.py`)

Duration: 00:07

The `visualization_utils.py` script contains functions for generating visualizations using Plotly. These functions include:

*   **`plot_risk_over_transition(df_transition_data)`**: Generates a line chart showing how Systematic Risk and Monthly Premium evolve over the TTV period during a career transition.
*   **`plot_idiosyncratic_risk_by_skills(df_skill_data)`**: Generates a line chart showing the impact of skill acquisition on Idiosyncratic Risk and Monthly Premium.
*   **`plot_risk_breakdown(current_scores, simulated_scores)`**: Generates a bar chart comparing current and simulated risk components.

```python
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
```

These visualizations help users understand the impact of different factors on their AI job displacement risk and the potential benefits of career diversification and upskilling.

## Diving into the Main Application (`app.py`)

Duration: 00:20

The `app.py` script is the main Streamlit application. Here's a breakdown of its key sections:

1.  **Import Statements:** Imports necessary libraries and functions from the other modules.
2.  **Page Configuration:** Sets the page title and layout.
3.  **Introduction and Explanation:** Provides an overview of the application and the AI-Q Score framework.
4.  **Sidebar: Global & Actuarial Parameters:**  Allows users to adjust global parameters like the Economic Climate Modifier and AI Innovation Index, as well as actuarial policy terms like Annual Salary, Coverage Duration, and Loading Factor.

    *   **Economic Climate Modifier ($M_{econ}$)**: A normalized index reflecting the overall economic health.
    *   **AI Innovation Index ($I_{AI}$)**: A normalized momentum index for AI advancements.
    *   **Actuarial Policy Terms**: Define the parameters of the hypothetical insurance policy.
5.  **Current Profile Section:** Allows users to input their current job details (job title, experience, education, company type, etc.) and calculates their current Idiosyncratic Risk, Systematic Risk, and Estimated Monthly Premium.
6.  **Company Risk Factors (Simulated):** This section simulates company risk factors. In a real-world application, these would be derived from real-time data.
7.  **Career Transition Simulation Section:**  Allows users to simulate a career transition by selecting a target career path and adjusting the Transition Progress and Skill Acquisition Progress. It recalculates the risk scores and premium based on the simulated values.
8.  **Visualizations Section:** Displays charts showing the comparison between current and simulated risk, the risk trend during the career transition, and the impact of skill acquisition.

Let's walk through the code.

