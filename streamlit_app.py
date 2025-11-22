import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FORCE LIGHT THEME CSS ---
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
    .footer-note { font-size:0.9rem; color:#475569 !important; text-align:center; margin-top:20px; }
    @media screen and (max-width: 700px) {
        body, html, .stApp { font-size: 1.08em; }
        section[data-testid="stSidebar"] > div { min-width:98vw !important; width:98vw !important; }
    }
    </style>
""", unsafe_allow_html=True)

# --- DATA FOR DEMO ASSESSMENT ---
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
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}

# --- SIDEBAR --- 
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;'>DISTOVERSITY | EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | Ed-Tech Intrapreneur | Early Childhood & EdTech Leader")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science', Ethics, and Empowerment.")
    st.markdown("**🚀 Key Skills & Domain Expertise**")
    st.markdown("""
- **Teaching & Educational Mentorship**  
    • 10+ years ground teaching & empowerment  
    • Pedagogy, curriculum development, mentorship  
- **Domain Expertise**  
    • Leadership for Footprints franchise growth (all India)  
    • 2,000+ students personally counseled/advised  
    • Admissions, student guidance (Subharti, Himalayan Garhwal, Noida International, Amity, Manipal, DY Patil, NMIMS)  
    • Power BI, Python, Streamlit analytics  
    • Deep child psychology understanding (Footprints Early Ed)  
    • Team Leadership | Ed-Psychology | Business Strategy  
**Our counselling is _data-driven_, powered by assessment. _Cost: ₹999/session._**
    """)
    st.markdown("""
<div style="background:linear-gradient(110deg,#e0f2fe,#c5fdd6);border-radius:12px;padding:16px 12px 10px 13px; border:1.5px solid #bae6fd;box-shadow:0 3px 18px #c6f9f866;">
<b>🌟 Ready to discover your energy and direction?</b><br>
Let's move beyond confusion and guesswork.<br>
<b>Book a 4D Assessment—let’s plan your next step together.</b><br>
<span style='color:#1f5d58;font-size:1em;'>No more random calls. Real futures, real results.<br>
Sign up for your session now for just <b>₹999!</b></span><br><br>
<a href='mailto:saad01489@gmail.com?subject=Book%20my%204D%20Assessment%20Session' target="_blank">
<button style='background: #059669;color:#fff;border:none;border-radius:5px;padding:7px 23px;font-size:1.06em;font-weight:700;cursor:pointer;'>Book My Session</button>
</a>
<span style='background:#e7f7e7;color:#308045;border-radius:7px;font-size:0.88em;font-weight:600;display:inline-block;padding:3px 9px;margin-top:8px;'>Proud Alison Community Member</span>
</div>
""", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Inter,sans-serif;font-size:1em;margin-bottom:5px;color:#126064;'>🔒 <b>We are NOT selling your data</b>. Your privacy is 100% protected.</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Inter,sans-serif;color:#516984;font-size:0.97em;margin-bottom:2px;'>Copyright © 2025 Distoversity. All rights reserved.</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Inter,sans-serif;font-size:0.96em;'><a href='https://linkedin.com' target='_blank'>LinkedIn</a> | <a href='mailto:saad01489@gmail.com'>Email</a></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("## Go to Career Guidance Platform")
    st.markdown("[👉 Distoversity AI Career Platform](https://distoversity-mvp-j4pmyhqdjr7v7ukpgwmyx6.streamlit.app/)", unsafe_allow_html=True)

# --- MAIN TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "My Story (The Journey)",
    "Why Teach For India?",
    "The 4-Genius Framework",
    "Assessment Demo"
])

with tab1:
    st.header("From Classroom to Changemaker: Building the Distoversity Brand")
    st.markdown("##### *Why a decade on the ground led to India's most trusted career guidance platform*")
    st.divider()
    st.markdown("""
**2015 – 2019**: Classroom Roots  
Started as a teacher, discovering Indian students' real needs and dreams.  
True education is mentorship, courage, and growth—not just marks.

**2020 – 2021**: Corporate Insight  
Learned operational scale at Oppo & Yazaki—always focused on positive change in education.

**2021 – 2025**: Counseling & Leadership  
Guided 2,000+ students and families at Amity, Manipal, UNIVO, NMIMS, NIU.  
Turned counseling into career architecture focused on transformation—not transactions.

**2024 – Present**: Distoversity Brand Launch  
Founded Distoversity—combining ground experience, tech (Python, Streamlit, AI), and holistic curriculum (HighScope USA).  
Built India's first platform to empower every learner with science-driven, ethical, and personalized guidance.  
The brand: Not selling degrees. Architecting futures for India.
""")

with tab2:
    st.header("Why Distoversity? The Brand Journey")
    st.markdown("""
- Every child deserves world-class guidance—not just academic salesmanship.
- My journey as teacher, counselor, and entrepreneur proved real impact is measured in lives transformed—not deals closed.
- With AI & psychology, we help students discover their unique strengths, passions, and the right path.
- Distoversity puts students first and builds India’s new mentorship movement—hope, credibility, and science.
""")

with tab3:
    st.header("The 4-Genius Framework")
    st.write("Distoversity philosophy: You cannot judge a fish by its ability to climb a tree.")
    st.markdown("""
- **Creator:** Launch, design, innovate  
- **Influencer:** Communicate, motivate  
- **Catalyst:** Action, results  
- **Analyst:** Data, structure, clarity  
""")

with tab4:
    st.title("Assessment Demo")
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
        st.success(f"Result: You are a {primary}!")
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

# --- FOOTER ---
st.markdown("""
<div class="footer-note">
<b>DISTOVERSITY | EMPOWERING INDIA</b><br>
<b>Privacy Policy:</b> We do NOT collect, share, or sell your personal data. All information is confidential.<br>
<b>Copyright © 2025 Distoversity. All rights reserved.</b>
</div>
""", unsafe_allow_html=True)
