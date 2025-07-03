# 🤖 Hallucination Risk Evaluator

This tool evaluates LLM-generated responses for hallucination risk using token uncertainty, fact verification, entity analysis, prompt stability, and human polling feedback.

## 🔧 Features
- Composite risk score (0–100%)
- Live human polling consensus input
- Entity anomaly detection
- Prompt instability estimator
- Streamlit dashboard

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
