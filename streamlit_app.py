import streamlit as st

# === PAGE CONFIGURATION ===
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === UNIVERSAL UI FONTS & COLORS ===
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
html, body, [data-testid="stAppViewContainer"], .stApp, .main {
    background-color: #f4fafe !important;
    color: #142636 !important;
    font-family: "Inter", Arial, sans-serif !important;
}
h1, h2, h3, h4, h5 {
    font-family: "Montserrat", Arial, sans-serif !important;
    color: #0a3863 !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}
section[data-testid="stSidebar"] > div {
    background: linear-gradient(113deg,#fcfcfe 80%,#e0f7fa 100%) !important;
    color: #142636 !important;
    border-right: 2px solid #C8E6F4;
    width: 320px !important;
    min-width: 285px !important;
    max-width: 99vw !important;
    padding: 0 14px 0 6px !important;
    border-radius: 0 0 27px 0 !important;
    box-shadow:0 2px 28px #a9e0fa19;
}
.stButton>button {
    color: #fff !important;
    background: linear-gradient(98deg,#0077b6 63%,#25c7a6 100%) !important;
    border-radius: 22px !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 14px #3fd7d855;
    padding:0.68em 1.85em;
    font-size:1.09em;
    border:none;
}
.motivate-cta {
    background: linear-gradient(100deg,#e0f2fd 67%,#d2fde9 100%);
    border: 1.9px solid #bae6fd;
    border-radius: 13px;
    padding: 14px 14px 11px 19px;
    margin: 21px 0 11px 0;
    font-size: 1.13em;
    color: #125361;
    box-shadow: 0 2px 20px #e3fcfd31;
    font-family: Inter,sans-serif;
    font-weight: 560;
    letter-spacing:0.01em;
}
.footer-note {
    font-size:0.98em; color:#758fa0 !important; text-align:center; margin-top:23px;
    font-family:"Montserrat",Arial,sans-serif !important;
    margin-bottom:10px;
}
@media screen and (max-width: 630px) {
    .stTabs { font-size:1.11em !important;}
    section[data-testid="stSidebar"] > div { min-width: 98vw !important; width:98vw!important; font-size:1.04em;}
}
</style>
""", unsafe_allow_html=True)

# === DATA ---
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
CAREER_HOOKS = {
    "Creator": "• Product Design, Brand, Strategy, Growth roles",
    "Influencer": "• PR, HR, Public Roles, Client Relations, Communication",
    "Catalyst": "• Operations, Execution, Projects, Startups",
    "Analyst": "• Data, Finance, Tech Analysis, Engineering"
}

# === SESSION ===
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}

# === SIDEBAR ===
with st.sidebar:
    st.markdown("""<span style="font-family:Montserrat;font-size:2em;font-weight:900;color:#0077B6;">
        DISTOVERSITY</span> <span style='font-size:1em;'>| Empowering India 🇮🇳</span>""", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("<span style='font-family:Montserrat;font-size:1.13em;color:#15a78b;font-weight:660;'>Your Career Success Partner</span>",unsafe_allow_html=True)
    st.markdown("Founder | EdTech Entrepreneur<br>Early Childhood & EdTech Leader", unsafe_allow_html=True)
    st.caption("📍 New Delhi, India")
    st.markdown("""
<b style='font-family:Montserrat,sans-serif;font-size:1.09em;background:linear-gradient(90deg,#e0f2fe 90%,#fff 100%);padding:7px 12px 7px 12px;border-radius:10px;color:#097b91;letter-spacing:-0.01em;display:block;'>🚀 Teaching & Educational Mentorship</b>
<div style='font-family:Inter,sans-serif;font-size:1em;font-weight:500;line-height:1.5;margin-bottom:10px;margin-left:3px;'>
    • 10+ years ground teaching & empowerment<br>
    • Pedagogy, curriculum development, mentorship
</div>
<b style='display:block;font-family:Montserrat,sans-serif;font-size:1.17em;color:#19376D;background:linear-gradient(90deg,#d8f5f7 75%,#f6fafe 100%);padding:8px 12px 7px 10px;border-radius:8px;border-left: 6px solid #0077B6;margin-top:3px;margin-bottom:8px;'>💼 Domain Expertise</b>
<div style='font-family:Inter,sans-serif;font-size:1em;font-weight:560;line-height:1.65;margin-left:2px;'>
    • Leadership for Footprints franchise growth (all India)<br>
    • 2,000+ students personally counseled/advised<br>
    • Admissions, student guidance (Subharti, Himalayan Garhwal, Noida International, Amity, Manipal, DY Patil, NMIMS)<br>
    • Power BI, Python, Streamlit analytics for student & franchise insights<br>
    • Deep child psychology understanding (Footprints Early Ed)<br>
    • Team Leadership | Ed-Psychology | Business Strategy
</div>
<div style='font-family:Inter,sans-serif;font-size:0.99em;margin:12px 0;'>
    <b>Our counselling is <span style='color:#008066;'>data-driven</span>, powered by assessment.<br>
    <span style='color:#0077B6;'>Cost: ₹999/session.</span></b>
</div>
""", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="motivate-cta">
        <span style='font-size:1.12em;font-weight:700;color:#1560a8;'>🌟 Ready to discover your energy and direction?</span><br>
        Let's move beyond guesswork.<br>
        <b>Book a 4D Assessment—let’s plan your future together.</b><br>
        <span style="color:#0a8773;"><b>No more random calls. Real futures, real results.<br>Sign up today for just ₹999!</b></span>
        <br>
        <a href='mailto:saad01489@gmail.com?subject=Book%204D%20Assessment%20Session' target="_blank"><button style='margin-top:7px; background: #059669; color: #fff; border:none; border-radius:6px;padding:10px 26px; font-size:1.09em; font-weight:670;box-shadow:0 2px 9px #6ec2b82c;'>Book My Session</button></a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("<b>🔒 Privacy: Your data is always safe and confidential.</b>", unsafe_allow_html=True)
    st.markdown("Copyright © 2025 Distoversity. All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")
    st.markdown("---")
    st.markdown("## Try Our Career Guidance Platform")
    st.markdown(
        "<a href='https://distoversity-mvp-j4pmyhqdjr7v7ukpgwmyx6.streamlit.app/' target='_blank'>👉 Distoversity Career Platform</a>",
        unsafe_allow_html=True
    )

# === TABS ===
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 My Story (The Journey)",
    "🛤️ Why Teach For India?",
    "🧠 The 4-Genius Framework",
    "🔎 Assessment Demo"
])

with tab1:
    st.header("From Classroom to Changemaker: The Distoversity Journey 🚀")
    st.markdown("##### Built on real ground work with 2,000+ students and India's leading universities.")
    st.markdown("<h3 style='color:#009688;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div style="margin-bottom:28px;">
            <div style="font-size:1.15em;color:#0FA0E6;font-weight:800;margin-bottom:2px;">2015–2019</div>
            <div style="font-weight:700;">The Start: Teaching for Heart</div>
            <div style="color:#2b5182;">Real lessons, real struggles, building trust and courage in every class.</div>
        </div>
        <div style="margin-bottom:28px;">
            <div style="font-size:1.15em;color:#0FA0E6;font-weight:800;margin-bottom:2px;">2020–2024</div>
            <div style="font-weight:700;">Scaling Up: Top Universities, Deep Impact</div>
            <div style="color:#2b5182;">Hundreds of stories, a mission beyond numbers—family, empathy, truth.</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="margin-bottom:17px;">
        <span style="font-size:1.09em;color:#1376d4;font-weight:700;">Impact Snapshots</span>
        <ul style="color:#48514F; font-size:1.06em;">
            <li>2,000+ students counseled—every life, a new victory</li>
            <li>Franchise leadership for India’s best early education brand</li>
            <li>4D Model: Guidance for dignity, not sales</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("Why Distoversity? Why Teach For India?")
    st.markdown("""
- Every learner deserves ethical, person-first guidance—not just sales calls.
- Real impact = lives transformed (not just enrolled).
- Data, psychology, and ground: India's next mentorship movement.
""")
    st.markdown("""
    <div class="motivate-cta" style="margin-top:16px;">
      🌱 Dream big for India's future. <b>Join the journey!</b> <br>
      <a href="https://linkedin.com">🤝 Connect on LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("The 4-Genius Framework")
    st.write("You can't judge a fish by its ability to climb a tree. We measure energy, not marks.")
    c1, c2 = st.columns(2)
    with c1:
        energy = st.selectbox("Select a Profile to Analyze:", ["Creator", "Influencer", "Catalyst", "Analyst"])
    with c2:
        if energy:
            st.markdown(f"<span style='font-family:Montserrat;font-size:1.10em;font-weight:700;color:#0fa0e6;'>🔍 {energy}</span>: {PROFILE_DESCRIPTIONS[energy]}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#197b6d;'>{CAREER_HOOKS[energy]}</span>", unsafe_allow_html=True)

with tab4:
    st.title("🔎 Assessment Demo")
    st.markdown("<h3 style='color:#009688;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.caption("Distoversity 4D Assessment: Real strengths. No scripts. Pure mentoring.")

    if st.session_state.step == 0:
        st.markdown("""
        <div class="motivate-cta">
        <b>Test your potential—get instant, data-driven insights in just 3 questions.</b>
        </div>
        """,unsafe_allow_html=True)
        if st.button("Start Assessment ➔", type="primary"):
            st.session_state.step = 1
            st.rerun()
    elif st.session_state.step == 1:
        curr = QUESTIONS[st.session_state.q_index]
        st.markdown(f"<b style='font-family:Montserrat;color:#17425d;font-size:1.18em;'>Q{st.session_state.q_index + 1}:</b> {curr['q']}", unsafe_allow_html=True)
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
        st.markdown(f"""
        <div style="background:linear-gradient(92deg,#e0f2fe 75%,#c9f9e9 100%);
        border:2px solid #bae6fd;border-radius:15px;padding:25px 17px;margin-bottom:15px;
        box-shadow: 0 3px 20px #b6e4fa40;">
            <h2 style="margin-bottom:10px;margin-top:0.7em;font-family:Montserrat;font-size:2em;letter-spacing:-2px;color:#199582;">🎉 {primary.upper()}!</h2>
            <div style="font-size:1.23em;font-weight:600;margin-bottom:8px;">
                {PROFILE_DESCRIPTIONS[primary]}
            </div>
            <div style="font-size:1.1em;margin:13px 0 7px 0;">
                <span style="color:#0077B6;font-weight:720;">
                Top Career Directions:
                </span> <span style="color:#166c6c;">{CAREER_HOOKS[primary]}</span>
            </div>
            <div style="margin:9px 0 3px 0;background:#f8fdff;border-radius:8px;padding:15px;">
                <b style="color:#065f46;">Universities that fit your genius:</b>
        """, unsafe_allow_html=True)
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:10px 7px 6px 7px; border:1.4px solid #bbe7fc; border-radius:9px; margin-bottom:10px; background:#f8fdfe;">
                <h4 style="font-family:Montserrat,sans-serif;font-weight:700;color:#1363a8;margin-bottom:4px;margin-top:8px;">{u['name']}</h4>
                <div style='font-size:1.01em;color:#527684;'><b>Programs:</b> {', '.join(u['programs'])}
                 | <b>Fee:</b> {u['fee']} | <b>Highest Pkg:</b> {u['high_pkg']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)
        if st.button("Restart Demo"):
            st.session_state.step = 0
            st.session_state.q_index = 0
            st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
            st.rerun()

st.markdown("""
<div class="footer-note">
<b>DISTOVERSITY | EMPOWERING INDIA 🇮🇳</b><br>
Privacy Policy: We do NOT collect, share, or sell your personal data. All information is confidential.<br>
Copyright © 2025 Distoversity. All rights reserved.
</div>
""", unsafe_allow_html=True)
