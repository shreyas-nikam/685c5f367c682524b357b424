
def load_synthetic_data() -> dict:
    """
    Loads predefined synthetic datasets and parameters into structured dictionaries.

    Returns:
        dict: A dictionary containing 'occupations', 'education_levels', 'schools',
              'companies', and 'actuarial_params', each as a dict with sample data.
    """
    # Synthetic data for occupations
    occupations: dict[str, dict[str, float]] = {
        "Data Entry Clerk": {"H_base": 20.0, "f_role": 0.8},
        "Senior Research Scientist": {"H_base": 70.0, "f_role": 1.2},
        "Software Engineer": {"H_base": 50.0, "f_role": 1.0},
        "Sales Associate": {"H_base": 30.0, "f_role": 0.9},
        "Nurse": {"H_base": 40.0, "f_role": 1.1},
    }

    # Synthetic data for education levels
    education_levels: dict[str, dict[str, float]] = {
        "Bachelor's": {"f_level": 1.00, "f_field": 0.90},
        "Master's": {"f_level": 1.10, "f_field": 1.00},
        "PhD": {"f_level": 1.20, "f_field": 1.10},
        "Associate": {"f_level": 0.85, "f_field": 0.80},
        "High School": {"f_level": 0.70, "f_field": 0.75},
    }

    # Synthetic data for schools, categorized by field
    schools: dict[str, list[str]] = {
        "Tech/Engineering/Quantitative Science": ["Tech Institute", "Science College"],
        "Liberal Arts/Humanities": ["Arts University", "Humanities College"],
        "Business": ["Business School"],
    }

    # Synthetic data for companies
    companies: dict[str, float] = {
        "Big firm": 0.95,
        "Mid-size firm": 1.00,
        "Startup Inc": 1.10,
        "Nonprofit Org": 0.85,
    }

    # Synthetic actuarial parameters
    actuarial_params: dict[str, float] = {
        "annual_salary": 90000,
        "coverage_percentage": 25,
        "coverage_duration": 6,
        "beta_systemic": 0.10,
        "beta_individual": 0.50,
        "loading_factor": 1.5,
        "min_premium": 20.0,
    }

    return {
        "occupations": occupations,
        "education_levels": education_levels,
        "schools": schools,
        "companies": companies,
        "actuarial_params": actuarial_params,
    }
