
# Technical Specifications for a Streamlit Application: Career Path Diversification Tool

## Overview

The "Career Path Diversification Tool" is a Streamlit application designed to help users understand and mitigate their exposure to systematic AI risk in their careers. It operationalizes the core concept of **Systematic Risk Exposure Mitigation** or **Career Path Diversification** as detailed in the provided research document "AI-Q Score: A Multi-Factor Parametric Framework for Quantifying and Mitigating AI-Driven Job Displacement Risk".

The application enables users to:
1.  **Input their current career profile**: Users will provide details about their current job, education, experience, and company.
2.  **View their current AI job displacement risk**: The application will calculate and display their current Idiosyncratic Risk and Systematic Risk scores, along with an estimated monthly "AI displacement insurance" premium.
3.  **Explore alternative career paths**: Based on a synthetic dataset mimicking O*NET, the application will suggest alternative career options with potentially lower systematic risk.
4.  **Simulate career transitions**: Users can select a target career path and simulate the effort (e.g., skill acquisition, transition time) required to move to it, observing the real-time impact on their risk scores and insurance premium.
5.  **Visualize risk trends**: Interactive charts will illustrate how risk scores and premiums change with career transition efforts and skill development.

Through these features, the application demonstrates how proactive career choices and skill development can significantly influence an individual's financial risk profile in an AI-driven labor market.

## Step-by-Step Development Process

The development of the Streamlit application will follow these logical steps:

1.  **Environment Setup**:
    *   Create a dedicated Python virtual environment.
    *   Install necessary libraries: `streamlit`, `pandas`, `numpy`, `plotly`.
    *   Create `app.py` as the main application file and a `utils` directory for helper modules (e.g., `utils/data_loader.py`, `utils/risk_calculator.py`, `utils/visualization_utils.py`).

2.  **Synthetic Data Generation**:
    *   Design and create a `synthetic_data.py` script or a JSON/CSV file within `utils/data/` to house the synthetic dataset. This dataset will mimic O*NET-like information, including:
        *   Job titles and their associated baseline Systematic Risk scores ($H_{base}$) and Role Multipliers ($f_{role}$).
        *   Education levels and corresponding Education Level Factors ($f_{level}$).
        *   Education fields and corresponding Education Field Factors ($f_{field}$).
        *   Institution tiers and corresponding Institution Tier Factors ($f_{school}$).
        *   Company types and Company Risk Factors ($F_{CR}$).
        *   General/Portable skills and Firm-Specific skills categories.
    *   The `data_loader.py` module will load this data into Pandas DataFrames or Python dictionaries for easy access within the application.

3.  **Core Risk Calculation Logic Implementation**:
    *   Develop the `risk_calculator.py` module. This module will encapsulate all mathematical formulas derived from the AI-Q Score model. Each formula will be implemented as a dedicated Python function.
    *   Ensure proper handling of inputs and outputs for each function (e.g., current job details, skill progress, environmental modifiers).
    *   Thoroughly test each calculation function with example values from the document (e.g., Alex Chen, Dr. Brenda Smith scenarios) to verify correctness.

4.  **User Interface (UI) Development - Input Forms**:
    *   In `app.py`, design the initial input forms using Streamlit widgets (`st.text_input`, `st.number_input`, `st.selectbox`, `st.slider`).
    *   Allow users to input their current job title, years of experience, education level, education field, school tier, company type, and initial training progress (if any).
    *   Include sliders for "Economic Climate Modifier" ($M_{econ}$) and "AI Innovation Index" ($I_{AI}$) to allow users to experiment with environmental factors.

5.  **Initial Risk Calculation and Display**:
    *   Based on user inputs, call the relevant functions from `risk_calculator.py` to compute the current Idiosyncratic Risk ($V_i(t)$), Systematic Risk ($H_i$), Annual Claim Probability ($P_{claim}$), Expected Loss ($E[Loss]$), and Monthly Premium ($P_{monthly}$).
    *   Display these calculated values prominently using `st.metric` or `st.markdown`.

6.  **Career Transition Simulation UI**:
    *   Add a section for career transition simulation.
    *   Include a `st.selectbox` for selecting a "Target Career Path" from the synthetic dataset.
    *   Implement `st.slider` widgets for "Transition Progress" (from 0% to 100%) and "Skill Acquisition Progress" (for general and firm-specific skills, from 0% to 100%).
    *   Include a `st.number_input` for "Time to Value (TTV) Period" (defaulting to 12 months).

7.  **Dynamic Risk Calculation and Visualization**:
    *   As users interact with the simulation widgets, dynamically re-calculate the $H_{base}(k)$, $V_i(t)$, $H_i$, $P_{claim}$, $E[Loss]$, and $P_{monthly}$ values.
    *   In `visualization_utils.py`, create functions to generate interactive charts using Plotly:
        *   **Line Chart**: Show $H_{base}(k)$ and $P_{monthly}$ over the TTV period as "Transition Progress" changes.
        *   **Bar Chart**: Compare current and target Systematic Risk and the impact on premium.
        *   **Scatter Plot / Line Chart**: Illustrate how Idiosyncratic Risk and premium change with "Skill Acquisition Progress".
    *   Integrate these charts into `app.py` using `st.plotly_chart`.

8.  **Explanatory Markdown and Tooltips**:
    *   Incorporate detailed `st.markdown` explanations for each section and concept, defining terms and providing context.
    *   Use `st.expander` for "behind-the-scenes" details or formula breakdowns.
    *   Add `st.help` or custom tooltips using `st.info` or `st.sidebar` for more complex concepts or parameters, guiding users through the data exploration process.

9.  **Refinement and Testing**:
    *   Review UI for clarity and responsiveness.
    *   Test all interactions and calculations thoroughly to ensure accuracy and robustness.
    *   Optimize performance for smoother user experience.

## Core Concepts and Mathematical Foundations

The application relies heavily on the mathematical framework presented in the "AI-Q Score" document. Below are the key concepts and their corresponding LaTeX formulae.

### Idiosyncratic Risk ($V_i(t)$)
The Idiosyncratic Risk, or Vulnerability, is a measure of an individual's personal, manageable vulnerability to job displacement. It is calculated as a composite of three distinct factors: Human Capital ($FHC$), Employer's Stability (Company Risk Factor, $F_{CR}$), and Proactive Upskilling efforts ($F_{US}$). The general form is:
$$
V_i(t) = f(FHC, FCR, FUS)
$$
We model this as a weighted product for the raw score ($V_{raw}$):
$$
V_{raw} = FHC \cdot (w_{CR} \cdot FCR + w_{US} \cdot FUS)
$$
The final score is then normalized to a scale of 0-100:
$$
V_i(t) = \min(100.0, \max(5.0, V_{raw} \cdot 50.0))
$$
Where:
- $V_i(t)$: Final Idiosyncratic Risk score at time $t$
- $FHC$: Human Capital Factor
- $FCR$: Company Risk Factor
- $FUS$: Upskilling Factor
- $w_{CR}$: Weight for Company Risk Factor (e.g., $0.4$)
- $w_{US}$: Weight for Upskilling Factor (e.g., $0.6$)
- $V_{raw}$: Raw Idiosyncratic Risk score before normalization

This formula quantifies how an individual's unique attributes and proactive efforts contribute to their overall job displacement risk, emphasizing aspects within their control.

### Human Capital Factor ($FHC$)
The Human Capital Factor assesses an individual's foundational resilience based on their educational and professional background. It is calculated as a weighted product of several sub-factors:
$$
FHC = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
$$
Where:
- $FHC$: Human Capital Factor
- $f_{role}$: Role Multiplier, reflecting job title vulnerability (e.g., $1.35$ for Data Entry Clerk, $0.3$ for Senior Research Scientist)
- $f_{level}$: Education Level Factor, based on highest education attained (e.g., $0.85$ for PhD, $1.00$ for Bachelor's)
- $f_{field}$: Education Field Factor, rewarding transferable skills (e.g., $0.90$ for Tech/Engineering, $1.10$ for Liberal Arts)
- $f_{school}$: Institution Tier Factor, a proxy for training quality (e.g., $0.95$ for Tier 1, $1.00$ for Tier 2)
- $f_{exp}$: Experience Factor, a decaying function of years of experience ($Yrs$), calculated as $1 - (0.015 \cdot \min(Yrs, 20))$.

This formula determines a baseline vulnerability score based on immutable aspects of a user's profile, providing a fundamental measure of their resilience to AI-driven changes.

### Company Risk Factor ($F_{CR}$)
The Company Risk Factor quantifies the stability and growth prospects of the individual's current employer, analogous to a corporate credit rating. It is a composite of sentiment, financial health, and growth/AI adoption scores.
$$
F_{CR} = w_1 \cdot S_{senti} + w_2 \cdot S_{fin} + w_3 \cdot S_{growth}
$$
Where:
- $F_{CR}$: Company Risk Factor
- $S_{senti}$: Sentiment Score (e.g., from real-time NLP analysis)
- $S_{fin}$: Financial Health Score (e.g., from financial statements)
- $S_{growth}$: Growth \& AI-Adoption Score (e.g., from R\&D spending, hiring trends for AI roles)
- $w_1, w_2, w_3$: Calibration weights (e.g., sum to $1.0$, typically equal if not specified otherwise, such as $0.33$ each).

This formula integrates external factors related to the employer's health and adaptability to AI, which directly influence an individual's risk.

### Upskilling Factor ($F_{US}$)
The Upskilling Factor measures an individual's proactive training efforts, differentiating between general/portable skills and firm-specific skills, rewarding the former more heavily for risk reduction.
$$
F_{US} = 1 - (\gamma_{gen} \cdot P_{gen}(t) + \gamma_{spec} \cdot P_{spec}(t))
$$
Where:
- $F_{US}$: Upskilling Factor
- $P_{gen}(t)$: Training progress (from $0$ to $1$) in general/portable skills (e.g., Python, data analysis) at time $t$
- $P_{spec}(t)$: Training progress (from $0$ to $1$) in firm-specific skills (e.g., proprietary software) at time $t$
- $\gamma_{gen}$: Weight for general skill progress (e.g., $0.7$)
- $\gamma_{spec}$: Weight for firm-specific skill progress (e.g., $0.3$)

This formula quantifies the impact of continuous learning on an individual's risk, highlighting the strategic benefit of acquiring widely applicable skills.

### Systematic Risk ($H_i$)
The Systematic Risk score is a dynamic index reflecting the macro-level automation hazard inherent to an entire occupation, adjusted by broader environmental factors like the economic climate and velocity of AI innovation.
$$
H_i = H_{base}(t) \cdot (w_{econ} \cdot M_{econ} + w_{inno} \cdot I_{AI})
$$
Where:
- $H_i$: Final Systematic Risk score
- $H_{base}(t)$: Base Occupational Hazard at time $t$ (can change over time due to career transition)
- $M_{econ}$: Economic Climate Modifier (a normalized index, e.g., $0.8$ to $1.2$)
- $I_{AI}$: AI Innovation Index (a normalized momentum index, e.g., $0.8$ to $1.2$)
- $w_{econ}$: Weight for Economic Climate Modifier (e.g., $0.5$)
- $w_{inno}$: Weight for AI Innovation Index (e.g., $0.5$)

This formula captures the broader, unavoidable market risks that influence job displacement, providing a macro-level perspective on risk.

### Base Occupational Hazard with Transition Time-to-Value (TTV) Modifier ($H_{base}(k)$)
When an individual undertakes a career transition, their base occupational hazard does not instantly switch to the target industry's score. Instead, it's a time-weighted average of the old and new industry risks over a defined TTV period.
$$
H_{base}(k) = \left(1 - \frac{k}{TTV}\right) \cdot H_{current} + \left(\frac{k}{TTV}\right) \cdot H_{target}
$$
Where:
- $H_{base}(k)$: Base Occupational Hazard at month $k$ during transition
- $k$: Number of months elapsed since pathway completion
- $TTV$: Total number of months in the Time-to-Value period (e.g., $12$)
- $H_{current}$: Base Occupational Hazard of the individual's original industry
- $H_{target}$: Base Occupational Hazard of the new target industry

This formula is critical for simulating the real-world impact of career path diversification, showing a gradual shift in systematic risk as a transition progresses.

### Annual Claim Probability ($P_{claim}$)
The annual probability of a claim (job displacement) is modeled as the joint probability of a systemic event occurring in the individual's industry and that event leading to a loss for that specific individual.
$$
P_{claim} = P_{systemic} \cdot P_{individual|systemic}
$$
The two conditional probabilities are defined as:
$$
P_{systemic} = \frac{H_i}{100} \cdot \beta_{systemic}
$$
$$P_{individual|systemic} = \frac{V_i(t)}{100} \cdot \beta_{individual}
$$
Where:
- $P_{claim}$: Annual Claim Probability
- $P_{systemic}$: Probability of a systemic displacement event
- $P_{individual|systemic}$: Conditional probability of job loss given a systemic event
- $H_i$: Systematic Risk Score
- $V_i(t)$: Idiosyncratic Risk Score
- $\beta_{systemic}$: Systemic Event Base Probability (e.g., $0.10$)
- $\beta_{individual}$: Individual Loss Base Probability (e.g., $0.50$)

This set of formulae converts the abstract risk scores into a concrete probability of job displacement, forming the basis for financial calculations.

### Total Payout Amount ($L_{payout}$)
This is the total financial benefit defined by the policy terms that would be paid out if a claim is triggered, reflecting income replacement.
$$
L_{payout} = \left(\frac{\text{Annual Salary}}{12}\right) \cdot \text{Coverage Duration} \cdot \text{Coverage Percentage}
$$
Where:
- $L_{payout}$: Total Payout Amount
- Annual Salary: User's annual income (e.g., $90,000$)
- Coverage Duration: Number of months of income replacement (e.g., $6$ months)
- Coverage Percentage: Percentage of salary replaced (e.g., $25\%$)

This calculation defines the potential financial impact of a job displacement event, which is essential for actuarial pricing.

### Annual Expected Loss ($E[Loss]$)
The annual expected financial loss is the total payout amount multiplied by the probability of a claim.
$$
E[Loss] = P_{claim} \cdot L_{payout}
$$
Where:
- $E[Loss]$: Annual Expected Loss
- $P_{claim}$: Annual Claim Probability
- $L_{payout}$: Total Payout Amount

This formula quantifies the anticipated financial cost of job displacement over a year.

### Final Monthly Premium ($P_{monthly}$)
The monthly premium is the final cost to the individual, derived from the annual expected loss, adjusted by a loading factor, and floored at a minimum premium.
$$
P_{monthly} = \max\left(\frac{E[Loss] \cdot \lambda}{12}, P_{min}\right)
$$
Where:
- $P_{monthly}$: Final Monthly Premium
- $E[Loss]$: Annual Expected Loss
- $\lambda$: Loading Factor, an insurance multiplier for administrative costs and profit margin (e.g., $1.5$)
- $P_{min}$: Minimum Monthly Premium (e.g., $20.00$)

This formula translates the complex risk assessments into a practical, actionable financial figure for the user.

## Required Libraries and Dependencies

The Streamlit application will primarily rely on the following Python libraries:

1.  **`streamlit`**: The core framework for building interactive web applications in Python.
    *   **Usage**: All UI components (inputs, outputs, layouts), reactive data flow, and application execution.
    *   **Specific Functions/Modules**: `streamlit.set_page_config`, `st.title`, `st.header`, `st.subheader`, `st.sidebar`, `st.expander`, `st.markdown`, `st.text_input`, `st.number_input`, `st.selectbox`, `st.slider`, `st.button`, `st.metric`, `st.plotly_chart`, `st.info`, `st.help`.
    *   **Import Example**: `import streamlit as st`

2.  **`pandas`**: Essential for efficient data manipulation and analysis, especially for handling the synthetic dataset.
    *   **Usage**: Loading and structuring the synthetic O*NET-like data, performing lookups for job attributes, and organizing data for calculations and visualizations.
    *   **Specific Functions/Modules**: `pandas.DataFrame`, `pd.read_csv` (if data is external CSV), `df.loc`, `df.apply`.
    *   **Import Example**: `import pandas as pd`

3.  **`numpy`**: For numerical operations, especially mathematical computations within the risk calculation functions.
    *   **Usage**: Implementing mathematical functions like `min`, `max`, and potentially array operations for more complex calculations if needed.
    *   **Specific Functions/Modules**: `numpy.min`, `numpy.max`, `numpy.power` (or Python's `**` operator).
    *   **Import Example**: `import numpy as np`

4.  **`plotly.express`**: For creating interactive and visually appealing charts and plots.
    *   **Usage**: Generating dynamic line charts, bar graphs, and scatter plots to visualize trends in risk scores and premiums. Plotly's interactivity (zoom, pan, tooltips) aligns with the `visualizationDetails` requirement.
    *   **Specific Functions/Modules**: `plotly.express.line`, `plotly.express.bar`.
    *   **Import Example**: `import plotly.express as px`

## Implementation Details

### Data Structures

The synthetic dataset will be represented using Python dictionaries or Pandas DataFrames, structured as follows:

*   **`occupations_data`**: A dictionary or DataFrame mapping job titles to their baseline systematic risk scores ($H_{base}$), and $f_{role}$ values.
    *   Example: `{'Paralegal': {'H_base': 65, 'f_role': 1.35}, 'Senior Research Scientist': {'H_base': 30, 'f_role': 0.3}, ...}`
*   **`education_data`**: A dictionary or DataFrame mapping education levels and fields to their respective multipliers ($f_{level}$, $f_{field}$).
    *   Example: `{'Bachelor\'s': {'f_level': 1.00}, 'PhD': {'f_level': 0.85}, 'Liberal Arts/Humanities': {'f_field': 1.10}, 'Tech/Engineering/Quantitative Science': {'f_field': 0.90}, ...}`
*   **`school_tier_data`**: A dictionary mapping institution tiers to $f_{school}$ values.
    *   Example: `{'Tier 1': 0.95, 'Tier 2': 1.00, ...}`
*   **`company_type_data`**: A dictionary mapping company types (e.g., 'Big firm', 'Mid-size firm') to $F_{CR}$ values.
    *   Example: `{'Big firm': 0.95, 'Mid-size firm': 1.00, ...}`
*   **`actuarial_parameters`**: A dictionary holding constant policy parameters like Annual Salary, Coverage Percentage, Coverage Duration, $\beta_{systemic}$, $\beta_{individual}$, $\lambda$, and $P_{min}$.

These data structures will be loaded via `utils/data_loader.py`.

### Core Logic Modules

1.  **`utils/data_loader.py`**:
    *   Function: `load_synthetic_data()`: Responsible for loading all the pre-defined synthetic datasets (occupations, education, company types, actuarial params) into appropriate Python data structures (DataFrames, dictionaries).

2.  **`utils/risk_calculator.py`**:
    *   **Functions for $FHC$ components**:
        *   `calculate_fexp(years_experience)`
    *   **Functions for main factors**:
        *   `calculate_fhc(role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value)`
        *   `calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)`: Note: For this application, $S_{senti}, S_{fin}, S_{growth}$ will be simulated/fixed input or chosen from simplified options, as their calculation is complex. Weights $w_1, w_2, w_3$ can be set to $0.33$ for simplicity if not provided.
        *   `calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec)`
    *   **Functions for risk scores**:
        *   `calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us)`
        *   `calculate_h_base_ttv(k, ttv, h_current, h_target)`
        *   `calculate_systematic_risk(h_base_t, mecon, iai, w_econ, w_inno)`
    *   **Functions for premium calculation**:
        *   `calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage)`
        *   `calculate_p_systemic(h_i, beta_systemic)`
        *   `calculate_p_individual_systemic(v_i_t, beta_individual)`
        *   `calculate_p_claim(p_systemic, p_individual_systemic)`
        *   `calculate_expected_loss(p_claim, lpayout)`
        *   `calculate_monthly_premium(expected_loss, loading_factor, min_premium)`

3.  **`utils/visualization_utils.py`**:
    *   `plot_risk_over_transition(df_transition_data)`: Generates a Plotly line chart showing how Systematic Risk and Monthly Premium evolve over the TTV period.
    *   `plot_idiosyncratic_risk_by_skills(df_skill_data)`: Generates a Plotly line chart or bar chart showing the impact of skill acquisition on Idiosyncratic Risk and premium.
    *   `plot_risk_breakdown(current_risk_scores, simulated_risk_scores)`: Generates a bar chart comparing current and simulated risk components.

### Main Application Flow (`app.py`)

1.  **Page Configuration**: `st.set_page_config` for wide mode and title.
2.  **Load Data**: Call `data_loader.load_synthetic_data()` to get all necessary lookup tables and parameters.
3.  **Sidebar for Parameters**:
    *   Sliders for global environmental modifiers ($M_{econ}$, $I_{AI}$).
    *   Inputs for actuarial parameters (Annual Salary, Coverage %, Duration, $\lambda$, $P_{min}$) allowing users to adjust policy terms.
4.  **Current Profile Section**:
    *   Input widgets for user's current job details (Role, Experience, Education Level, Field, School Tier, Company Type, Initial Skill Progress).
    *   Display `st.metric` for Current Idiosyncratic Risk, Current Systematic Risk, and Current Monthly Premium.
5.  **Career Transition Simulation Section**:
    *   `st.selectbox` for `Target Career Path`.
    *   `st.slider` for `Transition Progress` (0-12 months typically for TTV).
    *   `st.slider` for `General Skill Progress` and `Firm-Specific Skill Progress`.
    *   Display `st.metric` for Simulated Systematic Risk, Simulated Idiosyncratic Risk (after skill change), and Simulated Monthly Premium.
    *   Use `st.expander` for a detailed breakdown of how each factor (FHC, FCR, FUS, Hbase) changes.
6.  **Visualizations Section**:
    *   Display charts generated by `visualization_utils.py` showing risk and premium trends based on user interactions.
7.  **Conceptual Explanation Section**:
    *   Dedicated `st.expander` sections or `st.markdown` areas to explain "Systematic Risk Exposure Mitigation" and "Career Path Diversification" with definitions, practical examples, and relevant formulae (as detailed in the "Core Concepts" section).
    *   Cross-reference the concepts with the interactive elements of the application.
8.  **Help and Documentation**: Inline `st.info` or `st.help` for complex terms.

## User Interface Components

The application will leverage Streamlit's rich set of interactive widgets and display elements to create an intuitive user experience.

### Input Components

*   **`st.selectbox`**: For categorical selections like Job Title, Education Level, Education Field, School Tier, Company Type, and Target Career Path.
    *   *Example*: `current_job = st.selectbox("Your Current Job Title", options=list(occupation_data.keys()))`
*   **`st.number_input`**: For numerical inputs that need precise values, e.g., Annual Salary.
    *   *Example*: `annual_salary = st.number_input("Your Annual Salary", min_value=10000, value=90000, step=5000)`
*   **`st.slider`**: For continuous numerical inputs with a defined range, allowing for easy experimentation. Used for Years of Experience, Skill Acquisition Progress (General/Firm-Specific), Transition Progress (months), Economic Climate Modifier, and AI Innovation Index.
    *   *Example*: `years_exp = st.slider("Years of Professional Experience", min_value=0, max_value=40, value=10)`
*   **`st.checkbox`**: To toggle specific features or assumptions, if applicable (e.g., "Assume neutral environmental modifiers").

### Output Components

*   **`st.metric`**: For displaying key numerical results like current/simulated risk scores and monthly premiums. Provides a clear visual indication of value and change.
    *   *Example*: `st.metric(label="Your Current Monthly Premium", value=f"${current_premium:.2f}")`
*   **`st.markdown`**: For rendering all textual explanations, formula presentations, and general application content. Crucial for documentation and conceptual explanations.
    *   *Example*: `st.markdown("### Systematic Risk Exposure Mitigation")`
*   **`st.dataframe` / `st.table`**: To optionally display underlying data or intermediate calculation results for transparency.
*   **`st.plotly_chart`**: For embedding interactive Plotly visualizations.
    *   *Example*: `st.plotly_chart(fig, use_container_width=True)`

### Interactive Elements

*   **Annotations & Tooltips**: Plotly charts natively support tooltips on hover, which will be configured to display detailed insights about data points (e.g., specific risk values at different transition points). `st.info` or `st.expander` will serve as conceptual tooltips for Streamlit text.
*   **Real-time Updates**: Streamlit's execution model automatically re-runs the script on widget interaction, providing real-time updates to calculations and visualizations without explicit refresh buttons.
*   **`st.expander`**: To collapse and expand sections of content, useful for detailed explanations of formulas or background data without cluttering the main view.
*   **`st.sidebar`**: To house global parameters or navigation, keeping the main content area focused.

This comprehensive set of components will ensure the application is both functional and user-friendly, effectively demonstrating the underlying risk concepts.


### Appendix Code

```code
Vi(t) = f (FHC, FCR, FUS)
FHC = frole flevel ffield fschool fexp
FCR = W1 · Ssenti + W2. Sfin + W3. Sgrowth
FUS = 1 - (ygen Pgen(t) + Yspec Pspec(t))
Hi Hbase (t) (Wecon Mecon + Winno. IAI)
Hbase (k) = (1-k/TTV).Hcurrent + (k/TTV).Htarget
Mecon = f(GDP Growth, Sector Employment, Interest Rates)
IAI = f (VC Funding, R&D Spend, Public Salience)
Pclaim Psystemic Pindividual systemic
Psystemic Hi / 100 Bsystemic
Pindividual systemic Vi(t) / 100 Bindividual
Pmonthly = max(E[Loss] · λ / 12, Pmin)

Raw Score: Vraw = FHC (WCRFCR+WUS. FUS)
Final Score: Vi(t) = min(100.0, max (5.0, Vraw 50.0))
For this calculation, we will use the weights defined in the software
specification: WCR = 0.4 and wus = 0.6.

Human Capital Factor Calculation:
Sub-Factor   Formula / Lookup
Role (frole)   ROLE_MULTIPLIERS
Level (flevel)   EDUCATION_LEVEL
Field (ffield)   EDUCATION_FIELD
School (fschool)   SCHOOL_TIER
Experience (fexp)   1-(0.015min (Yrs, 20))
PRODUCT (FHC)  (Multiply all above)

Alex: Looks up 'Big firm' → FCR = 0.95
Brenda: Looks up 'Mid-size firm' → FCR = 1.00
Formula: FUS = 1 - (0.7 Pidio (t))
Calculation (Both Personas): 1 - (0.7 0.0) = 1.0
Persona A: Alex Chen (Paralegal).
(1) Vraw = 1.262 (0.40.95 +0.6 1.0) = 1.237
(2) Vi(t) = min(100.0, max(5.0, 1.237 50.0)) = 61.85
Persona B: Dr. Brenda Smith (Research Scientist).
(1) Vraw = 0.192 (0.41.00 +0.6 1.0) = 0.192
(2) Vi(t) = min(100.0, max(5.0, 0.192 50.0)) = 9.6

Alex's New FUS: 1- (0.7 0.5) = 0.65
Alex's New Vraw: 1.262 (0.40.95 +0.6 0.65) = 0.972
Alex's New Final Score: min(100.0, max(5.0, 0.972-50.0)) = 48.6

Hi = Hbase(t)(Wecon Mecon+Winno IAI), with weights Wecon = 0.5 and winno = 0.5.

Alex (Legal): Hbase = 65
Brenda (Healthcare): Hbase = 30
Economic Climate Modifier (Mecon): 1.0
AI Innovation Index (IAI): 1.0
Hi = Hbase (0.5. Mecon +0.5 IAI).
Persona A: Alex Chen (Paralegal). H₁ = 65 (0.5 1.0+0.5 1.0) = 65. (1.0) = 65.0
Persona B: Dr. Brenda Smith (Research Scientist). Hi = 30. (0.5. 1.0+0.5 1.0) = 30 (1.0) = 30.0

Calculate Alex's new Hbase (t) to Healthcare:
Hbase (6) = (1-k/TTV)·Hcurrent + (k/TTV)·Htarget
Hbase (6) = (1-6/12)·65+(6/12)·30 = (0.5)·65+(0.5)·30 = 32.5+ 15 = 47.5
Calculate Alex's new Final Score (Hi): (Assuming environmental modifiers are still 1.0)
H₁ = 47.5 (1.0) = 47.5
Hbase = Htarget = 30

Calculate Alex's new Final Score (H₁): H₁ = 30 (1.0) = 30.0

Persona A (Alex Chen): Idiosyncratic Risk (Vi): 61.85, Systematic Risk (Hi): 65.0
Persona B (Dr. Brenda Smith): Idiosyncratic Risk (Vi): 9.6, Systematic Risk (Hi): 30.0

Annual Salary: $90,000
Coverage Percentage: 25%
Coverage Duration: 6 months
Systemic Event Base Probability (ẞsystemic): 0.10 (10%)
Individual Loss Base Probability (βindividual): 0.50 (50%)
Loading Factor (λ): 1.5
Minimum Premium (Pmin): $20.00

Formula: Lpayout = ( (Annual Salary) / 12) · Coverage Duration · Coverage Percentage
Calculation: ($90,000 / 12) · 6 · 0.25 = $7,500
$7,500 · 1.5 = $11, 250 (Note: The document has 1.5 as part of the initial payout calc, which seems to be the loading factor. Clarified in the text)

Formula: pclaim = (Hi / 100 · Bsystemic) · (Vi / 100 · Bindividual)
Persona A: Alex Chen. Pclaim = (65.0 / 100 · 0.10) · (61.8 / 100 · 0.50) = (0.065) · (0.30925) = 0.0201 (or 2.01%)
Persona B: Dr. Brenda Smith. Pclaim = (30.0 / 100 · 0.10) · (9.6 / 100 · 0.50) = (0.03) · (0.048) = 0.00144 (or 0.144%)

Formula: E[Loss] = Pclaim · Lpayout
Persona A: Alex Chen. E[Loss] = 0.0201 · $11, 250 = $226.13
Persona B: Dr. Brenda Smith. E[Loss] = 0.00144 · $11, 250 = $16.20

Formula: Pmonthly = max(E[Loss] · λ / 12, Pmin)
Persona A: Alex Chen. Pmonthly = max($226.13·1.5 / 12, $20.00) = max($28.27, $20.00) = $28.27
Persona B: Dr. Brenda Smith. Pmonthly = max($16.20·1.5 / 12, $20.00) = max($2.03, $20.00) = $20.00
```