#Purpose: User interface with voice/text input, chatbot response, calculators, and charts. - Main streamlit app
import streamlit as st
from rag_pipeline import get_llm_response
from speech_utils import transcribe_audio, speak_text
from finance_tools import calculate_sip, calculate_emi
from chart_utils import plot_investment_growth

st.set_page_config(page_title="Finance Chatbot", layout="centered")
st.title("💰 Financial Independence Chatbot")

st.markdown("Ask me anything about budgeting, investing, loans, or financial planning!")

input_mode = st.radio("Choose input mode:", ["Text", "Voice"])

if input_mode == "Text":
    user_input = st.text_input("Your question:")
else:
    audio_file = st.file_uploader("Upload your question (audio)", type=["wav", "mp3"])
    if audio_file:
        user_input = transcribe_audio(audio_file)

if user_input:
    with st.spinner("Thinking..."):
        response = get_llm_response(user_input)
        st.success(response)
        speak_text(response)

    st.markdown("Would you like to try a calculator or see a chart?")

st.header("📊 Finance Tools")

with st.expander("SIP Calculator"):
    monthly_investment = st.number_input("Monthly Investment (₹)", value=5000)
    annual_return = st.slider("Expected Annual Return (%)", 5.0, 15.0, 10.0)
    years = st.slider("Investment Duration (Years)", 1, 30, 10)
    if st.button("Calculate SIP"):
        total = calculate_sip(monthly_investment, annual_return, years)
        st.success(f"Estimated corpus: ₹{total:,.2f}")
        plot_investment_growth(monthly_investment, annual_return, years)

with st.expander("EMI Calculator"):
    loan_amount = st.number_input("Loan Amount (₹)", value=500000)
    interest_rate = st.slider("Annual Interest Rate (%)", 5.0, 15.0, 8.5)
    tenure_years = st.slider("Loan Tenure (Years)", 1, 30, 10)
    if st.button("Calculate EMI"):
        emi = calculate_emi(loan_amount, interest_rate, tenure_years)
        st.success(f"Monthly EMI: ₹{emi:,.2f}")
