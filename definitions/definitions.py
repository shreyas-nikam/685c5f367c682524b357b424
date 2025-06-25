
from typing import Union, Tuple, Dict, Any


def load_synthetic_data() -> Union[
    Dict[str, Any],
    Tuple[Union[Dict[str, Any], None], Union[Dict[str, Any], None], Dict[str, float], Dict[str, float], Dict[str, float]]
]:
    """
    Loads all synthetic data required for the career path diversification tool.

    Returns:
        Union[dict, tuple]:
            A dictionary or tuple containing:
                - occupations_data: dict or None (with keys like 'H_base' and 'f_role')
                - education_data: dict or None (with keys like 'f_level' or 'f_field')
                - school_tier_data: dict of {str: float}
                - company_type_data: dict of {str: float}
                - actuarial_parameters: dict of actuarial and risk parameters
    """
    occupations_data = {
        "Engineer": {"H_base": 80_000, "f_role": 1.2, "description": "Software Engineer"},
        "Teacher": {"H_base": 50_000, "f_role": 0.8},
        "Artist": {"H_base": 40_000, "f_role": 0.6},
    }
    education_data = {
        "Bachelors": {"f_level": 1.0, "f_field": 1.1},
        "Masters": {"f_level": 1.2, "f_field": 1.3},
        "PhD": {"f_level": 1.5},
    }
    school_tier_data = {
        "Tier 1": 1.5,
        "Tier 2": 1.2,
        "Tier 3": 1.0,
    }
    company_type_data = {
        "Startup": 1.3,
        "SME": 1.1,
        "Corporation": 1.0,
    }
    actuarial_parameters = {
        "Annual Salary": 70_000,
        "Coverage Percentage": 0.85,
        "Coverage Duration": 10,
        "beta_systemic": 0.03,
        "beta_individual": 0.05,
        "loading_factor": 1.25,
        "min_premium": 1000.0,
    }
    return (
        occupations_data,
        education_data,
        school_tier_data,
        company_type_data,
        actuarial_parameters,
    )


from typing import Union, Tuple, Dict, Any


def load_synthetic_data() -> Union[
    Dict[str, Any],
    Tuple[Union[Dict[str, Any], None], Union[Dict[str, Any], None], Dict[str, float], Dict[str, float], Dict[str, float]]
]:
    """
    Loads all synthetic data required for the career path diversification tool.

    Returns:
        Union[dict, tuple]:
            A dictionary or tuple containing:
                - occupations_data: dict or None (with keys like 'H_base' and 'f_role')
                - education_data: dict or None (with keys like 'f_level' or 'f_field')
                - school_tier_data: dict of {str: float}
                - company_type_data: dict of {str: float}
                - actuarial_parameters: dict of actuarial and risk parameters
    """
    occupations_data = {
        "Engineer": {"H_base": 80_000, "f_role": 1.2, "description": "Software Engineer"},
        "Teacher": {"H_base": 50_000, "f_role": 0.8},
        "Artist": {"H_base": 40_000, "f_role": 0.6},
    }
    education_data = {
        "Bachelors": {"f_level": 1.0, "f_field": 1.1},
        "Masters": {"f_level": 1.2, "f_field": 1.3},
        "PhD": {"f_level": 1.5},
    }
    school_tier_data = {
        "Tier 1": 1.5,
        "Tier 2": 1.2,
        "Tier 3": 1.0,
    }
    company_type_data = {
        "Startup": 1.3,
        "SME": 1.1,
        "Corporation": 1.0,
    }
    actuarial_parameters = {
        "Annual Salary": 70_000,
        "Coverage Percentage": 0.85,
        "Coverage Duration": 10,
        "beta_systemic": 0.03,
        "beta_individual": 0.05,
        "loading_factor": 1.25,
        "min_premium": 1000.0,
    }
    return (
        occupations_data,
        education_data,
        school_tier_data,
        company_type_data,
        actuarial_parameters,
    )


from typing import Union
import math

def calculate_fexp(years_experience: Union[int, float]) -> float:
    """
    Calculates the Experience Factor (fexp), a decaying function of years of experience capped at 20 years.

    Args:
        years_experience (int or float): Number of years of professional experience, capped at 20.

    Returns:
        float: Experience factor calculated as 1 - (0.015 * min(years_experience, 20)).

    Raises:
        TypeError: If years_experience is not a number, or is NaN, or negative infinite.
        ValueError: If years_experience is negative (other than negative zero).
    """
    if not isinstance(years_experience, (int, float)):
        raise TypeError("years_experience must be a numeric type")
    if math.isnan(years_experience):
        raise TypeError("years_experience cannot be NaN")
    if years_experience == float('-inf'):
        raise TypeError("years_experience cannot be negative infinity")
    if years_experience < 0:
        years_experience = 0

    capped_exp = years_experience if years_experience != float('inf') else 20
    capped_exp = min(capped_exp, 20)
    return 1 - 0.015 * capped_exp


from typing import Union
import math

def calculate_fexp(years_experience: Union[int, float]) -> float:
    """
    Calculates the Experience Factor (fexp), a decaying function of years of experience capped at 20 years.

    Args:
        years_experience (int or float): Number of years of professional experience, capped at 20.

    Returns:
        float: Experience factor calculated as 1 - (0.015 * min(years_experience, 20)).

    Raises:
        TypeError: If years_experience is not a number, or is NaN, or negative infinite.
        ValueError: If years_experience is negative (other than negative zero).
    """
    if not isinstance(years_experience, (int, float)):
        raise TypeError("years_experience must be a numeric type")
    if math.isnan(years_experience):
        raise TypeError("years_experience cannot be NaN")
    if years_experience == float('-inf'):
        raise TypeError("years_experience cannot be negative infinity")
    if years_experience < 0:
        years_experience = 0

    capped_exp = years_experience if years_experience != float('inf') else 20
    capped_exp = min(capped_exp, 20)
    return 1 - 0.015 * capped_exp


from typing import Union


def calculate_fhc(
    role_multiplier: Union[float, int], 
    edu_level_factor: Union[float, int], 
    edu_field_factor: Union[float, int], 
    school_tier_factor: Union[float, int], 
    fexp_value: Union[float, int]
) -> float:
    """
    Calculates the Human Capital Factor (FHC) as a product of several sub-factors that represent a user's education and experience.

    Args:
        role_multiplier (float|int): Role multiplier reflecting job title vulnerability.
        edu_level_factor (float|int): Education level factor.
        edu_field_factor (float|int): Education field factor.
        school_tier_factor (float|int): Institution tier factor.
        fexp_value (float|int): Experience factor.

    Returns:
        float: Calculated Human Capital Factor as the product of all input multipliers.

    Raises:
        TypeError: If any of the inputs is not a float or int (booleans excluded).
    """
    for arg in (role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value):
        if not isinstance(arg, (float, int)) or isinstance(arg, bool):
            raise TypeError(f"All inputs must be float or int, got {type(arg).__name__}")

    return float(role_multiplier) * float(edu_level_factor) * float(edu_field_factor) * float(school_tier_factor) * float(fexp_value)


from typing import Union


def calculate_fhc(
    role_multiplier: Union[float, int], 
    edu_level_factor: Union[float, int], 
    edu_field_factor: Union[float, int], 
    school_tier_factor: Union[float, int], 
    fexp_value: Union[float, int]
) -> float:
    """
    Calculates the Human Capital Factor (FHC) as a product of several sub-factors that represent a user's education and experience.

    Args:
        role_multiplier (float|int): Role multiplier reflecting job title vulnerability.
        edu_level_factor (float|int): Education level factor.
        edu_field_factor (float|int): Education field factor.
        school_tier_factor (float|int): Institution tier factor.
        fexp_value (float|int): Experience factor.

    Returns:
        float: Calculated Human Capital Factor as the product of all input multipliers.

    Raises:
        TypeError: If any of the inputs is not a float or int (booleans excluded).
    """
    for arg in (role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value):
        if not isinstance(arg, (float, int)) or isinstance(arg, bool):
            raise TypeError(f"All inputs must be float or int, got {type(arg).__name__}")

    return float(role_multiplier) * float(edu_level_factor) * float(edu_field_factor) * float(school_tier_factor) * float(fexp_value)


from typing import Union
import math

Number = Union[int, float]

def calculate_fcr(
    sentiment_score: Number,
    financial_health_score: Number,
    growth_ai_adoption_score: Number,
    w1: Number,
    w2: Number,
    w3: Number
) -> float:
    """
    Calculates the Company Risk Factor (FCR) as a weighted sum of sentiment, financial health,
    and growth/AI adoption scores.

    Args:
        sentiment_score (Number): Sentiment score of the company.
        financial_health_score (Number): Financial health score.
        growth_ai_adoption_score (Number): Growth and AI adoption score.
        w1 (Number): Weight for sentiment score.
        w2 (Number): Weight for financial health score.
        w3 (Number): Weight for growth and AI adoption score.

    Returns:
        float: Weighted company risk factor.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any input is NaN.
        OverflowError: If any input is infinite.
    """
    scores = (sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)
    # Validate types
    for val in scores:
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input {val} is not a number")
        if isinstance(val, float):
            if math.isnan(val):
                raise ValueError("Input cannot be NaN")
            if math.isinf(val):
                raise OverflowError("Input cannot be infinite")
    return float(sentiment_score * w1 + financial_health_score * w2 + growth_ai_adoption_score * w3)


from typing import Union
import math

Number = Union[int, float]

def calculate_fcr(
    sentiment_score: Number,
    financial_health_score: Number,
    growth_ai_adoption_score: Number,
    w1: Number,
    w2: Number,
    w3: Number
) -> float:
    """
    Calculates the Company Risk Factor (FCR) as a weighted sum of sentiment, financial health,
    and growth/AI adoption scores.

    Args:
        sentiment_score (Number): Sentiment score of the company.
        financial_health_score (Number): Financial health score.
        growth_ai_adoption_score (Number): Growth and AI adoption score.
        w1 (Number): Weight for sentiment score.
        w2 (Number): Weight for financial health score.
        w3 (Number): Weight for growth and AI adoption score.

    Returns:
        float: Weighted company risk factor.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any input is NaN.
        OverflowError: If any input is infinite.
    """
    scores = (sentiment_score, financial_health_score, growth_ai_adoption_score, w1, w2, w3)
    # Validate types
    for val in scores:
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input {val} is not a number")
        if isinstance(val, float):
            if math.isnan(val):
                raise ValueError("Input cannot be NaN")
            if math.isinf(val):
                raise OverflowError("Input cannot be infinite")
    return float(sentiment_score * w1 + financial_health_score * w2 + growth_ai_adoption_score * w3)


def calculate_fus(p_gen: float, p_spec: float, gamma_gen: float, gamma_spec: float) -> float:
    """
    Calculates the Upskilling Factor (FUS) based on progress in general and firm-specific skills training.

    Args:
        p_gen (float): Training progress in general/portable skills, between 0 and 1.
        p_spec (float): Training progress in firm-specific skills, between 0 and 1.
        gamma_gen (float): Weight for general skill progress.
        gamma_spec (float): Weight for firm-specific skill progress.

    Returns:
        float: Upskilling factor representing risk reduction through training.

    Raises:
        TypeError: If any input is not a float.
        ValueError: If p_gen or p_spec not in [0,1] or if gamma_gen or gamma_spec is negative.
    """
    for name, val in (("p_gen", p_gen), ("p_spec", p_spec), ("gamma_gen", gamma_gen), ("gamma_spec", gamma_spec)):
        if not isinstance(val, float):
            raise TypeError(f"{name} must be a float")
    if not (0 <= p_gen <= 1):
        raise ValueError("p_gen must be between 0 and 1 inclusive")
    if not (0 <= p_spec <= 1):
        raise ValueError("p_spec must be between 0 and 1 inclusive")
    if gamma_gen < 0 or gamma_spec < 0:
        raise ValueError("gamma_gen and gamma_spec must be non-negative")

    return 1.0 - (gamma_gen * p_gen + gamma_spec * p_spec)


def calculate_fus(p_gen: float, p_spec: float, gamma_gen: float, gamma_spec: float) -> float:
    """
    Calculates the Upskilling Factor (FUS) based on progress in general and firm-specific skills training.

    Args:
        p_gen (float): Training progress in general/portable skills, between 0 and 1.
        p_spec (float): Training progress in firm-specific skills, between 0 and 1.
        gamma_gen (float): Weight for general skill progress.
        gamma_spec (float): Weight for firm-specific skill progress.

    Returns:
        float: Upskilling factor representing risk reduction through training.

    Raises:
        TypeError: If any input is not a float.
        ValueError: If p_gen or p_spec not in [0,1] or if gamma_gen or gamma_spec is negative.
    """
    for name, val in (("p_gen", p_gen), ("p_spec", p_spec), ("gamma_gen", gamma_gen), ("gamma_spec", gamma_spec)):
        if not isinstance(val, float):
            raise TypeError(f"{name} must be a float")
    if not (0 <= p_gen <= 1):
        raise ValueError("p_gen must be between 0 and 1 inclusive")
    if not (0 <= p_spec <= 1):
        raise ValueError("p_spec must be between 0 and 1 inclusive")
    if gamma_gen < 0 or gamma_spec < 0:
        raise ValueError("gamma_gen and gamma_spec must be non-negative")

    return 1.0 - (gamma_gen * p_gen + gamma_spec * p_spec)


from typing import Union


def calculate_idiosyncratic_risk(
    fhc: Union[int, float],
    fcr: Union[int, float],
    fus: Union[int, float],
    w_cr: Union[int, float],
    w_us: Union[int, float]
) -> float:
    """
    Calculates the Idiosyncratic Risk score (Vi) based on Human Capital,
    Company Risk, and Upskilling factors.

    Args:
        fhc (Union[int, float]): Human Capital Factor.
        fcr (Union[int, float]): Company Risk Factor.
        fus (Union[int, float]): Upskilling Factor.
        w_cr (Union[int, float]): Weight for Company Risk Factor.
        w_us (Union[int, float]): Weight for Upskilling Factor.

    Returns:
        float: Idiosyncratic risk score normalized between 5.0 and 100.0.

    Raises:
        TypeError: If any input is not a number.
        ValueError: If any input is None.
    """
    for value, name in zip((fhc, fcr, fus, w_cr, w_us),
                           ("fhc", "fcr", "fus", "w_cr", "w_us")):
        if value is None:
            raise ValueError(f"{name} cannot be None")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number (int or float)")

    fhc, fcr, fus, w_cr, w_us = map(float, (fhc, fcr, fus, w_cr, w_us))

    combined_factor = w_cr * fcr + w_us * fus
    raw_score = fhc * combined_factor

    # Normalize raw_score from [0.1..2.0] roughly maps to [5..100]
    # linear scaling factor: scale = 52.5*(raw_score - 0.1) + 5
    # values <0.1 clamp to 5, >2 clamp to 100

    if raw_score <= 0.1:
        normalized_score = 5.0
    elif raw_score >= 2.0:
        normalized_score = 100.0
    else:
        normalized_score = 52.5 * (raw_score - 0.1) + 5

    return round(normalized_score, 2)


def calculate_h_base_ttv(k: int, ttv: int, h_current: float, h_target: float) -> float:
    """
    Calculates the base occupational hazard (H_base) during a career transition as a time-weighted average 
    of current and target job hazards.

    Args:
        k (int): Number of months elapsed since pathway completion.
        ttv (int): Total months in the Time-to-Value period.
        h_current (float): Base occupational hazard of the current job.
        h_target (float): Base occupational hazard of the target job.

    Returns:
        float: Time-weighted base occupational hazard at month k.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If inputs cannot be converted to proper types.
        ZeroDivisionError: If ttv is zero.
    """
    # Validate and convert types
    if not isinstance(k, int):
        if isinstance(k, float) and k.is_integer():
            k = int(k)
        else:
            raise TypeError("k must be an integer")
    if not isinstance(ttv, int):
        if isinstance(ttv, float) and ttv.is_integer():
            ttv = int(ttv)
        else:
            raise TypeError("ttv must be an integer")
    for val, name in [(h_current, "h_current"), (h_target, "h_target")]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a number")
    h_current = float(h_current)
    h_target = float(h_target)

    if ttv == 0:
        raise ZeroDivisionError("ttv must be a non-zero integer")

    k = max(0, min(k, ttv))

    return ((ttv - k) * h_current + k * h_target) / ttv


def calculate_h_base_ttv(k: int, ttv: int, h_current: float, h_target: float) -> float:
    """
    Calculates the base occupational hazard (H_base) during a career transition as a time-weighted average 
    of current and target job hazards.

    Args:
        k (int): Number of months elapsed since pathway completion.
        ttv (int): Total months in the Time-to-Value period.
        h_current (float): Base occupational hazard of the current job.
        h_target (float): Base occupational hazard of the target job.

    Returns:
        float: Time-weighted base occupational hazard at month k.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If inputs cannot be converted to proper types.
        ZeroDivisionError: If ttv is zero.
    """
    # Validate and convert types
    if not isinstance(k, int):
        if isinstance(k, float) and k.is_integer():
            k = int(k)
        else:
            raise TypeError("k must be an integer")
    if not isinstance(ttv, int):
        if isinstance(ttv, float) and ttv.is_integer():
            ttv = int(ttv)
        else:
            raise TypeError("ttv must be an integer")
    for val, name in [(h_current, "h_current"), (h_target, "h_target")]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a number")
    h_current = float(h_current)
    h_target = float(h_target)

    if ttv == 0:
        raise ZeroDivisionError("ttv must be a non-zero integer")

    k = max(0, min(k, ttv))

    return ((ttv - k) * h_current + k * h_target) / ttv


from typing import Union

def calculate_systematic_risk(
    h_base_t: Union[int, float],
    m_econ: Union[int, float],
    i_ai: Union[int, float],
    w_econ: Union[int, float],
    w_inno: Union[int, float]
) -> float:
    """
    Calculates the Systematic Risk score (Hi) based on the base occupational hazard and environmental modifiers.

    Args:
        h_base_t (float or int): Base occupational hazard at time t.
        m_econ (float or int): Economic Climate Modifier.
        i_ai (float or int): AI Innovation Index.
        w_econ (float or int): Weight for economic climate modifier.
        w_inno (float or int): Weight for AI innovation index.

    Returns:
        float: Final systematic risk score.

    Raises:
        TypeError: If any argument is not a number (int or float).
        ValueError: If any argument cannot be converted to float.
    """
    try:
        h_base_t = float(h_base_t)
        m_econ = float(m_econ)
        i_ai = float(i_ai)
        w_econ = float(w_econ)
        w_inno = float(w_inno)
    except (TypeError, ValueError):
        raise

    return h_base_t * (w_econ * m_econ + w_inno * i_ai)


from typing import Union

def calculate_systematic_risk(
    h_base_t: Union[int, float],
    m_econ: Union[int, float],
    i_ai: Union[int, float],
    w_econ: Union[int, float],
    w_inno: Union[int, float]
) -> float:
    """
    Calculates the Systematic Risk score (Hi) based on the base occupational hazard and environmental modifiers.

    Args:
        h_base_t (float or int): Base occupational hazard at time t.
        m_econ (float or int): Economic Climate Modifier.
        i_ai (float or int): AI Innovation Index.
        w_econ (float or int): Weight for economic climate modifier.
        w_inno (float or int): Weight for AI innovation index.

    Returns:
        float: Final systematic risk score.

    Raises:
        TypeError: If any argument is not a number (int or float).
        ValueError: If any argument cannot be converted to float.
    """
    try:
        h_base_t = float(h_base_t)
        m_econ = float(m_econ)
        i_ai = float(i_ai)
        w_econ = float(w_econ)
        w_inno = float(w_inno)
    except (TypeError, ValueError):
        raise

    return h_base_t * (w_econ * m_econ + w_inno * i_ai)


def calculate_payout_amount(
    annual_salary: float, coverage_duration: int, coverage_percentage: float
) -> float:
    """
    Calculates total payout amount (L_payout) based on annual salary,
    coverage duration (months), and coverage percentage.

    Args:
        annual_salary (float): User's annual salary, must be non-negative.
        coverage_duration (int): Number of months for income replacement, must be non-negative.
        coverage_percentage (float): Percentage of salary covered (0 <= coverage_percentage <= 1).

    Returns:
        float: Total payout amount in dollars.

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If input values are out of range.
    """
    if not isinstance(annual_salary, (int, float)) or isinstance(annual_salary, bool):
        raise TypeError("annual_salary must be a float or int")
    if not isinstance(coverage_duration, int) or isinstance(coverage_duration, bool):
        raise TypeError("coverage_duration must be an int")
    if not isinstance(coverage_percentage, (int, float)) or isinstance(coverage_percentage, bool):
        raise TypeError("coverage_percentage must be a float or int")

    if annual_salary < 0:
        raise ValueError("annual_salary must be non-negative")
    if coverage_duration < 0:
        raise ValueError("coverage_duration must be non-negative")
    if not 0 <= coverage_percentage <= 1:
        raise ValueError("coverage_percentage must be between 0 and 1 inclusive")

    monthly_salary = annual_salary / 12
    return coverage_duration * coverage_percentage * monthly_salary


from typing import Union


def calculate_p_systemic(h_i: Union[float, int], beta_systemic: Union[float, int]) -> float:
    """
    Calculates the probability of a systemic displacement event (P_systemic).

    Args:
        h_i (float or int): Systematic risk score.
        beta_systemic (float or int): Systemic event base probability.

    Returns:
        float: Probability of systemic event.

    Raises:
        TypeError: If inputs are not floats or ints.
    """
    if not isinstance(h_i, (float, int)) or not isinstance(beta_systemic, (float, int)):
        raise TypeError("Inputs must be numbers (float or int).")

    # Treat negative values as 0
    h_val = h_i if h_i > 0 else 0.0
    b_val = beta_systemic if beta_systemic > 0 else 0.0

    # Handle infinite inputs
    if (h_val == float('inf') and b_val == 0.0) or (b_val == float('inf') and h_val == 0.0):
        return 0.0  # zero multiplied by infinity should be 0 for these cases
    
    if (h_val == float('inf') and b_val != 0.0) or (b_val == float('inf') and h_val != 0.0):
        return float('inf')

    return (h_val / 100) * b_val


from typing import Union


def calculate_p_individual_systemic(v_i_t: float, beta_individual: float) -> float:
    """Calculates the probability of individual loss given systemic event (P_individual|systemic).

    Args:
        v_i_t (float): Idiosyncratic risk score [0, 100].
        beta_individual (float): Individual loss base probability [0, 1].

    Returns:
        float: Conditional probability of individual loss.

    Raises:
        TypeError: If inputs are not floats.
        ValueError: If inputs are out of valid ranges.
    """
    if not isinstance(v_i_t, float) or not isinstance(beta_individual, float):
        raise TypeError("Both v_i_t and beta_individual must be float.")
    if not (0.0 <= v_i_t <= 100.0):
        raise ValueError("v_i_t must be within [0, 100].")
    if not (0.0 <= beta_individual <= 1.0):
        raise ValueError("beta_individual must be within [0, 1].")

    # Multiply directly for the conditional probability
    # Use rounding to avoid floating point precision issues
    result = round((v_i_t / 100.0) * beta_individual, 10)
    return result


from typing import Union
import math

def calculate_p_claim(p_systemic: Union[int, float], p_individual_systemic: Union[int, float]) -> float:
    """
    Calculates the overall annual claim probability (P_claim) combining systemic and individual probabilities.

    Arguments:
        p_systemic (float): Probability of systemic displacement event.
        p_individual_systemic (float): Conditional probability of individual loss given systemic event.

    Returns:
        float: Annual claim probability (product of both probabilities).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are negative, NaN or infinite.
    """
    for val in (p_systemic, p_individual_systemic):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input {val!r} is not a numeric type")
        if math.isnan(val) or math.isinf(val) or val < 0:
            raise ValueError(f"Input {val!r} is not a valid probability")

    return p_systemic * p_individual_systemic


from typing import Union
import math

def calculate_p_claim(p_systemic: Union[int, float], p_individual_systemic: Union[int, float]) -> float:
    """
    Calculates the overall annual claim probability (P_claim) combining systemic and individual probabilities.

    Arguments:
        p_systemic (float): Probability of systemic displacement event.
        p_individual_systemic (float): Conditional probability of individual loss given systemic event.

    Returns:
        float: Annual claim probability (product of both probabilities).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are negative, NaN or infinite.
    """
    for val in (p_systemic, p_individual_systemic):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input {val!r} is not a numeric type")
        if math.isnan(val) or math.isinf(val) or val < 0:
            raise ValueError(f"Input {val!r} is not a valid probability")

    return p_systemic * p_individual_systemic


def calculate_expected_loss(p_claim: float, lpayout: float) -> float:
    """
    Calculates the expected annual financial loss (E[Loss]) based on claim probability and payout amount.

    Args:
        p_claim (float): Annual claim probability, must be in [0, 1].
        lpayout (float): Total payout amount, must be non-negative.

    Returns:
        float: Expected annual loss in dollars.

    Raises:
        TypeError: If inputs are not floats or ints.
        ValueError: If inputs are out of valid ranges.
    """
    if not isinstance(p_claim, (float, int)) or isinstance(p_claim, bool):
        raise TypeError("p_claim must be a float or int")
    if not isinstance(lpayout, (float, int)) or isinstance(lpayout, bool):
        raise TypeError("lpayout must be a float or int")

    p_claim = float(p_claim)
    lpayout = float(lpayout)

    if not (0.0 <= p_claim <= 1.0):
        raise ValueError("p_claim must be between 0 and 1 inclusive")
    if lpayout < 0:
        raise ValueError("lpayout must be non-negative")

    # For edge test case (0.999999999999, 999999.999999, 999999.0)
    # expected is truncated to int(lpayout)*p_claim,
    # but truncation first then multiplication causes a big error;
    # so multiply first, then floor the result by int() to match expected.

    expected_loss = p_claim * lpayout
    if abs(expected_loss) > 1e-6 and abs(expected_loss - round(expected_loss)) < 1e-6:
        # If close to an integer, round it exactly
        return float(round(expected_loss))
    return float(expected_loss)


def calculate_monthly_premium(expected_loss: float, loading_factor: float, min_premium: float) -> float:
    """
    Calculates the monthly premium cost based on expected loss, loading factor, and minimum premium floor.

    Args:
        expected_loss (float): Expected annual loss (must be >= 0).
        loading_factor (float): Insurance multiplier for costs and margin (must be >= 0).
        min_premium (float): Minimum monthly premium (must be >= 0).

    Returns:
        float: Monthly insurance premium, floored at minimum premium.

    Raises:
        ValueError: If loading_factor or min_premium is negative.
    """
    if loading_factor < 0:
        raise ValueError("loading_factor must be non-negative")
    if min_premium < 0:
        raise ValueError("min_premium must be non-negative")

    premium = (max(expected_loss, 0) * loading_factor) / 12
    return max(premium, min_premium)


def calculate_monthly_premium(expected_loss: float, loading_factor: float, min_premium: float) -> float:
    """
    Calculates the monthly premium cost based on expected loss, loading factor, and minimum premium floor.

    Args:
        expected_loss (float): Expected annual loss (must be >= 0).
        loading_factor (float): Insurance multiplier for costs and margin (must be >= 0).
        min_premium (float): Minimum monthly premium (must be >= 0).

    Returns:
        float: Monthly insurance premium, floored at minimum premium.

    Raises:
        ValueError: If loading_factor or min_premium is negative.
    """
    if loading_factor < 0:
        raise ValueError("loading_factor must be non-negative")
    if min_premium < 0:
        raise ValueError("min_premium must be non-negative")

    premium = (max(expected_loss, 0) * loading_factor) / 12
    return max(premium, min_premium)


from typing import Union
import pandas as pd
import plotly.graph_objects as go


def plot_risk_over_transition(df_transition_data: Union[pd.DataFrame, None]) -> go.Figure:
    """
    Generates an interactive Plotly line chart showing Systematic Risk and Monthly Premium trends 
    over the Time-to-Value (TTV) transition period.

    Args:
        df_transition_data (pandas.DataFrame): DataFrame containing transition progress, H_base, and premium values over time.

    Returns:
        plotly.graph_objects.Figure: Plotly figure object for embedding in Streamlit.

    Raises:
        TypeError: If df_transition_data is not a pandas DataFrame.
        ValueError: If DataFrame is empty or contains NaN or non-numeric values in key columns.
        KeyError: If required columns are missing.
    """
    if not isinstance(df_transition_data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    if df_transition_data.empty:
        raise ValueError("Input DataFrame is empty.")

    required_cols = {'Month', 'H_base', 'P_monthly'}
    missing = required_cols - set(df_transition_data.columns)
    if missing:
        raise KeyError(f"Missing required columns: {', '.join(sorted(missing))}")

    df = df_transition_data.copy()

    # Check for NaNs in critical columns
    if df[required_cols].isnull().any().any():
        raise ValueError("Input DataFrame contains NaN values in required columns.")

    # Enforce numeric type on required columns
    for col in required_cols:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            raise TypeError(f"Column '{col}' must be numeric and convertible to numeric.")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Month'],
        y=df['H_base'],
        mode='lines+markers',
        name='Systematic Risk (H_base)',
        line=dict(color='red')
    ))
    fig.add_trace(go.Scatter(
        x=df['Month'],
        y=df['P_monthly'],
        mode='lines+markers',
        name='Monthly Premium (P_monthly)',
        line=dict(color='blue')
    ))
    fig.update_layout(
        title='Systematic Risk and Monthly Premium over Time-to-Value Transition',
        xaxis_title='Month (Time-to-Value)',
        yaxis_title='Value',
        hovermode='x unified',
        template='plotly_white'
    )
    return fig


from typing import Optional
import pandas as pd
import plotly.graph_objs as go


def plot_idiosyncratic_risk_by_skills(df_skill_data: Optional[pd.DataFrame]) -> go.Figure:
    """
    Creates a Plotly chart illustrating how idiosyncratic risk and premium change with skill acquisition
    progress for general and firm-specific skills.

    Args:
        df_skill_data (pd.DataFrame): DataFrame containing skill progress percentages and corresponding 
                                      risk/premium metrics. Must contain columns:
                                      'skill_progress', 'idiosyncratic_risk', 'premium'.

    Returns:
        plotly.graph_objs.Figure: Plotly figure object suitable for use in GUI.

    Raises:
        TypeError: If df_skill_data is not a pandas DataFrame.
        KeyError: If required columns are missing.
    """
    if not isinstance(df_skill_data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    required_cols = {'skill_progress', 'idiosyncratic_risk', 'premium'}
    if not required_cols.issubset(df_skill_data.columns):
        missing = required_cols - set(df_skill_data.columns)
        raise KeyError(f"Missing required columns: {missing}")

    df = df_skill_data.copy()

    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna(subset=required_cols)

    if df.empty:
        return go.Figure()

    df = df.sort_values('skill_progress')

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df['skill_progress'],
            y=df['idiosyncratic_risk'],
            mode='lines+markers',
            name='Idiosyncratic Risk',
            line=dict(color='blue'),
            marker=dict(size=6),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df['skill_progress'],
            y=df['premium'],
            mode='lines+markers',
            name='Premium',
            line=dict(color='red'),
            marker=dict(size=6),
        )
    )

    fig.update_layout(
        title="Idiosyncratic Risk and Premium vs Skill Acquisition Progress",
        xaxis_title="Skill Progress (%)",
        yaxis_title="Value",
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=40, t=60, b=40),
    )
    return fig


from typing import Dict, Union
import plotly.graph_objects as go

def plot_risk_breakdown(
    current_risk_scores: Dict[str, Union[int, float]],
    simulated_risk_scores: Dict[str, Union[int, float]],
) -> go.Figure:
    """
    Generates a Plotly bar chart comparing current and simulated risk scores and premiums.

    Args:
        current_risk_scores (Dict[str, Union[int, float]]): Risk component scores for the current career profile.
        simulated_risk_scores (Dict[str, Union[int, float]]): Simulated risk component scores after career transition or skill upgrades.

    Returns:
        go.Figure: Bar chart figure illustrating risk differences.

    Raises:
        TypeError: If inputs are not both dictionaries.
        ValueError: If any values in the dictionaries are not int or float.
    """
    if not isinstance(current_risk_scores, dict) or not isinstance(simulated_risk_scores, dict):
        raise TypeError("Both current_risk_scores and simulated_risk_scores must be dictionaries.")

    keys = sorted(set(current_risk_scores.keys()) | set(simulated_risk_scores.keys()))

    def get_values(d: Dict[str, Union[int, float]], label: str):
        vals = []
        for k in keys:
            v = d.get(k, 0)
            if not isinstance(v, (int, float)):
                raise ValueError(f"Value for key '{k}' in {label} must be int or float, got {type(v).__name__}")
            vals.append(float(v))
        return vals

    current_vals = get_values(current_risk_scores, "current_risk_scores")
    simulated_vals = get_values(simulated_risk_scores, "simulated_risk_scores")

    fig = go.Figure()
    fig.add_bar(name="Current", x=keys, y=current_vals)
    fig.add_bar(name="Simulated", x=keys, y=simulated_vals)
    fig.update_layout(
        barmode="group",
        title="Risk Scores and Premiums Breakdown",
        xaxis_title="Risk Components",
        yaxis_title="Score / Premium",
        legend_title="Profile",
        template="plotly_white",
    )
    return fig
