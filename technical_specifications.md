
## Overview

This Streamlit application aims to educate users about their potential job displacement risk due to AI by calculating an "AI-Q Score". This score is based on user input regarding their occupation, education, company stability, and upskilling efforts. The application provides visualizations showing risk components and allows users to simulate mitigation strategies.

## Step-by-Step Generation Process

1.  **Import Libraries:** Import necessary libraries, including Streamlit for the user interface, Pandas for data handling, and Plotly for visualizations.

    ```python
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    ```

2.  **Define Risk Calculation Functions:** Create functions to calculate the Systematic Risk, Idiosyncratic Risk, and the overall AI-Q score. These functions will take user inputs as arguments.  Refer to the attached document for formula details.

3.  **Create User Input Form:** Use Streamlit's `st.form` to create a form where users can input their information.  Include input fields for:

    *   Occupation (text input or selectbox)
    *   Education Level (selectbox)
    *   Company Stability (slider or selectbox)
    *   Upskilling Level (slider)

    Example:

    ```python
    with st.form("risk_assessment"):
        occupation = st.text_input("Occupation")
        education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        company_stability = st.slider("Company Stability (1-10)", 1, 10)
        upskilling_level = st.slider("Upskilling Efforts (1-10)", 1, 10)
        submitted = st.form_submit_button("Calculate Risk")
    ```

4.  **Calculate Risk Scores:** When the form is submitted, retrieve the user inputs and use the risk calculation functions to determine the Systematic Risk, Idiosyncratic Risk, and the AI-Q Score.

5.  **Create Visualizations:**  Use Plotly to generate a bar chart visualizing the breakdown of the AI-Q Score into Systematic and Idiosyncratic Risk components. Also, display the individual factor contributions (e.g., education, company stability).
    For line charts to simulate mitigation, you'll need to recalculate the scores as users adjust parameters. Use `st.session_state` to persist initial risk values as mitigation scenarios are explored.

    ```python
    if submitted:
        # Calculate risk scores (replace with actual calculation logic)
        systematic_risk = calculate_systematic_risk(occupation)
        idiosyncratic_risk = calculate_idiosyncratic_risk(education_level, company_stability, upskilling_level)
        ai_q_score = systematic_risk + idiosyncratic_risk

        # Create a Pandas DataFrame for the bar chart
        data = {'Risk Component': ['Systematic Risk', 'Idiosyncratic Risk'],
                'Score': [systematic_risk, idiosyncratic_risk]}
        df = pd.DataFrame(data)

        # Create the bar chart using Plotly
        fig = px.bar(df, x='Risk Component', y='Score', title='AI-Q Risk Breakdown')
        st.plotly_chart(fig)

        # Simulation example
        upskilling_change = st.slider("Adjust Upskilling Level", 1, 10, upskilling_level)
        new_idiosyncratic_risk = calculate_idiosyncratic_risk(education_level, company_stability, upskilling_change)
        mitigation_data = {'Risk Component': ['Systematic Risk', 'Idiosyncratic Risk (Original)', 'Idiosyncratic Risk (Mitigated)'],
                        'Score': [systematic_risk, idiosyncratic_risk, new_idiosyncratic_risk]}
        mitigation_df = pd.DataFrame(mitigation_data)
        mitigation_fig = px.bar(mitigation_df, x='Risk Component', y='Score', title='Risk Mitigation Simulation')
        st.plotly_chart(mitigation_fig)

        st.write(f"AI-Q Score: {ai_q_score}")

    def calculate_systematic_risk(occupation):
        # This is a placeholder; in a real application, it would use a more complex calculation.
        risk_mapping = {
            "Data Entry Clerk": 80,
            "Software Engineer": 30,
            "Senior Research Scientist": 10,
            "Paralegal": 65 #from the attached document
        }

        #If the input does not match return a neutral value to avoid an error
        return risk_mapping.get(occupation,50)

    def calculate_idiosyncratic_risk(education, stability, upskilling):
        # Education Level Factor (Simplified)
        education_factor = {
            "High School": 70,
            "Bachelor's": 50,
            "Master's": 30,
            "PhD": 10
        }[education]

        # Combine factors (Simplified - adjust as needed)
        risk = education_factor + (10 - stability) * 5 + (10 - upskilling) * 2
        return risk
    ```

6.  **Implement Simulation:** Add sliders or other input widgets that allow users to modify their inputs (e.g., upskilling level).  Recalculate the risk scores and update the visualizations in real-time to demonstrate the impact of these changes.

7.  **Add Documentation:** Include `st.markdown` to provide explanations of each input field, the risk calculation process, and the meaning of the AI-Q Score.  Provide tooltips for the visualizations to further explain the data.

    Example:

    ```python
    st.markdown("## About the AI-Q Score")
    st.markdown("This application calculates your potential job displacement risk due to AI.  Input your information below:")

    st.sidebar.markdown("### Systematic Risk")
    st.sidebar.markdown("The risk associated with your *occupation* due to AI automation, inspired by concept of Systematic Risk")

    st.sidebar.markdown("### Idiosyncratic Risk")
    st.sidebar.markdown("The risk associated with your individual *vulnerability* due to AI automation, which is inspired by the concept of Idiosyncratic Risk.")
    ```

## Important Definitions, Examples, and Formulae

*   **AI-Q Score:** A numerical representation of an individual's overall risk of job displacement due to AI.  It is the sum of Systematic and Idiosyncratic Risk.

    *   *Formula:*  AI-Q Score = Systematic Risk + Idiosyncratic Risk

*   **Systematic Risk (H or H<sub>i</sub>):** Represents the risk inherent to a particular occupation due to automation. This is a dynamic index reflecting the macro-level automation hazard of an occupation, modified by prevailing economic conditions and the velocity of AI innovation.

    *   *Example:* Jobs involving routine tasks have higher Systematic Risk. The user manual contains detailed formula of the Systematic Risk.
    *   *Formula:*  Based on user's education and experience. See attached document for details.

*   **Idiosyncratic Risk (V or V<sub>i</sub>):** Represents the individual's specific vulnerability based on their human capital, employer's stability, and upskilling efforts. This is the granular, multi-factor assessment of an individual's vulnerability based on their specific human capital, their employer's stability, and their proactive upskilling efforts.

    *   *Example:* Individuals with higher education and more upskilling have lower Idiosyncratic Risk. The user manual contains detailed formula of the Idiosyncratic Risk
    *   *Formula:* Based on factors in the attached document.

*   **Mitigation:** Actions taken to reduce the AI-Q Score, such as upskilling or changing career paths.

    *   *Example:* Completing a data science course to improve upskilling levels.

* The concepts of **Systematic Risk** and **Idiosyncratic Risk** are referenced from the provided document "AI-Q Score: A Multi-Factor Parametric Framework for Quantifying and Mitigating AI-Driven Job Displacement Risk," highlighting the analogy between financial risk management and career risk management in the age of AI.

## Libraries and Tools

*   **Streamlit:** A Python library used to create the user interface (UI) for the application.  It allows developers to easily create interactive web applications with minimal code. Streamlit is used for creating all input elements (text boxes, sliders, select boxes) and displaying the results (text, charts).

*   **Pandas:** A Python library providing data structures and data analysis tools. It is mainly used to create dataframes needed for displaying charts in `plotly`.

*   **Plotly:** A Python library for creating interactive, web-based visualizations. It is used to generate the bar chart showing the AI-Q Score breakdown and the line charts for simulation.
