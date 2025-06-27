
import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_synthetic_data
from utils.risk_calculator import (
    calculate_fexp, calculate_fhc, calculate_fcr, calculate_fus,
    calculate_idiosyncratic_risk, calculate_h_base_ttv, calculate_systematic_risk,
    calculate_payout_amount, calculate_p_systemic, calculate_p_individual_systemic,
    calculate_p_claim, calculate_expected_loss, calculate_monthly_premium
)
from utils.visualization_utils import plot_risk_over_transition, plot_idiosyncratic_risk_by_skills, plot_risk_breakdown

st.set_page_config(page_title="AI Risk Score - V4: Career Path Diversification", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("AI Risk Score - V4")
st.subheader("Career Path Diversification Tool")
st.divider()

st.markdown("""
In this lab, we introduce the **AI Risk Score - V4: Career Path Diversification Tool**, a Streamlit application
designed to help individuals quantify and mitigate their exposure to AI-driven job displacement risk.
This tool operationalizes the core concepts from the "AI-Q Score: A Multi-Factor Parametric Framework
for Quantifying and Mitigating AI-Driven Job Displacement Risk" research document.

### The Problem: AI and Job Displacement
The rapid advancements in Artificial Intelligence (AI) are fundamentally reshaping the global labor market.
While AI creates new opportunities, it also poses a significant risk of job displacement for various roles
across industries. Understanding and proactively managing this risk is crucial for career longevity and financial stability.

### Our Solution: The AI-Q Score Framework
The AI-Q Score framework provides a comprehensive method to quantify an individual's job displacement risk.
It breaks down the total risk into two main components:

1.  **Idiosyncratic Risk ($V_i(t)$)**: This represents the individual-specific, manageable vulnerability to job displacement.
    It considers your unique human capital, your employer's stability, and your proactive efforts in upskilling.
    This is the part of your risk that you can directly influence.

2.  **Systematic Risk ($H_i$)**: This reflects the macro-level automation hazard inherent to an entire occupation,
    adjusted by broader environmental factors like the economic climate and the velocity of AI innovation.
    This is the part of your risk that is largely outside of your direct control but can be mitigated
    through strategic career path diversification.

### Career Path Diversification
Just as investors diversify their portfolios to mitigate market risk, individuals can diversify their
career paths to reduce their exposure to systematic AI risk. This application allows you to:
*   Assess your current risk profile.
*   Explore alternative career paths with different inherent systematic risks.
*   Simulate the impact of skill acquisition and career transitions on your risk scores and hypothetical
    "AI displacement insurance" premiums.

By interacting with this tool, you can visualize how strategic career choices and continuous learning can
significantly improve your financial resilience in an AI-driven world.
""")

st.divider()

# Load synthetic data
data = load_synthetic_data()
occupations_data = data['occupations_data']
education_data = data['education_data']
education_field_data = data['education_field_data']
school_tier_data = data['school_tier_data']
company_type_data = data['company_type_data']
actuarial_params = data['actuarial_parameters']

# Sidebar for Global and Actuarial Parameters
st.sidebar.header("Global & Actuarial Parameters")
st.sidebar.markdown("Adjust these parameters to see their impact on risk scores and premiums.")

economic_climate_modifier = st.sidebar.slider(
    "Economic Climate Modifier ($M_{econ}$)",
    min_value=0.8, max_value=1.2, value=1.0, step=0.01,
    help="A normalized index reflecting the overall economic health. Higher values indicate tougher economic conditions."
)
ai_innovation_index = st.sidebar.slider(
    "AI Innovation Index ($I_{AI}$)",
    min_value=0.8, max_value=1.2, value=1.0, step=0.01,
    help="A normalized momentum index for AI advancements. Higher values indicate faster AI progress and potential disruption."
)

st.sidebar.subheader("Actuarial Policy Terms")
annual_salary = st.sidebar.number_input(
    "Your Annual Salary ($)",
    min_value=10000, value=int(actuarial_params['Annual Salary']), step=5000,
    help="Your current annual gross salary used for calculating potential payout."
)
coverage_duration = st.sidebar.number_input(
    "Coverage Duration (months)",
    min_value=1, max_value=24, value=actuarial_params['Coverage Duration'], step=1,
    help="Number of months of income replacement if job displacement occurs."
)
coverage_percentage = st.sidebar.slider(
    "Coverage Percentage (%)",
    min_value=0.05, max_value=1.0, value=actuarial_params['Coverage Percentage'], step=0.05, format="%.0f%%",
    help="Percentage of your salary replaced by the insurance in case of displacement."
)
loading_factor = st.sidebar.slider(
    "Insurance Loading Factor ($\lambda$)",
    min_value=1.0, max_value=2.0, value=actuarial_params['Loading Factor'], step=0.05,
    help="An insurance multiplier for administrative costs and profit margin."
)
min_monthly_premium = st.sidebar.number_input(
    "Minimum Monthly Premium ($P_{min}$)",
    min_value=0.0, value=actuarial_params['Minimum Monthly Premium'], step=5.0,
    help="The minimum monthly premium charged, regardless of calculated risk."
)

# Constants from actuarial_params
w_cr = actuarial_params['W_CR']
w_us = actuarial_params['W_US']
w_econ = actuarial_params['W_ECON']
w_inno = actuarial_params['W_INNO']
gamma_gen = actuarial_params['GAMMA_GEN']
gamma_spec = actuarial_params['GAMMA_SPEC']
beta_systemic = actuarial_params['Beta Systemic']
beta_individual = actuarial_params['Beta Individual']
ttv_default = actuarial_params['TTV_DEFAULT']

# --- Current Profile Section ---
st.header("Your Current Career Profile")
st.markdown("""
Input your current job details to assess your present AI job displacement risk.
This section calculates your **Idiosyncratic Risk** and **Systematic Risk**.
""")

col1, col2 = st.columns(2)

with col1:
    current_job_title = st.selectbox(
        "Your Current Job Title",
        options=list(occupations_data.keys()),
        index=list(occupations_data.keys()).index('Software Developer') # Default value
    )
    years_experience = st.slider("Years of Professional Experience", min_value=0, max_value=40, value=10)
    education_level = st.selectbox(
        "Highest Education Level",
        options=list(education_data.keys()),
        index=list(education_data.keys()).index("Bachelor's")
    )
    education_field = st.selectbox(
        "Education Field",
        options=list(education_field_data.keys()),
        index=list(education_field_data.keys()).index("STEM (Science, Technology, Engineering, Math)")
    )

with col2:
    school_tier = st.selectbox(
        "Institution Tier",
        options=list(school_tier_data.keys()),
        index=list(school_tier_data.keys()).index("Tier 2 (Reputable State/Private)")
    )
    company_type = st.selectbox(
        "Current Company Type",
        options=list(company_type_data.keys()),
        index=list(company_type_data.keys()).index("Large Established Firm (Non-Tech)")
    )
    initial_gen_skill_progress = st.slider(
        "Current General Skill Acquisition Progress (%)",
        min_value=0, max_value=100, value=50, step=5, format="%d%%",
        help="Your current progress in acquiring general/portable skills (e.g., Python, data analysis)."
    ) / 100.0
    initial_spec_skill_progress = st.slider(
        "Current Firm-Specific Skill Acquisition Progress (%)",
        min_value=0, max_value=100, value=20, step=5, format="%d%%",
        help="Your current progress in acquiring firm-specific skills (e.g., proprietary software)."
    ) / 100.0

# Fixed/simulated scores for FCR components
# In a real app, these would come from real-time data analysis
st.subheader("Company Risk Factors (Simulated)")
st.info("For this demonstration, Company Risk Factors are simplified. In a production system, these would be derived from real-time data.")
col_fcr1, col_fcr2, col_fcr3 = st.columns(3)
with col_fcr1:
    s_senti = st.number_input("Sentiment Score (0-1)", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
with col_fcr2:
    s_fin = st.number_input("Financial Health Score (0-1)", min_value=0.0, max_value=1.0, value=0.8, step=0.05)
with col_fcr3:
    s_growth = st.number_input("Growth & AI-Adoption Score (0-1)", min_value=0.0, max_value=1.0, value=0.75, step=0.05)


# Calculate current risk scores
current_fexp = calculate_fexp(years_experience)
current_fhc = calculate_fhc(
    occupations_data[current_job_title]['f_role'],
    education_data[education_level]['f_level'],
    education_field_data[education_field]['f_field'],
    school_tier_data[school_tier]['f_school'],
    current_fexp
)
current_fcr = calculate_fcr(s_senti, s_fin, s_growth)
current_fus = calculate_fus(initial_gen_skill_progress, initial_spec_skill_progress, gamma_gen, gamma_spec)

current_idiosyncratic_risk = calculate_idiosyncratic_risk(current_fhc, current_fcr, current_fus, w_cr, w_us)
current_h_base = occupations_data[current_job_title]['H_base']
current_systematic_risk = calculate_systematic_risk(current_h_base, economic_climate_modifier, ai_innovation_index, w_econ, w_inno)

# Calculate current premium
current_payout = calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage)
current_p_systemic = calculate_p_systemic(current_systematic_risk, beta_systemic)
current_p_individual_systemic = calculate_p_individual_systemic(current_idiosyncratic_risk, beta_individual)
current_p_claim = calculate_p_claim(current_p_systemic, current_p_individual_systemic)
current_expected_loss = calculate_expected_loss(current_p_claim, current_payout)
current_monthly_premium = calculate_monthly_premium(current_expected_loss, loading_factor, min_monthly_premium)

st.subheader("Your Current AI Job Displacement Risk Score")
col_metrics = st.columns(3)
with col_metrics[0]:
    st.metric(label="Idiosyncratic Risk ($V_i(t)$)", value=f"{current_idiosyncratic_risk:.2f}")
with col_metrics[1]:
    st.metric(label="Systematic Risk ($H_i$)", value=f"{current_systematic_risk:.2f}")
with col_metrics[2]:
    st.metric(label="Estimated Monthly Premium", value=f"${current_monthly_premium:.2f}")

current_scores_dict = {
    'Idiosyncratic Risk': current_idiosyncratic_risk,
    'Systematic Risk': current_systematic_risk,
    'Monthly Premium': current_monthly_premium
}

st.markdown("""
The **Idiosyncratic Risk** reflects your personal vulnerability, influenced by your skills, experience,
education, and company. The **Systematic Risk** is the inherent risk of your occupation
due to broad AI advancements and economic conditions.
The **Estimated Monthly Premium** is a hypothetical cost for "AI displacement insurance"
based on these risk factors.
""")

st.divider()

# --- Career Transition Simulation Section ---
st.header("Simulate Career Transition & Skill Development")
st.markdown("""
Explore how changing your career path and acquiring new skills can mitigate your risk.
Select a target career and adjust the "Transition Progress" and "Skill Acquisition Progress"
to see the real-time impact on your risk scores and premium.
""")

target_job_title = st.selectbox(
    "Target Career Path",
    options=[job for job in occupations_data.keys() if job != current_job_title],
    index=list(occupations_data.keys()).index('Data Scientist') if 'Data Scientist' in occupations_data.keys() and 'Data Scientist' != current_job_title else 0
)

col_sim_prog = st.columns(3)
with col_sim_prog[0]:
    transition_progress_months = st.slider(
        "Transition Progress (Months)",
        min_value=0, max_value=ttv_default * 2, value=0, step=1,
        help=f"Months into your career transition. Assumes a default Time-to-Value (TTV) period of {ttv_default} months."
    )
with col_sim_prog[1]:
    sim_gen_skill_progress = st.slider(
        "Simulated General Skill Acquisition Progress (%)",
        min_value=0, max_value=100, value=int(initial_gen_skill_progress * 100), step=5, format="%d%%",
        help="Simulate increasing your general/portable skills."
    ) / 100.0
with col_sim_prog[2]:
    sim_spec_skill_progress = st.slider(
        "Simulated Firm-Specific Skill Acquisition Progress (%)",
        min_value=0, max_value=100, value=int(initial_spec_skill_progress * 100), step=5, format="%d%%",
        help="Simulate increasing your firm-specific skills."
    ) / 100.0

# Recalculate with simulated values
sim_fus = calculate_fus(sim_gen_skill_progress, sim_spec_skill_progress, gamma_gen, gamma_spec)
sim_idiosyncratic_risk = calculate_idiosyncratic_risk(current_fhc, current_fcr, sim_fus, w_cr, w_us)

target_h_base = occupations_data[target_job_title]['H_base']
sim_h_base_ttv = calculate_h_base_ttv(transition_progress_months, ttv_default, current_h_base, target_h_base)
sim_systematic_risk = calculate_systematic_risk(sim_h_base_ttv, economic_climate_modifier, ai_innovation_index, w_econ, w_inno)

sim_p_systemic = calculate_p_systemic(sim_systematic_risk, beta_systemic)
sim_p_individual_systemic = calculate_p_individual_systemic(sim_idiosyncratic_risk, beta_individual)
sim_p_claim = calculate_p_claim(sim_p_systemic, sim_p_individual_systemic)
sim_expected_loss = calculate_expected_loss(sim_p_claim, current_payout)
sim_monthly_premium = calculate_monthly_premium(sim_expected_loss, loading_factor, min_monthly_premium)

st.subheader("Simulated AI Job Displacement Risk Score")
col_sim_metrics = st.columns(3)
with col_sim_metrics[0]:
    st.metric(label="Idiosyncratic Risk ($V_i(t)$) (Simulated)", value=f"{sim_idiosyncratic_risk:.2f}",
              delta=f"{sim_idiosyncratic_risk - current_idiosyncratic_risk:.2f}")
with col_sim_metrics[1]:
    st.metric(label="Systematic Risk ($H_i$) (Simulated)", value=f"{sim_systematic_risk:.2f}",
              delta=f"{sim_systematic_risk - current_systematic_risk:.2f}")
with col_sim_metrics[2]:
    st.metric(label="Estimated Monthly Premium (Simulated)", value=f"${sim_monthly_premium:.2f}",
              delta=f"${sim_monthly_premium - current_monthly_premium:.2f}")

simulated_scores_dict = {
    'Idiosyncratic Risk': sim_idiosyncratic_risk,
    'Systematic Risk': sim_systematic_risk,
    'Monthly Premium': sim_monthly_premium
}

st.divider()

# --- Visualizations Section ---
st.header("Risk Trends Visualizations")

st.markdown("### Comparison: Current vs. Simulated Risk & Premium")
fig_comparison = plot_risk_breakdown(current_scores_dict, simulated_scores_dict)
st.plotly_chart(fig_comparison, use_container_width=True)

st.markdown("### Systematic Risk & Premium During Career Transition")
st.markdown(r"""
This chart illustrates how your **Systematic Risk** and **Monthly Premium** gradually shift
from your current job's risk profile to the target job's profile over the
**Time-to-Value (TTV)** period. This shows the benefit of career diversification.
The formula used for $H_{base}(k)$ is:
$$H_{base}(k) = \left(1 - \frac{k}{TTV}\right) \cdot H_{current} + \left(\frac{k}{TTV}\right) \cdot H_{target}$$
Where:
- $k$: Months elapsed since pathway completion.
- $TTV$: Total months in the Time-to-Value period (default: $12$).
- $H_{current}$: Base Occupational Hazard of your original industry.
- $H_{target}$: Base Occupational Hazard of your new target industry.
""")

transition_data = []
for k_month in range(0, ttv_default + 1):
    h_base_at_k = calculate_h_base_ttv(k_month, ttv_default, current_h_base, target_h_base)
    sys_risk_at_k = calculate_systematic_risk(h_base_at_k, economic_climate_modifier, ai_innovation_index, w_econ, w_inno)
    
    # Assuming Idiosyncratic Risk remains constant or changes due to fixed skill gain for this plot
    # For a dynamic Idiosyncratic Risk over transition, we'd need more complex skill progression modeling
    p_sys_at_k = calculate_p_systemic(sys_risk_at_k, beta_systemic)
    p_ind_at_k = calculate_p_individual_systemic(sim_idiosyncratic_risk, beta_individual) # Using simulated skills
    p_claim_at_k = calculate_p_claim(p_sys_at_k, p_ind_at_k)
    exp_loss_at_k = calculate_expected_loss(p_claim_at_k, current_payout)
    monthly_prem_at_k = calculate_monthly_premium(exp_loss_at_k, loading_factor, min_monthly_premium)
    
    transition_data.append({
        'Months Elapsed': k_month,
        'Systematic Risk': sys_risk_at_k,
        'Monthly Premium': monthly_prem_at_k
    })
df_transition_data = pd.DataFrame(transition_data)
fig_transition = plot_risk_over_transition(df_transition_data)
st.plotly_chart(fig_transition, use_container_width=True)


st.markdown("### Idiosyncratic Risk & Premium vs. Skill Acquisition")
st.markdown(r"""
This chart demonstrates how investing in **General Skills** can significantly reduce your
**Idiosyncratic Risk** and, consequently, your **Monthly Premium**. General skills
are broadly applicable and offer better risk reduction than firm-specific skills.
The **Upskilling Factor ($F_{US}$)** is calculated as:
$$F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))$$
Where:
- $P_{gen}(t)$: Training progress in general/portable skills ($0$ to $1$).
- $P_{spec}(t)$: Training progress in firm-specific skills ($0$ to $1$).
- $\gamma_{gen}$: Weight for general skill progress (default: $0.7$).
- $\gamma_{spec}$: Weight for firm-specific skill progress (default: $0.3$).
""")

skill_progress_data = []
for progress_percent in range(0, 101, 5):
    progress_ratio = progress_percent / 100.0
    
    # Simulate impact of general skills, assuming spec skills constant at initial value
    sim_fus_gen_impact = calculate_fus(progress_ratio, initial_spec_skill_progress, gamma_gen, gamma_spec)
    sim_idiosyncratic_risk_gen_impact = calculate_idiosyncratic_risk(current_fhc, current_fcr, sim_fus_gen_impact, w_cr, w_us)
    
    p_sys_skill_impact = calculate_p_systemic(sim_systematic_risk, beta_systemic) # systematic risk from simulation
    p_ind_skill_impact = calculate_p_individual_systemic(sim_idiosyncratic_risk_gen_impact, beta_individual)
    p_claim_skill_impact = calculate_p_claim(p_sys_skill_impact, p_ind_skill_impact)
    exp_loss_skill_impact = calculate_expected_loss(p_claim_skill_impact, current_payout)
    monthly_prem_skill_impact = calculate_monthly_premium(exp_loss_skill_impact, loading_factor, min_monthly_premium)
    
    skill_progress_data.append({
        'Skill Progress': progress_percent / 100.0,
        'Idiosyncratic Risk': sim_idiosyncratic_risk_gen_impact,
        'Monthly Premium': monthly_prem_skill_impact
    })

df_skill_progress_data = pd.DataFrame(skill_progress_data)
fig_skill = plot_idiosyncratic_risk_by_skills(df_skill_progress_data)
st.plotly_chart(fig_skill, use_container_width=True)

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.")
