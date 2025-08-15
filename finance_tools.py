def calculate_sip(monthly_investment, annual_return, years):
    r = annual_return / 100 / 12
    n = years * 12
    corpus = monthly_investment * (((1 + r) ** n - 1) * (1 + r)) / r
    return corpus

def calculate_emi(loan_amount, annual_rate, tenure_years):
    r = annual_rate / 100 / 12
    n = tenure_years * 12
    emi = loan_amount * r * ((1 + r) ** n) / ((1 + r) ** n - 1)
    return emi
