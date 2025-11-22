import streamlit as st
import time

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="Distoversity | Mohd Saad – Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----- LIGHT THEME CSS -----
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: #F4F9FD !important;
        color: #0F172A !important;
    }
    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
    }
    h1, h2, h3, h4, h5, h6, p, span, div, label, li {
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important;
    }
    h1, h2, h3 {
        color: #003366 !important;
        -webkit-text-fill-color: #003366 !important;
    }
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
    }
    .d-card, .story-card, div[data-testid="stExpander"], .stMarkdown {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }
    .footer-note { font-size:0.98rem; color:#475569 !important; text-align:center; margin-top:20px; }
    a { color: #0077B6 !important; -webkit-text-fill-color: #0077B6 !important; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: BIO, BRAND, CONTACT ---
with st.sidebar:
    st.markdown("<h4 style='color:#0077B6;'>DISTOVERSITY</h4>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("**Founder | EdTech Entrepreneur**")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'sales' in education with 'science' and empowerment.")
    st.markdown("---")
    st.markdown("### 🏆 Brand Expertise")
    st.code(
        "Franchise Expansion & Early Growth\n"
        "Career Counseling & Student Guidance\n"
        "EdTech (Python, Power BI, Streamlit)\n"
        "Student Support (UG/PG/Scholarships)\n"
        "Early Childhood (HighScope, Holistic ECE)\n"
        "Program Leadership & Team Building"
    )
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Your data is always safe and confidential.", unsafe_allow_html=True)
    st.markdown("Copyright © 2025 Distoversity. All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")

# ----- MAIN BRAND INTRO (Landing Hook) -----
st.header("From Classroom to Changemaker: Distoversity’s 10-Year Journey 🚀")
st.markdown("##### *How on-ground wisdom, tech, and passion built a brand for India's future*")
st.markdown("<h3 style='color:#0077B6;'>BUILDING FUTURES, NOT JUST CAREERS</h3>", unsafe_allow_html=True)
st.divider()

st.markdown("""
I’m **Mohd Saad**, and this is how Distoversity was born.
<br><br>
**2015–2019: Classroom Foundations**  
I started as a teacher, living inside India’s classrooms—discovering that impact is about mentorship, not just marks. Every child has a dream; most just lack a champion.
<br><br>
**2020–2021: Corporate Insight**  
I entered the powerhouse world of OPPO and Yazaki. Here, I learned scale, systems, and operational grit—but the calling to uplift Indian education never left me.
<br><br>
**2021–2025: Counseling, Leadership & Scaling Change**  
From Amity to Manipal, UNIVO, NMIMS, NIU—over 2,000 students and families guided. I turned counseling into career architecture, focusing on real futures, not just admissions.  
At **Footprints Day Care**, I led expansion into new cities and championed holistic, global early childhood models (HighScope USA), proving that business and care can—and should—grow together.
<br><br>
**Tech as a Bridge: EdTech Innovator**  
My love for problem-solving led me from counseling rooms to code—building dashboards (Power BI), rapid solutions (Python/Streamlit), and launching data-driven guidance, so every decision in education is smarter and fairer.
<br><br>
---

### Why Distoversity?
Distoversity isn’t just a company, it’s the answer to a decade of ground lessons. I saw India’s education gaps up close, and the solution isn’t just more tech or more sales—it’s **personalization, ethics, analytics, and heart**.
<br><br>
**Distoversity is my promise:** To democratize access, empower every student, and build a new brand of education leadership for India.
""", unsafe_allow_html=True)

st.success("🌱 Empowering India's next generation—one learner, family, and school at a time.")

# Key Expertise Cards (showcase as brand)
st.markdown("#### My Sectoral Impact & Brand Differentiators")
cols = st.columns(3)
with cols[0]:
    st.info("**2,000+ students/families guided**\n\nAcross India’s top universities and programs.")
with cols[1]:
    st.success("**Franchise Growth:**\n\nScaled Footprints Day Care into new cities with holistic ECE (HighScope) models.")
with cols[2]:
    st.warning("**Built EdTech Tools:**\n\nPower BI dashboards, Python/Streamlit solutions for smarter education.")

#---------- OPTIONAL: Extra Inspiration / Testimonials section ----------
st.markdown("""
---
##### A Brand for the Future
> "*Distoversity is built on the belief that every learner in India deserves world-class, personal guidance — not just ‘admissions support’, but lifelong empowerment.*"
""")

# Footer Brand Note
st.markdown("""
<div class="footer-note">
<b>DISTOVERSITY – EMPOWERING INDIA</b><br>
<b>Privacy Policy:</b> We do NOT collect, share, or sell your personal data. All information is confidential.<br>
<b>Copyright © 2025 Distoversity. All rights reserved.</b>
</div>
""", unsafe_allow_html=True)
