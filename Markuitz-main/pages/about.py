import streamlit as st
import time

col1, col2 = st.columns([0.14, 0.86], gap="small")
col1.write("`Created by:`")
linkedin_url = "http://www.linkedin.com/in/khaledomarmohammed/"
col2.markdown(
        f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="15" height="15" style="vertical-align: middle; margin-right: 10px;">`Khaled Omar`</a>',
        unsafe_allow_html=True,
    )



st.markdown("""
<style>
@keyframes pulse {
  0% { opacity: 0.2; }
  50% { opacity: 1; }
  100% { opacity: 0.2; }
}

.gradient-text {
  text-align: center;
  font-size: 36px;
  font-weight: bold;
  background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: pulse 3s infinite;
  margin-bottom: 0;
}
.sub-text {
  text-align: center;
  font-size: 20px;
  color: #555;
  font-style: italic;
}
</style>

<div class="gradient-text"> Welcome to the Portfolio Optimizer</div>
""", unsafe_allow_html=True)

st.title("ℹ️ About This Project")

st.markdown("""
## 📝 Project Overview

This project is built using [Streamlit](https://streamlit.io) to provide a simple and interactive interface  
for applying **Markowitz Portfolio Theory** to real financial data.

---

## 👥 Development Team

- **Khaled Omar** 
- **Omar Mohammed** 
- **Mohammed Osama** 
- **Esraa Harby** 
- **Alaa Ashraf** 



---

## 📚 Tools & Resources

- **Python Libraries**: Streamlit, NumPy, Pandas,  Plotly.Express, Yfinance, Scipy.Pptimize  
- **Finance Concepts**: Modern Portfolio Theory, Risk vs. Return

---

## 💡 Goal

To help users understand portfolio optimization by providing a practical tool  
that combines finance theory with data visualization.

---

🎓 **This is a Graduated Project**
""")

# تأثير عند الانتقال بين الصفحات
with st.spinner('Loading...'):
    time.sleep(1)  # الانتظار قبل الانتقال


col1, col2, col3 = st.columns([3, 6, 3])

with col1:
    if st.button("⬅️ Back to Welcome"):
        st.switch_page("pages/wel.py")
        st.experimental_rerun()

with col3:
    
    if st.button("➡️ Go to Portfolio"):
        st.switch_page("pages/main.py")
        st.experimental_rerun()