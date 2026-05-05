import streamlit as st
import requests
import json

st.set_page_config(page_title="Valura AI", layout="wide")

st.title("💰 Valura AI Co-Investor")

# -------------------------
# Input Section
# -------------------------
query = st.text_input("Ask your question:")

portfolio_input = st.text_area(
    "Portfolio (JSON format):",
    value="""[
{"ticker": "AAPL", "value": 60000},
{"ticker": "TSLA", "value": 20000}
]"""
)

submit = st.button("Analyze")

# -------------------------
# Output Section
# -------------------------
output_box = st.empty()

if submit:
    if not query:
        st.warning("Please enter a query")
    else:
        try:
            portfolio = json.loads(portfolio_input)
        except:
            st.error("Invalid JSON format")
            st.stop()

        try:
            with st.spinner("Processing..."):

                response = requests.post(
                    "http://127.0.0.1:8000/query",
                    json={
                        "query": query,
                        "session_id": "streamlit_user",
                        "portfolio": portfolio
                    },
                    stream=True
                )

                full_response = ""

                for line in response.iter_lines():
                    if line:
                        decoded = line.decode("utf-8")

                        # Extract only data lines
                        if decoded.startswith("data:"):
                            data = decoded.replace("data:", "").strip()
                            full_response += data + "\n"

                            output_box.text(full_response)

        except Exception as e:
            st.error(f"Error: {e}")