import pandas as pd

def calculate_financial_metrics(df: pd.DataFrame):
    df["cash_flow"] = df["revenue"] - df["expenses"]

    return {
        "average_revenue": round(df["revenue"].mean(), 2),
        "average_expenses": round(df["expenses"].mean(), 2),
        "average_cash_flow": round(df["cash_flow"].mean(), 2),
        "current_ratio": round(
            df["accounts_receivable"].mean() /
            df["accounts_payable"].mean(), 2
        ),
        "debt_to_equity": round(
            df["loan_outstanding"].iloc[-1] /
            df["revenue"].mean(), 2
        ),
        "negative_cash_flow_months": int(
            (df["cash_flow"] < 0).sum()
        )
    }
