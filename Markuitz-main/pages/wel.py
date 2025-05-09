import streamlit as st
import time

st.markdown("""
<style>
.gradient-orange {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
}
</style>

<div class="gradient-orange"> Welcome to the Portfolio Optimizer
<div class="sub-text">Start Your Investment Journey</div>            
""", unsafe_allow_html=True)




st.markdown("""
## 🎯 What is Markowitz Portfolio Theory?

Markowitz Portfolio Theory is a fundamental concept in modern finance.  
It helps investors **maximize returns** and **minimize risk** by diversifying their investments across multiple assets.

---

## 🧠 Purpose of This Website

This web app allows you to:

- Analyze the return-risk relationship between assets.
- Generate an optimized portfolio using Markowitz theory.
- Visualize the results through interactive charts.

---

## 📌 How to Use

1. Navigate to the **Portfolio** page.
2. Enter your **target return** and **mony** you invest
3. View the optimized portfolio and performance charts.

---


""")












st.markdown("""
<style>
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.bounce-button {
  text-align: center;
  padding: 15px 30px;
  font-size: 18px;
  font-weight: bold;
  background-color: #00c6ff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  animation: bounce 1s infinite;
}
</style>

<button class="bounce-button" onclick="window.location.href='pages/main.py'">🚀 Start Your Optimization</button>
""", unsafe_allow_html=True)







# تأثير عند الانتقال بين الصفحات
with st.spinner('Loading...'):
    time.sleep(1)  # الانتظار قبل الانتقال


col1, col2, col3 = st.columns([3, 6, 3])

with col1:
    if st.button("➡️ Go to About"):
        st.switch_page("pages/about.py")
        st.experimental_rerun()

with col3:
    if st.button("📈 Start Now"):
        st.switch_page("pages/main.py")
        st.experimental_rerun()