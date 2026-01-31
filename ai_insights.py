import os
from openai import OpenAI

def generate_ai_insights(metrics, risk):
    """
    Generates AI insights.
    Falls back to rule-based insights if OpenAI is unavailable.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return fallback_insights(metrics, risk)

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a financial advisor for SMEs.

Metrics:
{metrics}

Risk:
{risk}

Explain:
1. Financial health summary
2. Key risks
3. Cost optimization ideas
4. Credit readiness

Use simple business language.
"""

        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception:
        # SSL / network / API errors handled here
        return fallback_insights(metrics, risk)


def fallback_insights(metrics, risk):
    return f"""
Financial Health Summary:
The business shows an average monthly revenue of {metrics['average_revenue']} with
a cash flow of {metrics['average_cash_flow']}.

Risk Assessment:
Overall risk level is {risk['risk_level']}. Key risks include:
{', '.join(risk['risk_factors']) if risk['risk_factors'] else 'No major risks detected.'}

Cost Optimization:
Review operating expenses and improve collections from receivables.

Credit Readiness:
Based on current metrics, the business has moderate readiness for external credit.
"""
