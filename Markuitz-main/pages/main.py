
import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit_shadcn_ui as ui

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import time
import warnings

from PIL import Image
# from Markuitz.interpretations import  optimization_strategies_info, appinfo ##metric_info, var_info,##
from portfolio_optimizer import PortfolioOptimizer


def main():
    ##تحميل الصورة وإعداد الصفحة
    # im = Image.open("EfficientFrontier.png")
    # st.set_page_config(page_title="Portfolio Optimization Dashboard", page_icon=im)
    
    ##title in page
    st.markdown("""
<style>
@keyframes wave {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.wave-text {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #0072ff;
    animation: wave 2s infinite;
}
</style>

<div class="wave-text">📈 Smart Investing Starts Here</div>
""", unsafe_allow_html=True)
   

    




    cont1 = st.container(border=True)
    cont1.markdown("### Input Parameters")
    money = cont1.number_input(
        "Enter How much you will invest ($)", value=None, step=100, placeholder="enter a number $..."##value=##default_tickers_str
    )
   
    
        
    UserReturn = cont1.number_input(
        "Return of investment (%)",
        min_value=0.0,
        max_value=100.0,
        step=5.0,
        format="%0.8f",
        value=None,
        placeholder="enter persantage %...",
        help = "enter return you want earn from your investment"
    )
    calc = cont1.button("Calculate")
    if calc:
        try:
            with st.spinner("Buckle Up! Financial Wizardry in Progress...."):
                optimizer = PortfolioOptimizer(
                    ['AAPL', 'JNJ', 'PG', 'JPM', 'XOM', 'AMZN', 'KO', 'MSFT', 'GOLD', 'CVX'],
                    '2015-01-01',
                    '2023-12-30',
                    "stock_data.xlsx",
                    UserReturn,
                    0.044,
                )
                # Get and process optimized allocation (as DataFrame)
                optimizer.optimized_allocation["allocation"] = optimizer.optimized_allocation["allocation"].apply(lambda x: round(x * 100, 2))

                # Rename for clarity in display
                optimizer.optimized_allocation.rename(columns={"allocation": "Allocation (%)"}, inplace=True)

        except ValueError as e:
            st.error("Unable to download data for one or more tickers!")
            return
        except Exception as e:
            st.error(str(e))
            return        
        with st.container(border=True):
                tab1, tab2 = st.tabs(
                   [
                      "",
                      "Distribution",
                      
                   ]
                )
                with tab1:
                    st.markdown("#### Optimized Portfolio Performance")
                    
                    w_opt_markowitz=optimizer.singleEquationSolver()
                    risk_markowitz=optimizer.riskFunction(w_opt_markowitz)
                    ret_markowitz=optimizer.portfolioReturn(w_opt_markowitz)
                    st.markdown(f"**Expected Annual Return**: {ret_markowitz:.2%}")
                    st.markdown(f"**Portfolio Risk**: {risk_markowitz:.2%}")

                    st.markdown("#### Specific Optimized Portfolio Performance")
                    w_opt_specific_return = optimizer.markowitz_optimal_weights_specific_return(UserReturn/100)
                    risk_specific_return = optimizer.riskFunction(w_opt_specific_return)
                    ret_specific_return = optimizer.portfolioReturn(w_opt_specific_return)
                    st.markdown(f"**Expected Annual Return**: {ret_specific_return:.2%}")
                    st.markdown(f"**Portfolio Risk**: {risk_specific_return:.4%}")

                    st.markdown(f"Sum of Weights: {np.sum(w_opt_specific_return):.4f}")
                    ret_mony=(ret_specific_return)*money
                    st.markdown(f"**Your Many After Investment**: {(ret_mony+money):.2f}")

                    
                with tab2:
                    st.markdown("#### Optimized Portfolio Distribution")
                    

                    alocCol, pieCol = st.columns(2)

                    with alocCol:
                        allocations = optimizer.optimized_allocation.copy()  # avoid modifying original df
                        allocations["Tickers"] = allocations.index
                        allocations = allocations[["Tickers", "Allocation (%)"]]

                        # Use Streamlit's built-in table (assuming you're not using a custom `ui.table`)
                        st.table(allocations)

                    with pieCol:
                        sharpeChart = optimizer.optimized_allocation[
                            optimizer.optimized_allocation["Allocation (%)"] != 0
                        ].copy()

                        fig = px.pie(
                            sharpeChart,
                            values="Allocation (%)",
                            names=sharpeChart.index,
                        )
                        fig.update_layout(
                            width=180,
                            height=200,
                            showlegend=False,
                            margin=dict(t=20, b=0, l=0, r=0),
                        )
                        st.plotly_chart(fig, use_container_width=True)
    # تأثير عند الانتقال بين الصفحات
    with st.spinner('Loading...'):
        time.sleep(1)  # الانتظار قبل الانتقال
                                 
    col1, col2, col3 = st.columns([3, 4, 2])

    with col1:
        if st.button("⬅️ Back to Welcome"):
            st.switch_page("pages/wel.py")
            st.experimental_rerun()

    with col3:
        if st.button("➡️ Go to About"):
            st.switch_page("pages/About.py")
            st.experimental_rerun()

# if __name__ == "__main__":
main()

