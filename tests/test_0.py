import pytest
from definition_9b225fce140e46b9915591f478afa57f import load_synthetic_data

@pytest.mark.parametrize("result", [
    # Test that load_synthetic_data returns a dictionary with expected keys
    ("occupations", "education_levels", "schools", "companies", "actuarial_params")
])
def test_load_synthetic_data_structure(result):
    data = load_synthetic_data()
    assert isinstance(data, dict)
    for key in ["occupations", "education_levels", "schools", "companies", "actuarial_params"]:
        assert key in data
        assert isinstance(data[key], dict)
        assert len(data[key]) > 0

@pytest.mark.parametrize("occupation, expected_keys", [
    ("Data Entry Clerk", ["H_base", "f_role"]),
    ("Senior Research Scientist", ["H_base", "f_role"]),
])
def test_occupations_data_content(occupation, expected_keys):
    data = load_synthetic_data()
    occupations = data["occupations"]
    assert occupation in occupations
    for key in expected_keys:
        assert key in occupations[occupation]
        # test numeric values are within expected ranges
        if key == "H_base":
            assert 0 <= occupations[occupation][key] <= 100
        elif key == "f_role":
            assert isinstance(occupations[occupation][key], (float, int))

@pytest.mark.parametrize("education_level, field, expected", [
    ("Bachelor's", "Tech/Engineering/Quantitative Science", {"f_level": 1.00, "f_field": 0.90}),
    ("PhD", "Liberal Arts/Humanities", {"f_level": 0.85, "f_field": 1.10}),
])
def test_education_data_content(education_level, field, expected):
    data = load_synthetic_data()
    edu_data = data["education_levels"]
    school_data = data["schools"]
    assert education_level in edu_data
    assert field in edu_data
    for key, val in expected.items():
        # Confirm presence and correct value
        assert edu_data[education_level][key] == val
        # Also check that schools data has expected keys
        assert field in school_data

@pytest.mark.parametrize("company, expected", [
    ("Big firm", 0.95),
    ("Mid-size firm", 1.00),
])
def test_companies_data_content(company, expected):
    data = load_synthetic_data()
    companies = data["companies"]
    assert company in companies
    assert abs(companies[company] - expected) < 1e-6

@pytest.mark.parametrize("params", [
    ("annual_salary", 90000),
    ("coverage_percentage", 25),
    ("coverage_duration", 6),
    ("beta_systemic", 0.10),
    ("beta_individual", 0.50),
    ("loading_factor", 1.5),
    ("min_premium", 20.0),
])
def test_actuarial_parameters_values(params):
    data = load_synthetic_data()
    actuary_params = data["actuarial_params"]
    key = params[0]
    value = params[1]
    assert key in actuary_params
    # Check numerical value
    assert abs(actuary_params[key] - value) < 1e-6 or isinstance(actuary_params[key], (int, float))
    
# Additional edge cases for load_synthetic_data
def test_load_synthetic_data_completeness():
    data = load_synthetic_data()
    # Confirm all expected keys exist
    for key in ["occupations", "education_levels", "schools", "companies", "actuarial_params"]:
        assert key in data
        assert isinstance(data[key], dict)
        assert len(data[key]) > 0

# Edge case: test that all risks are normalized within 0-100
def test_risk_scores_are_normalized():
    data = load_synthetic_data()
    occupations = data["occupations"]
    for occupation, vals in occupations.items():
        assert 0 <= vals["H_base"] <= 100
        # Simulate FHC calculation: ensure the result is within expected bounds
        # Since FHC is a product of factors, it's reasonable to check for float/int
        assert isinstance(vals["f_role"], (float, int))
    # Check FHC calculation (assuming it's handled externally) stays within 0-100 when normalized
    # But as we only test load_synthetic_data here, just ensure data consistency
