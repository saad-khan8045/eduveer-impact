import streamlit as st
import pandas as pd
import time
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL CSS: SIDEBAR, ARROW, MOBILE ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
body, html, [data-testid="stAppViewContainer"], .stApp {
    font-family: "Inter", "Montserrat", Arial, sans-serif !important;
}
section[data-testid="stSidebar"] > div {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0;
    width: 340px !important;
    min-width: 340px !important;
    position: relative;
    box-sizing: border-box;
}
.sidebar-arrow-btn {
    position: absolute;
    top: 47%;
    right: -21px;
    transform: translateY(-50%);
    font-size: 2.1em;
    background: linear-gradient(135deg,#0077B6,#42a6de);
    color: #fff;
    border-radius: 999px;
    width: 42px;
    height: 42px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 18px #e4ecf6;
    cursor: pointer;
    transition: background 0.13s, color 0.13s, box-shadow 0.13s;
    z-index: 99;
    border: none; outline: none;
    border:1.5px solid #d1eafd;
}
.sidebar-arrow-btn:hover {
    background: linear-gradient(135deg,#0095ff,#42a6de);
    color: #fff;
    box-shadow: 0 12px 38px #bad6f9;
}
@media screen and (max-width: 600px) {
    section[data-testid="stSidebar"] > div {
        min-width: 97vw !important;
        width: 97vw !important;
    }
    .sidebar-arrow-btn { right: 8px; top:54%; }
}
h1, h2, h3, h4 {
    font-family: "Montserrat", Arial, sans-serif !important;
    color: #19376D !important;
    font-weight: 700;
}
.stMarkdown, div, p, label { font-family: "Inter", Arial, sans-serif !important; }
.footer-note {
    font-size:0.95em; color:#758fa0 !important; text-align:center; margin-top:30px;
    font-family:"Montserrat",Arial,sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: BIO, BRAND, ARROW, CONTACT ---
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;font-weight:800;'>DISTOVERSITY | EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | EdTech Entrepreneur | Early Childhood & EdTech Leader")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science', Ethics, and Empowerment.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-bottom:18px;">
        <span style="font-size:1.12em;color:#1b376d;font-weight:700;">🚀 Key Skills & Domain Expertise</span>
        <br><br>
        <span style="font-size:1em;color:#235789;font-weight:600;">Teaching & Educational Mentorship</span><br>
        <span style="color:#364958;font-size:0.97em;">• 10+ years ground teaching, student empowerment.<br>• Pedagogy, curriculum development, mentorship.</span>
        <br><br>
        <span style="font-size:1em;color:#235789;font-weight:600;">Data Analyst & EdTech Solutions</span><br>
        <span style="color:#364958;font-size:0.97em;">• Dashboards/analytics for franchise & careers.<br>• Python, Streamlit, Power BI for education transformation.</span>
        <br><br>
        <span style="font-size:1em;color:#235789;font-weight:600;">Domain Expertise: Franchise Expansion, Counseling</span><br>
        <span style="color:#364958;font-size:0.97em;">• Leadership in multi-city franchise growth (Footprints Daycare), admissions, guidance.<br>• Early childhood (HighScope USA), business strategy.</span>
        <br><br>
        <span style="font-size:0.97em;color:#075985;">Ed-Psychology | AI Agents | Team Leadership | Business Development</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<button class='sidebar-arrow-btn' title='Expand/Collapse Sidebar'>❯</button>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Your data is always safe and confidential.", unsafe_allow_html=True)
    st.markdown("Copyright © 2025 Distoversity. All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")
    st.markdown("---")
    st.markdown("## Try our AI Career Platform")
    st.markdown(
        "<a href='https://distoversity-mvp-j4pmyhqdjr7v7ukpgwmyx6.streamlit.app/' target='_blank'>👉 Distoversity AI Career Platform</a>",
        unsafe_allow_html=True
    )

# --- QUIZ & PROFILE DATA ---
UNIVERSITIES = [
    {"name": "Amity Online", "programs": ["MBA", "MCA"], "fee": "₹1.75L", "badges": ["UGC", "NAAC A+"], "best_for": ["Analyst"], "high_pkg": "₹18 LPA"},
    {"name": "Manipal Jaipur", "programs": ["MBA", "BCA"], "fee": "₹1.50L", "badges": ["AICTE", "NAAC A+"], "best_for": ["Creator"], "high_pkg": "₹14 LPA"},
    {"name": "LPU Online", "programs": ["MBA", "BA"], "fee": "₹98k", "badges": ["UGC", "AICTE"], "best_for": ["Catalyst"], "high_pkg": "₹12 LPA"},
    {"name": "NMIMS Global", "programs": ["MBA (Ex)"], "fee": "₹4.0L", "badges": ["Top Ranked"], "best_for": ["Influencer"], "high_pkg": "₹24 LPA"}
]
QUESTIONS = [
    {"q": "When solving problems, you prefer:", "options": [("💡 Innovation", "Creator"), ("🗣️ Discussion", "Influencer"), ("📊 Data", "Analyst"), ("⚡ Action", "Catalyst")]},
    {"q": "Your ideal workspace:", "options": [("🎨 Studio", "Creator"), ("📢 Boardroom", "Influencer"), ("💻 Lab", "Analyst"), ("🏗️ Field", "Catalyst")]},
    {"q": "What motivates you?", "options": [("🚀 Creating", "Creator"), ("🤝 Connecting", "Influencer"), ("🔍 Analyzing", "Analyst"), ("✅ Doing", "Catalyst")]}
]
PROFILE_DESCRIPTIONS = {
    "Creator": "Innovative, big-picture, loves launching ideas. Best fit: Product Designer, Brand Builder, Strategy.",
    "Influencer": "Natural leader, communicator, energizes teams. Best fit: PR, HR, Client Relations, Media.",
    "Catalyst": "Efficient, action-oriented, gets results. Best fit: Ops Manager, Logistics, Project Execution.",
    "Analyst": "Precise, data-driven, solves puzzles. Best fit: Finance, Data, Engineering."
}
if "messages" not in st.session_state: st.session_state.messages = []
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
if "profile_result" not in st.session_state: st.session_state.profile_result = None

# --- MAIN TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 My Story (The Hook)",
    "🛤️ Why Teach For India?",
    "🧠 The 4-Genius Framework",
    "🤖 Eduveer AI (Live Demo)"
])

with tab1:
    st.header("From Classroom to Changemaker: The Distoversity Journey 🚀")
    st.markdown("##### *Built on a decade of ground realities and transformation in Indian education*")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div style="margin-bottom:22px;">
            <div style="font-size:1.1em;color:#0077B6;font-weight:800;margin-bottom:4px;">2015–2019</div>
            <div style="font-weight:700;">🧑‍🏫 Teaching Roots</div>
            <div style="color:#475569;">Started as a teacher, learning student realities & potential. Real education is mentorship, not marks.</div>
        </div>
        <div style="margin-bottom:22px;">
            <div style="font-size:1.1em;color:#0077B6;font-weight:800;margin-bottom:4px;">2020–2021</div>
            <div style="font-weight:700;">🏢 Industry Insight</div>
            <div style="color:#475569;">Oppo & Yazaki—corporate scale, but always with a purpose: education transformation.</div>
        </div>
        <div style="margin-bottom:22px;">
            <div style="font-size:1.1em;color:#F97316;font-weight:800;margin-bottom:4px;">2021–2025</div>
            <div style="font-weight:700;">🎓 Counseling & Leadership</div>
            <div style="color:#475569;">2,000+ students guided as counselor, architecting careers (Amity, Manipal, NMIMS, UNIVO...). Transformation, not transactions.</div>
        </div>
        <div style="margin-bottom:22px;">
            <div style="font-size:1.1em;color:#10B981;font-weight:800;margin-bottom:4px;">2024–Present</div>
            <div style="font-weight:700;">🚀 Distoversity Brand</div>
            <div style="color:#475569;">
                Founder of India's first platform to combine ground expertise, tech, and holistic curriculum for unbiased, personalized guidance.<br>
                <span style="font-weight:700;color:#0077B6;">Empowering futures. Not selling degrees. Architecting India's next generation.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("💡 Distoversity Brand Hook")
        st.markdown("""
        - Empowerment through teaching, counseling, analytics, and entrepreneurship.<br>
        - Real impact: sector leadership, 2,000+ careers shaped, continuous innovation.<br>
        - Built on authenticity, tech, and vision.
        """, unsafe_allow_html=True)
        st.success("🎓 Impact: 2,000+ students served | 35% improved career satisfaction.")
        st.markdown("""
        <div class="card" style="margin-top:14px;">
            <h4>Success Story: Riya</h4>
            <p>Riya matched her skills to her destiny, not just a degree, thanks to personalized guidance.</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("Why Distoversity? Why Teach For India?")
    st.markdown("""
    - Every learner deserves ethical, world-class guidance.
    - Real impact means lives transformed, not deals closed.
    - Blending AI, psychology, and ground wisdom for the right path.
    - India's next mentorship movement—hope, credibility, scaling futures.
    """)
    st.success("🌱 Together, let's build India's new generation of empowered learners.")
    st.info("🤝 Ready for collaboration: [Connect on LinkedIn](https://linkedin.com)")

with tab3:
    st.header("We don't ask for Marks. We ask for Energy.")
    st.write("Distoversity philosophy: Guidance should measure energy, not only ability. Every child has unique strengths.")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        energy = st.selectbox("Select a Profile to Analyze:", ["Creator", "Influencer", "Catalyst", "Analyst"])
    with c2:
        if energy:
            st.markdown(f"**{energy}:** {PROFILE_DESCRIPTIONS[energy]}")
            if energy == "Creator": st.success("🌟 Vision-driven. Loves freedom. Struggles with routine.")
            if energy == "Influencer": st.warning("🔥 People-driven. Loves collaboration. Hates isolation.")
            if energy == "Catalyst": st.info("🤝 Results-driven. Loves action. Hates chaos.")
            if energy == "Analyst": st.error("📊 Data-driven. Needs clarity. Hates hype.")

with tab4:
    st.title("🤖 Eduveer AI Demo")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.caption("AI logic-powered career profiler for Indian students.")
    if st.session_state.step == 0:
        if st.button("Start AI Assessment ➔", type="primary"):
            st.session_state.step = 1
            st.rerun()
    elif st.session_state.step == 1:
        curr = QUESTIONS[st.session_state.q_index]
        st.markdown(f"**Q{st.session_state.q_index + 1}:** {curr['q']}")
        cols = st.columns(2)
        for i, (txt, en) in enumerate(curr["options"]):
            if cols[i%2].button(txt, key=f"btn_{i}_{st.session_state.q_index}"):
                st.session_state.scores[en] += 1
                if st.session_state.q_index < len(QUESTIONS)-1:
                    st.session_state.q_index += 1
                else:
                    st.session_state.step = 2
                st.rerun()
    elif st.session_state.step == 2:
        primary = max(st.session_state.scores, key=st.session_state.scores.get)
        st.success(f"🎉 Result: You are a {primary}!")
        st.write(PROFILE_DESCRIPTIONS[primary])
        st.write("Recommended Universities:")
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:15px; border:1px solid #ddd; border-radius:10px; margin-bottom:10px;">
                <h4>{u['name']}</h4>
                <p><b>Programs:</b> {', '.join(u['programs'])} | <b>Fee:</b> {u['fee']} | <b>Highest Pkg:</b> {u['high_pkg']}</p>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Restart Demo"):
            st.session_state.step = 0
            st.session_state.q_index = 0
            st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
            st.rerun()

st.markdown("""
<div class="footer-note">
DISTOVERSITY | EMPOWERING INDIA 🇮🇳<br>
Privacy Policy: We do NOT collect, share, or sell your personal data. All information is confidential.<br>
Copyright © 2025 Distoversity. All rights reserved.
</div>
""", unsafe_allow_html=True)
