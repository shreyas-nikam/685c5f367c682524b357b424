
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
        'Associate's': {'f_level': 1.10},
        'Bachelor's': {'f_level': 1.00},
        'Master's': {'f_level': 0.90},
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
