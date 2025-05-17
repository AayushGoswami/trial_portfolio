import streamlit as st
from PIL import Image

# -------------------- Config --------------------
st.set_page_config(page_title="AI Freelancer Portfolio", layout="wide")
st.title("👋 Hi, I'm Your Name")
st.subheader("AI Web App Developer | Python · Streamlit · LLMs · Chatbots")
st.markdown("""
🚀 I build custom AI-powered web apps using Streamlit, OpenAI, Gemini, and Python.
Let's turn your ideas into intelligent, interactive tools.
""")

# -------------------- CTA Buttons --------------------
col1, col2 = st.columns([1,1])
with col1:
    st.markdown('[📬 Hire Me](mailto:silver.bittu@gmail.com)', unsafe_allow_html=True)
with col2:
    with open("Resume.pdf", "rb") as file:
        st.download_button("📄 Download Resume", file, file_name="Resume.pdf")

# -------------------- Services --------------------
st.markdown("---")
st.header("💼 Services")
col1, col2 = st.columns(2)
col1.markdown("""
- 🤖 **Custom Chatbots** (OpenAI / Gemini)
- 📊 **AI Dashboards** (Streamlit + Data)
- 🧠 **Emotion Recognition Apps** (Live camera)
""")
col2.markdown("""
- ✅ **Fake News Detection**
- 🎓 **AI Tutor Tools for EdTech**
- 🌐 **Web Deployment & API Integration**
""")

# -------------------- Projects --------------------
st.markdown("---")
st.header("📁 Featured Projects")

with st.expander("🧠 Fake News Detection Web App"):
    st.image("fake_news.png", width=500)
    st.write("Detects fake news from article links or screenshots using NLP and fact-checking APIs. Built with Streamlit and HuggingFace.")
    st.markdown("[GitHub Repo](https://github.com/yourprofile/fake-news-detector)")

with st.expander("💬 AI Chatbot for E-commerce"):
    st.image("chatbot.png", width=500)
    st.write("Product recommendation and FAQ chatbot using OpenAI API and LangChain.")
    st.markdown("[GitHub Repo](https://github.com/yourprofile/ecommerce-chatbot)")

with st.expander("🧠 Real-time Emotion Detection App"):
    st.image("emotion.png", width=500)
    st.write("Recognizes emotions from webcam feed using fine-tuned deep learning models + OpenCV.")
    st.markdown("[GitHub Repo](https://github.com/yourprofile/emotion-recognition)")

# -------------------- Tech Stack --------------------
st.markdown("---")
st.header("🛠️ Tech Stack")
st.markdown("""
**Languages & Tools:** Python, Streamlit, Flask, Git, HuggingFace

**AI Frameworks:** OpenAI API, Gemini, LangChain, LLaMA, LoRA, QLoRA

**Libraries:** NumPy, Pandas, Scikit-learn, PyTorch, OpenCV
""")

# -------------------- Contact Form --------------------
st.markdown("---")
st.header("📬 Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks! I’ll get back to you soon.")

# -------------------- Footer --------------------
st.markdown("""
---
© 2025 Your Name · Made with ❤️ and Python  
[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourprofile) | [Fiverr](https://fiverr.com/yourprofile) | [Upwork](https://upwork.com/freelancers/yourprofile)
""")
