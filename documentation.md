id: 685c5f367c682524b357b424_documentation
summary: AI Risk Score - V4 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Understanding and Using the Career Longevity Calculator

This codelab provides a comprehensive guide to understanding and utilizing a Streamlit application designed to estimate career longevity and associated insurance premiums.  We'll explore the application's functionality, underlying logic, and how various factors influence the final estimations. This application is crucial for both individuals seeking to understand their career prospects and insurance professionals aiming to create tailored policies.

## Introduction to Career Longevity Estimation
Duration: 00:05

This application is designed to estimate an individual's career longevity and associated risks, providing a framework for personalized insurance premium calculation.  It considers a range of factors including occupation, education, company type, and broader economic trends to offer a more nuanced prediction than traditional methods.  Understanding how these factors interact is key to appreciating the application's value.

## Application Architecture
Duration: 00:10

While we don't have a full Streamlit application code, we can infer the architecture based on the provided helper functions.  The application likely follows a standard Streamlit structure:

1.  **User Interface (Streamlit):**  Streamlit provides the interface for users to input their data (occupation, education level, etc.). This is where users will interact with the application.
2.  **Data Loading (data_loader.py):** This module loads pre-defined datasets from the `synthetic_data.py` file.  These datasets contain the baseline parameters and scaling factors for various factors influencing career longevity and risk.
3.  **Calculation Engine (Inferred from data):** This is the core logic of the application (not explicitly provided). It takes user inputs and data from the loaded datasets and performs calculations to estimate career longevity, risk factors, and insurance premiums.
4.  **Output Display (Streamlit):**  The calculated results (estimated career longevity, risk score, premium) are displayed to the user through the Streamlit interface.

## Understanding the Data
Duration: 00:15

The application relies on synthetic data to model the impact of various factors on career longevity and risk. Let's examine the key data structures:

### 1. Occupation Data (`get_occupations_data`)

```python
def get_occupations_data():
    return {
        'Data Entry Clerk': {'H_base': 80, 'f_role': 1.35},
        'Paralegal': {'H_base': 65, 'f_role': 1.10},
        'Financial Analyst': {'H_base': 50, 'f_role': 0.90},
        'Software Engineer': {'H_base': 40, 'f_role': 0.70},
        'Senior Research Scientist': {'H_base': 30, 'f_role': 0.30},
        'HR Manager': {'H_base': 60, 'f_role': 1.05},
        'Marketing Specialist': {'H_base': 55, 'f_role': 0.95},
        'Registered Nurse': {'H_base': 20, 'f_role': 0.20},
        'Management Consultant': {'H_base': 45, 'f_role': 0.80},
        'Customer Service Rep': {'H_base': 75, 'f_role': 1.20},
    }
```

*   **`H_base`:**  Represents the baseline hazard or risk associated with a particular occupation. Higher values suggest a greater inherent risk of career disruption.
*   **`f_role`:**  A scaling factor that adjusts the impact of systematic risk on the individual's career within that occupation.

### 2. Education Data (`get_education_data`)

```python
def get_education_data():
    return {
        'No Degree': {'f_level': 1.20},
        'High School': {'f_level': 1.15},
        'Associate's': {'f_level': 1.10},
        'Bachelor's': {'f_level': 1.00},
        'Master's': {'f_level': 0.90},
        'PhD': {'f_level': 0.85},
    }
```

*   **`f_level`:**  A factor reflecting the impact of the education level on an individual's resilience to career shocks.  Lower values suggest greater resilience.

### 3. Education Field Data (`get_education_field_data`)

```python
def get_education_field_data():
    return {
        'Liberal Arts/Humanities': {'f_field': 1.10},
        'Business/Management': {'f_field': 1.05},
        'Social Sciences': {'f_field': 1.05},
        'Natural Sciences': {'f_field': 0.95},
        'Tech/Engineering/Quantitative Science': {'f_field': 0.90},
    }
```

*   **`f_field`:**  A factor reflecting how the field of study influences an individual's career resilience.

### 4. School Tier Data (`get_school_tier_data`)

```python
def get_school_tier_data():
    return {
        'Tier 1 (Ivy/Top Tier)': {'f_school': 0.95},
        'Tier 2 (Reputable State/Private)': {'f_school': 1.00},
        'Tier 3 (Local/Regional)': {'f_school': 1.05},
        'Tier 4 (Online/Vocational)': {'f_school': 1.10},
    }
```

*   **`f_school`:** A factor reflecting the impact of the school tier on career progression and security.

### 5. Company Type Data (`get_company_type_data`)

```python
def get_company_type_data():
    return {
        'Startup (High Growth/High Risk)': {'F_CR': 1.15},
        'Mid-size Firm (Stable/Moderate Growth)': {'F_CR': 1.00},
        'Big Firm (Established/Lower Growth)': {'F_CR': 0.95},
        'Government/Non-Profit (Very Stable)': {'F_CR': 0.85},
    }
```

*   **`F_CR`:**  Represents the company risk factor. Higher values denote greater risk associated with the company type.

### 6. Actuarial Parameters (`get_actuarial_parameters`)

This dictionary contains various parameters used in the actuarial calculations. These include default values for salary, coverage duration, coverage percentage, beta values (systemic and individual risk), loading factors, and other economic and innovation-related factors.

##  Dissecting the Calculation Logic (Inferred)
Duration: 00:20

While the precise calculations are not given, we can deduce the underlying logic based on the provided data:

1.  **Baseline Hazard Adjustment:** The `H_base` value from the occupation data serves as a starting point for assessing career risk.
2.  **Education Level Adjustment:** The `f_level` factor from the education data modifies the baseline hazard, reflecting the protective or detrimental effect of education.
3.  **Education Field Adjustment:** The `f_field` from the education field data further refines the hazard based on the chosen field of study.
4.  **School Tier Adjustment:** The `f_school` factor adjusts the hazard based on the prestige or tier of the educational institution.
5.  **Company Risk Assessment:** The `F_CR` factor from the company type data directly influences the idiosyncratic risk component.
6.  **Systematic Risk Calculation:** The `beta_systemic_default`, `economic_climate_default`, and `ai_innovation_default` parameters, along with the `w_econ` and `w_inno` weights, determine the overall systematic risk affecting career longevity.
7.  **Idiosyncratic Risk Calculation:** The `beta_individual_default`, `F_CR`, `w_cr`, `w_us`, `gamma_gen`, and `gamma_spec` parameters contribute to the calculation of idiosyncratic risk, which represents individual-specific factors influencing career stability.
8.  **Premium Calculation:** The application likely utilizes the calculated risk scores, `annual_salary_default`, `coverage_duration_months_default`, `coverage_percentage_default`, `loading_factor_default`, and `min_premium_default` parameters to determine the appropriate insurance premium.

<aside class="positive">
The weights (e.g., `w_cr`, `w_us`, `w_econ`, `w_inno`, `gamma_gen`, `gamma_spec`) determine the relative importance of different factors in the risk calculation.  Adjusting these weights allows for fine-tuning the model to reflect different economic realities or individual circumstances.
</aside>

## Using the Application (Hypothetical)
Duration: 00:10

Imagine the Streamlit application has the following input fields:

*   **Occupation:** (Dropdown selection from `get_occupations_data().keys()`)
*   **Education Level:** (Dropdown selection from `get_education_data().keys()`)
*   **Field of Study:** (Dropdown selection from `get_education_field_data().keys()`)
*   **School Tier:** (Dropdown selection from `get_school_tier_data().keys()`)
*   **Company Type:** (Dropdown selection from `get_company_type_data().keys()`)
*   **Economic Climate:** (Numerical input, default `economic_climate_default`)
*   **AI Innovation:** (Numerical input, default `ai_innovation_default`)

After the user fills in these fields and clicks "Calculate," the application performs the calculations and displays the following:

*   **Estimated Career Longevity (Years):**  A numerical estimate of how long the individual is likely to remain in their chosen career.
*   **Risk Score:** A quantitative measure of the overall risk associated with the individual's career profile.
*   **Recommended Insurance Premium:** The calculated insurance premium based on the risk assessment and other actuarial parameters.

## Expanding the Application
Duration: 00:10

This application can be further enhanced by:

*   **Incorporating Real-World Data:**  Replace the synthetic data with real-world datasets on career transitions, salary trends, and economic indicators for greater accuracy.
*   **Adding More Factors:** Include factors such as geographic location, age, gender, and specific skills to refine the risk assessment.
*   **Implementing Machine Learning Models:**  Train machine learning models on historical data to predict career longevity and risk more accurately.
*   **Visualizing Results:** Use Streamlit's charting capabilities to visualize the impact of different factors on career longevity and premium calculations.

## Conclusion
Duration: 00:05

This codelab has provided a detailed exploration of the Career Longevity Calculator, from its underlying data structures to its potential applications and future enhancements. By understanding the principles outlined here, developers can build upon this foundation to create even more sophisticated and personalized career and insurance planning tools.
