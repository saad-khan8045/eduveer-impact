import streamlit as st

# --- PAGE FONTS & CONFIG ---
st.set_page_config(
    page_title="Distoversity | Founder Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Google Fonts (Montserrat for headings, Roboto for content)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
    html, body, [data-testid="stAppViewContainer"], .stApp {
        font-family: "Roboto", Arial, sans-serif !important;
        background-color: #F5F9FF !important;
        color: #273142 !important;
    }
    h1, h2, h3, h4 {
        font-family: "Montserrat", Arial, sans-serif !important;
        color: #19376D !important;
        font-weight: 700;
        margin-bottom: 0.8em;
    }
    .stTabs [role="tab"] {
        font-family: "Montserrat", Arial, sans-serif !important;
        font-size: 1.13em !important;
        color: #19376D !important;
    }
    .stMarkdown {
        font-family: "Roboto", Arial, sans-serif !important;
        font-size: 1.03em;
        color: #273142 !important;
    }
    .footer-note {
        font-size:0.97rem; color:#7B8794 !important; text-align:center; margin-top:32px;
        font-family: "Montserrat", Arial, sans-serif !important;
    }
    .story-card {background:#FFF; border-radius:16px; box-shadow:0 3px 12px #e3e3e3; padding:22px;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: BIO, BRAND, CONTACT ---
with st.sidebar:
    st.markdown("<h2 style='color:#0077B6;'>DISTOVERSITY</h2>", unsafe_allow_html=True)
    st.markdown("**Mohd Saad**", unsafe_allow_html=True)
    st.caption("Founder | EdTech Entrepreneur")
    st.markdown("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'sales' in education with 'science' and empowerment.")
    st.markdown("---")
    st.markdown("### 🏆 Brand Skills")
    st.code("Franchise Expansion & Early Growth\nCareer Counseling & Guidance\nEdTech (Python, Power BI, Streamlit)\nEarly Childhood (HighScope, Holistic ECE)\nProgram Leadership & Team Building")
    st.markdown("---")
    st.markdown("#### Contact")
    st.markdown("[LinkedIn](https://linkedin.com/in/your-link) · [Email](mailto:saad01489@gmail.com)", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.92em; color:#7B8794;margin-top:14px;text-align:left;'>Privacy Policy: Your data is always safe and confidential. Copyright © 2025 Distoversity.</div>
    """, unsafe_allow_html=True)

# ---- MAIN PAGE TABS ----
tab1, tab2, tab3, tab4 = st.tabs([
    "About/Founder",
    "Distoversity Mission",
    "Experience & Impact",
    "Contact"
])

# ---- TAB 1: ABOUT / STORY ----
with tab1:
    st.header("From Classroom to Changemaker: A Founder’s Journey 🚀")
    st.markdown("""
    <div class="story-card">
    <b>Hi, I’m Mohd Saad.</b> For 10 years, education has been my ground, my challenge, and my transformation.
    <ul>
    <li><b>2015–2019</b>: Started as a teacher; learned that real impact is about mentorship, confidence, and hope.</li>
    <li><b>2020–2021</b>: Joined OPPO and Yazaki; embraced operational excellence, but knew my real calling was in education.</li>
    <li><b>2021–2025</b>: Guided 2,000+ students and families at Amity, Manipal, UNIVO, NMIMS, NIU. Turned counseling into career architecture, focusing on futures, not just admissions.</li>
    <li><b>Footprints Day Care</b>: Led franchise growth into new cities and pushed holistic global early childhood models (HighScope USA).</li>
    <li><b>EdTech & Data</b>: Built solutions with Power BI, Python, and Streamlit—turning data into better decisions for students.</li>
    </ul>
    <b>Distoversity is built from a decade of these experiences, anchored in ethics, analytics, and heart.</b>
    </div>
    """, unsafe_allow_html=True)

# ---- TAB 2: DISTOVERSITY MISSION ----
with tab2:
    st.header("Distoversity: India’s Next-Gen Education Platform")
    st.markdown("""
    <div class="story-card">
    <b>Distoversity isn't just a company. It’s the movement to empower every Indian learner.</b>
    <ul>
    <li>Personalized, unbiased, ethical guidance—powered by ground experience and AI.</li>
    <li>Career discovery and mentorship at scale—moving beyond marks, sales, or old-school advice.</li>
    <li>Global best practices: Early childhood models (HighScope), tech-driven guidance, and strategic partnerships.</li>
    <li>Our promise: To democratize opportunity and empower every learner’s journey.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- TAB 3: EXPERIENCE/IMPACT ----
with tab3:
    st.header("Experience & Sector Impact")
    st.markdown("""
    <div class="story-card">
    <b>My Impact:</b>
    <ul>
    <li>Guided 2,000+ students/families across India’s top universities (Amity, Manipal, NMIMS, UNIVO, NIU, and more).</li>
    <li>Championed franchise growth (Footprints Day Care), delivering next-gen, holistic education in new cities.</li>
    <li>Designed and deployed EdTech/data solutions: Power BI dashboards, career analysis tools, rapid counseling platforms.</li>
    <li>Led program strategy, team mentorship, market research, and holistic early childhood initiatives.</li>
    </ul>
    <b>Sector Skills:</b> Franchise Expansion, Career Counseling, EdTech/Data Analytics, Early Childhood Development, Team Leadership.
    </div>
    """, unsafe_allow_html=True)

# ---- TAB 4: CONTACT ----
with tab4:
    st.header("Contact & Collaborate")
    st.markdown("""
    <div class="story-card">
    <b>Let's build a more empowered India together.</b><br>
    <ul>
    <li>Email: <a href='mailto:saad01489@gmail.com'>saad01489@gmail.com</a></li>
    <li>LinkedIn: <a href='https://linkedin.com/in/your-link'>linkedin.com/in/your-link</a></li>
    <li>Location: New Delhi, India</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("""
<div class="footer-note">
DISTOVERSITY – EMPOWERING INDIA<br>
Privacy Policy: We do NOT collect, share, or sell your personal data. All information is confidential.<br>
Copyright © 2025 Distoversity. All rights reserved.
</div>
""", unsafe_allow_html=True)
