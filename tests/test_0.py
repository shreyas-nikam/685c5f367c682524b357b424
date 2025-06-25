import pytest
from definition_81d17ef361744c778ff8cd55b0d37125 import load_synthetic_data

def test_load_synthetic_data_type_and_content():
    data = load_synthetic_data()
    # The output should be a tuple or dictionary
    assert data is not None
    assert isinstance(data, (tuple, dict)), "Output should be tuple or dict"
    
    # If dict, check keys
    if isinstance(data, dict):
        expected_keys = {
            'occupations_data', 'education_data', 'school_tier_data',
            'company_type_data', 'actuarial_parameters'
        }
        assert expected_keys.issubset(data.keys()), f"Missing keys in data dict, expected at least {expected_keys}"
        # occupations_data must be dict or DataFrame
        occ = data['occupations_data']
        assert isinstance(occ, (dict, type(None))) or hasattr(occ, 'loc'), "occupations_data should be dict or DataFrame"
        edu = data['education_data']
        assert isinstance(edu, (dict, type(None))) or hasattr(edu, 'loc'), "education_data should be dict or DataFrame"
        school = data['school_tier_data']
        assert isinstance(school, dict), "school_tier_data should be dict"
        comp = data['company_type_data']
        assert isinstance(comp, dict), "company_type_data should be dict"
        actuarial = data['actuarial_parameters']
        assert isinstance(actuarial, dict), "actuarial_parameters should be dict"
    # If tuple, expect length 5
    elif isinstance(data, tuple):
        assert len(data) == 5, "Output tuple should contain 5 elements"
        occ, edu, school, comp, actuarial = data
        # Basic types check
        assert isinstance(occ, (dict, type(None))) or hasattr(occ, 'loc'), "occupations_data should be dict or DataFrame"
        assert isinstance(edu, (dict, type(None))) or hasattr(edu, 'loc'), "education_data should be dict or DataFrame"
        assert isinstance(school, dict), "school_tier_data should be dict"
        assert isinstance(comp, dict), "company_type_data should be dict"
        assert isinstance(actuarial, dict), "actuarial_parameters should be dict"
        

@pytest.mark.parametrize("invalid_input", [
    123,
    "string",
    [1,2,3],
    None,
    5.6,
    True,
])
def test_load_synthetic_data_invalid_call(invalid_input):
    # load_synthetic_data is defined without arguments,
    # so passing input should raise TypeError
    with pytest.raises(TypeError):
        load_synthetic_data(invalid_input)


def test_load_synthetic_data_occupations_data_content():
    data = load_synthetic_data()
    # Extract occupations data
    if isinstance(data, dict):
        occupations = data.get('occupations_data')
    else:
        occupations = data[0]
    assert occupations is not None, "occupations_data should not be None"
    # Test for expected keys for at least one occupation
    if hasattr(occupations, 'get'):
        # dict type
        # Expect at least one occupation with keys 'H_base' and 'f_role'
        found_valid = False
        for val in occupations.values():
            if isinstance(val, dict):
                if 'H_base' in val and 'f_role' in val:
                    found_valid = True
                    # Validate values types
                    assert isinstance(val['H_base'], (int, float)), "H_base should be numeric"
                    assert isinstance(val['f_role'], (int, float)), "f_role should be numeric"
                    break
        assert found_valid, "No valid occupation entry with keys 'H_base' and 'f_role'"
    elif hasattr(occupations, 'loc'):
        # Pandas DataFrame, check columns
        required_cols = {'H_base', 'f_role'}
        assert required_cols.issubset(set(occupations.columns)), "Occupations DataFrame missing required columns"
        # Check some values
        sample_row = occupations.iloc[0]
        assert isinstance(sample_row['H_base'], (int,float)), "H_base should be numeric"
        assert isinstance(sample_row['f_role'], (int,float)), "f_role should be numeric"


def test_load_synthetic_data_education_data_content():
    data = load_synthetic_data()
    if isinstance(data, dict):
        education = data.get('education_data')
    else:
        education = data[1]
    assert education is not None, "education_data should not be None"
    # The education data should contain mappings for f_level or f_field
    found_level = False
    found_field = False
    if hasattr(education, 'get'):
        # dict type
        for val in education.values():
            if isinstance(val, dict):
                if 'f_level' in val:
                    found_level = True
                    assert isinstance(val['f_level'], (int,float))
                if 'f_field' in val:
                    found_field = True
                    assert isinstance(val['f_field'], (int,float))
            if found_level and found_field:
                break
        # At least one of f_level or f_field should be found
        assert found_level or found_field, "education_data lacks f_level or f_field mappings"
    elif hasattr(education, 'loc'):
        # DataFrame, check columns
        # Must have at least f_level or f_field columns
        cols = set(education.columns)
        assert 'f_level' in cols or 'f_field' in cols, "Education DataFrame missing f_level and f_field columns"
        # Check one value type if exist
        if 'f_level' in cols:
            v = education['f_level'].dropna().iloc[0]
            assert isinstance(v, (int,float))
        elif 'f_field' in cols:
            v = education['f_field'].dropna().iloc[0]
            assert isinstance(v, (int,float))


def test_load_synthetic_data_school_tier_data_content():
    data = load_synthetic_data()
    if isinstance(data, dict):
        schooling = data.get('school_tier_data')
    else:
        schooling = data[2]
    assert schooling is not None, "school_tier_data should not be None"
    assert isinstance(schooling, dict), "school_tier_data should be dict"
    # Check keys and values types
    assert len(schooling) > 0, "school_tier_data should not be empty"
    for k,v in schooling.items():
        assert isinstance(k, str)
        assert isinstance(v, (int, float))


def test_load_synthetic_data_company_type_data_content():
    data = load_synthetic_data()
    if isinstance(data, dict):
        company = data.get('company_type_data')
    else:
        company = data[3]
    assert company is not None, "company_type_data should not be None"
    assert isinstance(company, dict), "company_type_data should be dict"
    # Check keys and values types
    assert len(company) > 0, "company_type_data should not be empty"
    for k,v in company.items():
        assert isinstance(k, str)
        assert isinstance(v, (int, float))


def test_load_synthetic_data_actuarial_parameters_content():
    data = load_synthetic_data()
    if isinstance(data, dict):
        actuarial = data.get('actuarial_parameters')
    else:
        actuarial = data[4]
    assert actuarial is not None, "actuarial_parameters should not be None"
    assert isinstance(actuarial, dict), "actuarial_parameters should be dict"
    # Check required keys are present with appropriate types
    required_keys = {
        'Annual Salary', 'Coverage Percentage', 'Coverage Duration',
        'beta_systemic', 'beta_individual', 'loading_factor', 'min_premium'
    }
    missing_keys = required_keys - set(actuarial.keys())
    assert missing_keys == set(), f"actuarial_parameters missing keys: {missing_keys}"
    for key in required_keys:
        val = actuarial[key]
        assert isinstance(val, (int, float)), f"actuarial_parameters[{key}] should be numeric"


def test_load_synthetic_data_handles_no_arguments():
    # Confirm that calling without arguments works
    try:
        result = load_synthetic_data()
    except Exception:
        pytest.fail("load_synthetic_data() raised Exception unexpectedly")


@pytest.mark.parametrize("return_type", ['dict', 'tuple'])
def test_load_synthetic_data_handles_return_type(monkeypatch, return_type):
    # This is a simple monkeypatch test to simulate returning either tuple or dict
    # Only for illustrative purposes, may not be possible depending on implementation
    # Here we just test the output type is one of allowed types
    data = load_synthetic_data()
    assert isinstance(data, (tuple, dict))


@pytest.mark.parametrize("stress_case", [
    pytest.param(None, id="None"),
    pytest.param("", id="EmptyString"),
    pytest.param({}, id="EmptyDict"),
    pytest.param([], id="EmptyList"),
])
def test_load_synthetic_data_produces_consistent_structure(stress_case):
    # This test verifies that the function does not return invalid structures even under unexpected conditions
    # load_synthetic_data has no inputs, so ignoring stress_case usage.
    data = load_synthetic_data()
    assert isinstance(data, (tuple, dict)), "Return type should always be tuple or dict"
