id: 685c5f367c682524b357b424_user_guide
summary: AI Risk Score - V4 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI Risk Score: Career Path Diversification Tool

## Introduction
Duration: 00:05

Welcome to the AI Risk Score - V4 Codelab! This application provides a practical, hands-on approach to understanding and mitigating the risks associated with AI-driven job displacement. It's based on the "AI-Q Score" framework, a method for quantifying your personal risk and exploring strategies for career resilience in an evolving job market. This codelab will walk you through the application's features, demonstrating how you can use it to assess your current risk profile, explore alternative career paths, and simulate the impact of skill development. This is NOT about the code of the app, but understanding the concepts it presents and showcases.

<aside class="positive">
This tool is designed to empower you with the knowledge and insights needed to make informed career decisions in the age of AI. <b>Understanding the risks is the first step toward managing them!</b>
</aside>

## Understanding the Core Concepts
Duration: 00:10

Before diving into the application, let's clarify the key concepts behind the AI-Q Score framework:

*   **Idiosyncratic Risk ($V_i(t)$):** This represents your individual vulnerability to job displacement. It's influenced by factors like your education, skills, experience, and the stability of your employer. This is the risk you can directly influence through your choices and actions.
*   **Systematic Risk ($H_i$):** This reflects the inherent risk of job displacement due to automation within your occupation, adjusted by factors like the overall economic climate and the pace of AI innovation. This risk is largely outside of your control, but you can mitigate it by choosing a career in an industry with lower automation hazards.
*   **Career Path Diversification:** The idea of diversifying your career similar to how an investor diversifies a portfolio. Instead of relying on a single area of expertise, you can, over time, spread your skills and experience across multiple fields to reduce systematic risk.
*   **Time-to-Value (TTV):** The time it takes you to transition to a new career path to reduce systematic risk. In this app the default is set to 12 months.

<aside class="negative">
Remember that this tool provides a *hypothetical* risk assessment. While it's based on a research framework, the results should not be taken as definitive predictions. <b>It's crucial to use your own judgment and consider your unique circumstances!</b>
</aside>

## Exploring Your Current Career Profile
Duration: 00:15

The first step is to assess your current risk profile. The application allows you to input your current job details, including your job title, years of experience, education level, and company type. The goal here is to get a baseline for your Idiosyncratic and Systematic Risks.

1.  **Job Title:** Select your current job title from the dropdown menu. This will automatically determine the base automation hazard ($H_{base}$) associated with your occupation.
2.  **Experience:** Use the slider to specify the number of years of professional experience you possess. More years of experience typically reduce your risk factor.
3.  **Education:** Select your highest level of education from the dropdown. Higher education generally reduces your risk factor, because it shows your capacity to learn and adapt.
4.  **Company Type:** Select your current company's type from the dropdown. Innovative companies have less risk than mature non tech companies.
5.  **Skill Acquisition Progress:** Use the sliders to indicate your current progress in acquiring general and firm-specific skills. The relative weightage of the progress of general and firm-specific skills in upskilling factor is controlled using the gamma parameters in the sidebar.

<aside class="positive">
Take your time when entering your information to ensure the most accurate results. <b>The more accurate your input, the more relevant the risk assessment will be!</b>
</aside>

## Understanding Company Risk Factors (Simulated)
Duration: 00:05

The application includes simulated Company Risk Factors (CRF) like sentiment score, financial health score, and growth and AI-adoption score. These are simplified and fixed in this app, but they would be based on real-time data in a production system. Adjust these values to see how a company's perceived stability and AI adoption strategies can impact your overall risk score.

## Interpreting Your Current Risk Score
Duration: 00:05

After entering your details, the application calculates and displays your current Idiosyncratic Risk, Systematic Risk, and an estimated monthly premium for hypothetical "AI displacement insurance."

*   **Idiosyncratic Risk ($V_i(t)$):** This metric represents your personal vulnerability to job displacement.
*   **Systematic Risk ($H_i$):** This metric captures the automation hazards inherent to your occupation, plus broader environmental factors.
*   **Estimated Monthly Premium:** This is a hypothetical cost for "AI displacement insurance" based on your risk factors.

## Simulating a Career Transition
Duration: 00:15

Now, let's explore the impact of a career transition. The application allows you to simulate changing your career path and acquiring new skills.

1.  **Target Career Path:** Select a new career path from the dropdown menu. This will change the base automation hazard ($H_{base}$) used in the Systematic Risk calculation.
2.  **Transition Progress (Months):** Use the slider to indicate how far along you are in your career transition. This allows you to see how your risk scores gradually change as you move towards your new career.
3.  **Simulated Skill Acquisition Progress:** Use the sliders to simulate the impact of acquiring new general and firm-specific skills. Acquiring new skills helps you to mitigate the idiosyncratic risk.

<aside class="negative">
Remember that a career transition takes time and effort. <b>Be realistic about the time it will take you to acquire new skills and establish yourself in a new field!</b>
</aside>

## Analyzing Simulated Risk Scores
Duration: 00:05

After simulating a career transition, the application displays your new Idiosyncratic Risk, Systematic Risk, and estimated monthly premium. You'll also see the change (delta) compared to your current scores. This allows you to assess the potential risk reduction associated with your career transition.

## Visualizing Risk Trends
Duration: 00:10

The application includes several visualizations to help you understand the trends in your risk scores:

*   **Comparison: Current vs. Simulated Risk & Premium:** This bar chart compares your current and simulated risk components, allowing you to easily see the impact of your career transition and skill development.
*   **Systematic Risk & Premium During Career Transition:** This line chart shows how your Systematic Risk and estimated monthly premium change over the transition period.
*   **Idiosyncratic Risk & Premium vs. Skill Acquisition:** This line chart demonstrates how acquiring new general skills can reduce your Idiosyncratic Risk and estimated monthly premium.

## Global & Actuarial Parameters
Duration: 00:05

The sidebar contains global and actuarial parameters. You can adjust these parameters and observe the impact on risk scores and premiums. For example, increasing the economic climate modifier might increase the systematic risk. You can also adjust the insurance policy terms to see how it affects the premium.

## Conclusion
Duration: 00:05

Congratulations! You have now completed the AI Risk Score Codelab. You've learned how to use the application to assess your current risk profile, explore alternative career paths, and simulate the impact of skill development. Remember that this tool is designed to empower you with the knowledge and insights needed to make informed career decisions in the age of AI. Use this knowledge to plan, diversify, and continuously learn!
