def calculate_risk(metrics):
    score = 100
    risks = []

    if metrics["average_cash_flow"] < 0:
        score -= 30
        risks.append("Negative cash flow")

    if metrics["current_ratio"] < 1:
        score -= 20
        risks.append("Low liquidity")

    if metrics["debt_to_equity"] > 2:
        score -= 25
        risks.append("High debt burden")

    if metrics["negative_cash_flow_months"] >= 2:
        score -= 15
        risks.append("Multiple months of cash loss")

    score = max(score, 0)

    risk_level = (
        "Low Risk" if score >= 70 else
        "Medium Risk" if score >= 40 else
        "High Risk"
    )

    return {
        "financial_health_score": score,
        "risk_level": risk_level,
        "risk_factors": risks
    }
