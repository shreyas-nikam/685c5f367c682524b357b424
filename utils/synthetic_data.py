
import pandas as pd

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

def get_education_data():
    return {
        'No Degree': {'f_level': 1.20},
        'High School': {'f_level': 1.15},
        'Associate's': {'f_level': 1.10},
        'Bachelor's': {'f_level': 1.00},
        'Master's': {'f_level': 0.90},
        'PhD': {'f_level': 0.85},
    }

def get_education_field_data():
    return {
        'Liberal Arts/Humanities': {'f_field': 1.10},
        'Business/Management': {'f_field': 1.05},
        'Social Sciences': {'f_field': 1.05},
        'Natural Sciences': {'f_field': 0.95},
        'Tech/Engineering/Quantitative Science': {'f_field': 0.90},
    }

def get_school_tier_data():
    return {
        'Tier 1 (Ivy/Top Tier)': {'f_school': 0.95},
        'Tier 2 (Reputable State/Private)': {'f_school': 1.00},
        'Tier 3 (Local/Regional)': {'f_school': 1.05},
        'Tier 4 (Online/Vocational)': {'f_school': 1.10},
    }

def get_company_type_data():
    return {
        'Startup (High Growth/High Risk)': {'F_CR': 1.15},
        'Mid-size Firm (Stable/Moderate Growth)': {'F_CR': 1.00},
        'Big Firm (Established/Lower Growth)': {'F_CR': 0.95},
        'Government/Non-Profit (Very Stable)': {'F_CR': 0.85},
    }

def get_actuarial_parameters():
    return {
        'annual_salary_default': 90000,
        'coverage_duration_months_default': 6,
        'coverage_percentage_default': 0.25,
        'beta_systemic_default': 0.10,
        'beta_individual_default': 0.50,
        'loading_factor_default': 1.5,
        'min_premium_default': 20.00,
        'ttv_period_default': 12,
        'economic_climate_default': 1.0,
        'ai_innovation_default': 1.0,
        'w_cr': 0.4, # Weight for Company Risk in Idiosyncratic Risk
        'w_us': 0.6, # Weight for Upskilling in Idiosyncratic Risk
        'w1_fcr': 0.33, # Weights for FCR components (sentiment, financial, growth)
        'w2_fcr': 0.34,
        'w3_fcr': 0.33,
        'gamma_gen': 0.7, # Weight for general skill progress in Upskilling Factor
        'gamma_spec': 0.3, # Weight for firm-specific skill progress in Upskilling Factor
        'w_econ': 0.5, # Weight for Economic Climate in Systematic Risk
        'w_inno': 0.5, # Weight for AI Innovation in Systematic Risk
    }

