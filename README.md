
# AI Risk Score - V4: Career Path Diversification Tool

## Overview

The "Career Path Diversification Tool" is a Streamlit application designed to help users understand and mitigate their exposure to systematic AI risk in their careers. It operationalizes the core concept of **Systematic Risk Exposure Mitigation** or **Career Path Diversification** as detailed in the provided research document "AI-Q Score: A Multi-Factor Parametric Framework for Quantifying and Mitigating AI-Driven Job Displacement Risk".

This application allows users to:
1.  **Input their current career profile**: Provide details about their current job, education, experience, and company.
2.  **View their current AI job displacement risk**: Calculate and display their current Idiosyncratic Risk and Systematic Risk scores, along with an estimated monthly "AI displacement insurance" premium.
3.  **Explore alternative career paths**: Based on a synthetic dataset mimicking O*NET, the application suggests alternative career options with potentially lower systematic risk.
4.  **Simulate career transitions**: Select a target career path and simulate the effort (e.g., skill acquisition, transition time) required to move to it, observing the real-time impact on their risk scores and insurance premium.
5.  **Visualize risk trends**: Interactive charts illustrate how risk scores and premiums change with career transition efforts and skill development.

Through these features, the application demonstrates how proactive career choices and skill development can significantly influence an individual's financial risk profile in an AI-driven labor market.

## How to Run the Application

### Prerequisites

*   Docker (recommended)
*   Python 3.9+ (if running locally without Docker)

### Running with Docker (Recommended)

1.  **Build the Docker Image**:
    ```bash
    docker build -t ai-risk-score-v4 .
    ```
2.  **Run the Docker Container**:
    ```bash
    docker run -p 8501:8501 ai-risk-score-v4
    ```
3.  **Access the Application**: Open your web browser and navigate to `http://localhost:8501`.

### Running Locally (without Docker)

1.  **Clone the Repository**: (Assuming you have access to the repository)
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Create a Virtual Environment (Optional but Recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```
5.  **Access the Application**: Open your web browser; Streamlit will typically open a new tab at `http://localhost:8501`.

## Application Structure

*   `app.py`: The main Streamlit application file.
*   `requirements.txt`: Lists all Python dependencies.
*   `Dockerfile`: Docker configuration for containerization.
*   `README.md`: This file.
*   `utils/`: Directory containing helper modules:
    *   `data_loader.py`: Handles loading of synthetic datasets.
    *   `risk_calculator.py`: Implements all the mathematical formulas for risk calculation.
    *   `visualization_utils.py`: Contains functions for generating Plotly charts.
