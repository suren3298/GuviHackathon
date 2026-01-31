# AI-Powered Financial Health Assessment Platform for SMEs

## Problem Statement
Small and Medium Enterprises (SMEs) often struggle to understand their financial health, manage cash flow, assess creditworthiness, and identify financial risks due to complex financial data and lack of expert guidance.

---

## Solution Overview
This project is an AI-powered financial health assessment platform designed for SMEs. It analyzes financial data to provide clear, actionable insights in simple business language, helping non-finance business owners make better financial decisions.

The platform evaluates financial health, identifies risks, assesses credit readiness, and suggests cost optimization strategies through an easy-to-use interface.

---

## Key Features
- Financial health scoring
- Risk and creditworthiness assessment
- Cash flow and liquidity analysis
- Cost optimization insights
- AI-generated business-friendly explanations
- Clean and simple user interface
- Resilient design with AI fallback when external services are unavailable

---

## Tech Stack
- Backend: FastAPI (Python)
- Data Processing: pandas
- AI Layer: OpenAI GPT (with fallback logic)
- Frontend: HTML, CSS, JavaScript (served via FastAPI)
- Deployment: Render
- Version Control: GitHub

---

## How It Works
1. Financial data is read from a CSV file.
2. Core financial metrics are calculated.
3. A risk and financial health score is generated.
4. AI (or fallback logic) produces human-readable insights.
5. Results are displayed in a clean web interface.

---

## How to Run Locally
```bash
pip install -r requirements.txt
python -m uvicorn main:app --port 8001
