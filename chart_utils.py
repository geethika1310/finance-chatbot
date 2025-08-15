import matplotlib.pyplot as plt
import streamlit as st

def plot_investment_growth(monthly_investment, annual_return, years):
    r = annual_return / 100 / 12
    months = years * 12
    values = []
    total = 0
    for i in range(1, months + 1):
        total = total * (1 + r) + monthly_investment
        values.append(total)

    plt.figure(figsize=(8, 4))
    plt.plot(range(1, months + 1), values, color='green')
    plt.title("Investment Growth Over Time")
    plt.xlabel("Months")
    plt.ylabel("Corpus (₹)")
    plt.grid(True)
    st.pyplot(plt)
