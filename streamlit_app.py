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

# --- PROFESSIONAL VISUAL CSS + SIDEBAR ARROW + MOBILE PROMPT ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: #F4F9FD !important;
        color: #0F172A !important;
    }
    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
        width: 330px !important;
        min-width: 330px !important;
        position: relative;
    }
    .expand-arrow {
        position: absolute;
        top: 50%;
        right: -22px;
        transform: translateY(-50%);
        font-size: 2.2em;
        background: #E0F2FE;
        border-radius: 50px;
        padding: 1px 9px;
        color: #1892d8;
        box-shadow: 0 2px 6px #dbe7fd;
        cursor: pointer;
        transition: background 0.11s;
        z-index: 100;
    }
    .expand-arrow:hover {
        background: #bde0fa;
        color: #0077B6;
    }
    @media screen and (max-width: 600px) {
        section[data-testid="stSidebar"] > div {
            min-width: 95vw !important;
            width: 95vw !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# --- UNIVERSITY & QUIZ DATA ---
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
# --- SESSION STATE ---
if "messages" not in st.session_state: st.session_state.messages = []
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
if "profile_result" not in st.session_state: st.session_state.profile_result = None

# --- SIDEBAR: BIO, PRIVACY & COPYRIGHT + ARROW + REDIRECT ---
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;font-weight:800;'>DISTOVERSITY | EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | Ed-Tech Intrapreneur | Early Childhood & EdTech Leader")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science', Ethics, and Empowerment.")
    st.markdown("### <span style='color:#19376D;font-size:1.18em;'>🚀 Key Skills & Domain Expertise</span>", unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-bottom:12px;">
        <span style="font-size:1.09em;color:#235789;font-weight:700;">Teaching & Educational Mentorship</span><br>
        <span style="color:#364958;">• 10+ years in on-ground teaching, student empowerment.<br>
        • Pedagogy, curriculum design, holistic mentorship.</span>
    </div>
    <div style="margin-bottom:12px;">
        <span style="font-size:1.09em;color:#235789;font-weight:700;">Data Analyst & EdTech Solutions</span><br>
        <span style="color:#364958;">• Power BI dashboards for franchise & student analytics.<br>
        • Python, Streamlit & advanced analytics for decision-making.</span>
    </div>
    <div style="margin-bottom:12px;">
        <span style="font-size:1.09em;color:#235789;font-weight:700;">Domain Expertise: Education & Franchise Expansion</span><br>
        <span style="color:#364958;">• Multi-city franchise growth (Footprints Daycare).<br>
        • Admissions, career counseling, early childhood (HighScope USA), team leadership & analytics.</span>
    </div>
    <div style="margin-bottom:10px;">
        <span style="font-size:1em;color:#075985;">Ed-Psychology | LLM & AI Agents | Team Leadership | Business Development</span>
    </div>
    """, unsafe_allow_html=True)
    # Sidebar right arrow for expand/collapse visual cue
    st.markdown("<div class='expand-arrow' title='Expand/Collapse Sidebar'>❯</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Your data is always safe and confidential. We never sell or share personal information.", unsafe_allow_html=True)
    st.markdown("<b>Copyright © 2025 Distoversity.</b> All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")
    st.markdown("---")
    st.markdown("## Go to Career Guidance Platform (Distoversity)")
    st.markdown(
        "[👉 Try Distoversity AI Career Platform](https://distoversity-mvp-j4pmyhqdjr7v7ukpgwmyx6.streamlit.app/)",
        unsafe_allow_html=True
    )

# --- MAIN TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 My Story (The Hook)", 
    "🛤️ Why Teach For India?", 
    "🧠 The 4-Genius Framework", 
    "🤖 Eduveer AI (Live Demo)"
])

# --- TAB 1: STORY ---
with tab1:
    st.header("From Classroom to Changemaker: Building the Distoversity Brand 🚀")
    st.markdown("##### *Why a decade on the ground led to India's most trusted career guidance platform*")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div style="margin-bottom:22px;">
            <div style="font-size:1.2em;color:#0077B6;font-weight:800;margin-bottom:4px;">📅 <span style="background:#E0F2FE;border-radius:8px;padding:2px 12px 2px 8px;">2015 – 2019</span></div>
            <div style="font-size:1.07em;font-weight:700;">🧑‍🏫 Classroom Roots</div>
            <div style="color:#475569;">
            Started as a teacher, discovering Indian students' real needs and dreams.<br>
            Learned that true education is about mentorship, courage, and personal growth—not just marks.
            </div>
        </div>
        <div style="margin-bottom:22px;">
            <div style="font-size:1.2em;color:#0077B6;font-weight:800;margin-bottom:4px;">📅 <span style="background:#E0F2FE;border-radius:8px;padding:2px 12px 2px 8px;">2020 – 2021</span></div>
            <div style="font-size:1.07em;font-weight:700;">🏢 Corporate Insight</div>
            <div style="color:#475569;">
            Worked at Oppo & Yazaki—learning operational scale, but always focused on bringing positive change to education.
            </div>
        </div>
        <div style="margin-bottom:22px;">
            <div style="font-size:1.2em;color:#F97316;font-weight:800;margin-bottom:4px;">📅 <span style="background:#FEF3C7;border-radius:8px;padding:2px 10px 2px 8px;">2021 – 2025</span></div>
            <div style="font-size:1.07em;font-weight:700;">🎓 Counseling & Leadership</div>
            <div style="color:#475569;">
            Guided 2,000+ students and families at Amity, Manipal, UNIVO, NMIMS, NIU.<br>
            Turned counseling into career architecture focused on transformation—not transactions.
            </div>
        </div>
        <div style="margin-bottom:22px;">
            <div style="font-size:1.2em;color:#10B981;font-weight:800;margin-bottom:4px;">📅 <span style="background:#D1FAE5;border-radius:8px;padding:2px 11px 2px 8px;">2024 – Present</span></div>
            <div style="font-size:1.07em;font-weight:700;">🚀 Distoversity Brand Launch</div>
            <div style="color:#475569;">
            Founded Distoversity—combining ground experience, tech (Python, Streamlit, AI), and holistic curriculum (HighScope USA).<br>
            Built India's first platform to empower every learner with science-driven, ethical, and personalized guidance. <br>
            <span style="font-weight:700;color:#0077B6;">The brand story: Not selling degrees. Architecting futures for India.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("💡 The Distoversity Hook")
        st.markdown("""
        - Empowerment from classrooms, boardrooms, and EdTech labs.<br>
        - India’s only platform built from real journeys and data—not hype.<br>
        - Founder story, sector impact, and brand promise in every line.
        """, unsafe_allow_html=True)
        st.success("🎓 Impact: 2,000+ students served | 35% improved career satisfaction.")
        st.markdown("""
        <div class="card" style="margin-top:14px;">
            <h4>Success Story: Riya</h4>
            <p>Riya struggled to match her skills to a degree. After our counseling, she’s thriving in a program that fits her natural energy and ambition.</p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: TFI Alignment ---
with tab2:
    st.header("Why Distoversity? The Brand Journey")
    st.markdown("""
    - Every child deserves world-class guidance—not just academic salesmanship.
    - My journey as teacher, counselor, and entrepreneur proved real impact is measured in lives transformed—not deals closed.
    - With AI & psychology, we help students discover their unique strengths, passions, and the right path.
    - Distoversity puts students first and builds India’s new mentorship movement—hope, credibility, and science.
    """)
    st.success("🌱 Let's build a brand that transforms India's education forever.")
    st.info("🤝 Ready to collaborate: [Connect on LinkedIn](https://www.linkedin.com)")

# --- TAB 3: FRAMEWORK ---
with tab3:
    st.header("We don't ask for Marks. We ask for Energy.")
    st.write("Distoversity philosophy: You cannot judge a fish by its ability to climb a tree.")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        energy = st.selectbox(
            "Select a Profile to Analyze:", 
            ["Creator", "Influencer", "Catalyst", "Analyst"]
        )
    with c2:
        if energy:
            st.markdown(f"**{energy}:** {PROFILE_DESCRIPTIONS[energy]}")
            if "Creator" == energy: st.success("🌟 Vision-driven. Loves freedom. Struggles with routine.")
            if "Influencer" == energy: st.warning("🔥 People-driven. Needs collaboration. Avoids isolation.")
            if "Catalyst" == energy: st.info("🤝 Results-driven. Needs structure, hates chaos.")
            if "Analyst" == energy: st.error("📊 Data-driven. Needs clarity, hates hype.")

# --- TAB 4: EDUVEER BOT/QUIZ ---
with tab4:
    st.title("🤖 Eduveer AI Demo")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.caption("Logic-based career counselor for every Indian student.")
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
        st.write("Universities matching your profile:")
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

# --- MOBILE PROMPT FOR TAB SWITCHING (Below ALL content) ---
st.markdown("""
<div style='margin-top:10px; text-align:center;'>
    <span style="font-size:1.12em; color:#0077B6;"><b>← Swipe or tap arrows to switch tabs</b></span>
</div>
""", unsafe_allow_html=True)

# --- FOOTER: PRIVACY & COPYRIGHT ---
st.markdown("""
<div class="footer-note">
<b>DISTOVERSITY | EMPOWERING INDIA 🇮🇳</b><br>
<b>Privacy Policy:</b> We do NOT collect, share, or sell your personal data. All information is confidential.<br>
<b>Copyright © 2025 Distoversity. All rights reserved.</b>
</div>
""", unsafe_allow_html=True)
