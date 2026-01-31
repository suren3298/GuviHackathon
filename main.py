from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

from financial_engine import calculate_financial_metrics
from risk_engine import calculate_risk
from ai_insights import generate_ai_insights

app = FastAPI(title="SME Financial Health Analyzer")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SME Financial Health Analyzer</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 900px;
                margin: 40px auto;
                background: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #2c3e50;
            }
            p.subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
            }
            .btn {
                display: block;
                width: 260px;
                margin: 0 auto 30px;
                padding: 12px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            .btn:hover {
                background-color: #0056b3;
            }
            .card {
                background: #f9fafb;
                padding: 20px;
                border-radius: 6px;
                margin-bottom: 20px;
            }
            .card h2 {
                margin-top: 0;
                color: #34495e;
            }
            pre {
                white-space: pre-wrap;
                font-size: 14px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI-Powered SME Financial Health Analyzer</h1>
            <p class="subtitle">
                Analyze financial health, risk, and credit readiness using AI-driven insights
            </p>

            <button class="btn" onclick="analyze()">Analyze Financial Data</button>

            <div id="output"></div>
        </div>

        <script>
            async function analyze() {
                const outputDiv = document.getElementById("output");
                outputDiv.innerHTML = "<p>Analyzing financial data...</p>";

                const response = await fetch("/analyze");
                const data = await response.json();

                outputDiv.innerHTML = `
                    <div class="card">
                        <h2>Financial Metrics</h2>
                        <pre>${JSON.stringify(data.financial_metrics, null, 2)}</pre>
                    </div>

                    <div class="card">
                        <h2>Risk Analysis</h2>
                        <pre>${JSON.stringify(data.risk_analysis, null, 2)}</pre>
                    </div>

                    <div class="card">
                        <h2>AI Insights</h2>
                        <pre>${data.ai_insights}</pre>
                    </div>
                `;
            }
        </script>
    </body>
    </html>
    """

@app.get("/analyze")
def analyze():
    df = pd.read_csv("data/sme_financials.csv")

    metrics = calculate_financial_metrics(df)
    risk = calculate_risk(metrics)
    insights = generate_ai_insights(metrics, risk)

    return {
        "financial_metrics": metrics,
        "risk_analysis": risk,
        "ai_insights": insights
    }
