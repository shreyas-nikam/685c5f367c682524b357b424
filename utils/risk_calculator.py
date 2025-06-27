
import numpy as np

def calculate_fexp(years_experience):
    """
    Calculates the Experience Factor (f_exp).
    f_exp = 1 - (0.015 * min(Yrs, 20))
    """
    return 1 - (0.015 * min(years_experience, 20))

def calculate_fhc(role_multiplier, edu_level_factor, edu_field_factor, school_tier_factor, fexp_value):
    """
    Calculates the Human Capital Factor (FHC).
    FHC = f_role * f_level * f_field * f_school * f_exp
    """
    return role_multiplier * edu_level_factor * edu_field_factor * school_tier_factor * fexp_value

def calculate_fcr(sentiment_score, financial_health_score, growth_ai_adoption_score, w1=0.33, w2=0.33, w3=0.34):
    """
    Calculates the Company Risk Factor (F_CR).
    F_CR = w_1 * S_senti + w_2 * S_fin + w_3 * S_growth
    For simplicity, S_senti, S_fin, S_growth will be simulated/fixed in the app.
    """
    return (w1 * sentiment_score + w2 * financial_health_score + w3 * growth_ai_adoption_score)

def calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec):
    """
    Calculates the Upskilling Factor (F_US).
    F_US = 1 - (gamma_gen * P_gen(t) + gamma_spec * P_spec(t))
    """
    return 1 - (gamma_gen * p_gen + gamma_spec * p_spec)

def calculate_idiosyncratic_risk(fhc, fcr, fus, w_cr, w_us):
    """
    Calculates the Idiosyncratic Risk (V_i(t)).
    V_raw = FHC * (w_CR * FCR + w_US * FUS)
    V_i(t) = min(100.0, max(5.0, V_raw * 50.0))
    """
    v_raw = fhc * (w_cr * fcr + w_us * fus)
    return min(100.0, max(5.0, v_raw * 50.0))

def calculate_h_base_ttv(k, ttv, h_current, h_target):
    """
    Calculates the Base Occupational Hazard with Transition Time-to-Value (TTV) Modifier (H_base(k)).
    H_base(k) = (1 - k/TTV) * H_current + (k/TTV) * H_target
    """
    if ttv == 0: # Avoid division by zero
        return h_target
    if k >= ttv: # If transition is complete or beyond TTV
        return h_target
    return (1 - k / ttv) * h_current + (k / ttv) * h_target

def calculate_systematic_risk(h_base_t, mecon, iai, w_econ, w_inno):
    """
    Calculates the Systematic Risk (H_i).
    H_i = H_base(t) * (w_econ * M_econ + w_inno * I_AI)
    """
    return h_base_t * (w_econ * mecon + w_inno * iai)

def calculate_payout_amount(annual_salary, coverage_duration, coverage_percentage):
    """
    Calculates the Total Payout Amount (L_payout).
    L_payout = (Annual Salary / 12) * Coverage Duration * Coverage Percentage
    """
    return (annual_salary / 12) * coverage_duration * coverage_percentage

def calculate_p_systemic(h_i, beta_systemic):
    """
    Calculates the Probability of a Systemic Event (P_systemic).
    P_systemic = (H_i / 100) * beta_systemic
    """
    return (h_i / 100) * beta_systemic

def calculate_p_individual_systemic(v_i_t, beta_individual):
    """
    Calculates the Conditional Probability of Job Loss Given a Systemic Event (P_individual|systemic).
    P_individual|systemic = (V_i(t) / 100) * beta_individual
    """
    return (v_i_t / 100) * beta_individual

def calculate_p_claim(p_systemic, p_individual_systemic):
    """
    Calculates the Annual Claim Probability (P_claim).
    P_claim = P_systemic * P_individual|systemic
    """
    return p_systemic * p_individual_systemic

def calculate_expected_loss(p_claim, lpayout):
    """
    Calculates the Annual Expected Loss (E[Loss]).
    E[Loss] = P_claim * L_payout
    """
    return p_claim * lpayout

def calculate_monthly_premium(expected_loss, loading_factor, min_premium):
    """
    Calculates the Final Monthly Premium (P_monthly).
    P_monthly = max((E[Loss] * lambda) / 12, P_min)
    """
    return max((expected_loss * loading_factor) / 12, min_premium)
