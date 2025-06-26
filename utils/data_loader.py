
import pandas as pd
from utils import synthetic_data

def load_synthetic_data():
    """
    Loads all synthetic datasets into a dictionary.
    """
    data = {
        'occupations': synthetic_data.get_occupations_data(),
        'education_levels': synthetic_data.get_education_data(),
        'education_fields': synthetic_data.get_education_field_data(),
        'school_tiers': synthetic_data.get_school_tier_data(),
        'company_types': synthetic_data.get_company_type_data(),
        'actuarial_params': synthetic_data.get_actuarial_parameters()
    }
    return data

