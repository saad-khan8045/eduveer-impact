import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL STYLE ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
html, body, [data-testid="stAppViewContainer"], .stApp, .main {
    background-color: #F4F9FD !important;
    color: #0F172A !important;
    font-family: "Inter", "Montserrat", Arial, sans-serif !important;
    font-size: 1.01em;
}
h1, h2, h3, h4, h5 {
    font-family: "Montserrat", Arial, sans-serif !important;
    color: #19376D !important;
    font-weight: 700;
}
section[data-testid="stSidebar"] > div {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
    border-right: 1px solid #E2E8F0;
    width: 310px !important;
    min-width: 290px !important;
    max-width: 99vw !important;
    padding-right: 10px !important;
    box-sizing: border-box;
}
.stMarkdown, div, p, label { font-family: "Inter", Arial, sans-serif !important; }
input, textarea, select, div[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #000 !important;
    border: 1px solid #CBD5E1 !important;
}
.stButton>button {
    color: #fff !important;
    background: #0077B6 !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
}
.motivate-cta {
    background: linear-gradient(100deg, #e0f2fe 70%, #bbf7d0 100%);
    border: 1.5px solid #bae6fd;
    border-radius: 8px;
    padding: 15px 14px;
    margin: 20px 0 10px 0;
    font-size: 1.09em;
    color: #134e4a;
    text-align: left;
    box-shadow: 0 2px 16px #c7f9f8;
    font-weight: 500;
}
@media screen and (max-width: 600px) {
    html, body, [data-testid="stAppViewContainer"], .stApp, .main {
        font-size: 1.05em;
    }
    section[data-testid="stSidebar"] > div {
        min-width: 97vw !important;
        width: 97vw !important;
        font-size: 1.01em;
        padding-right: 2vw !important;
    }
    .footer-note { font-size:0.94em !important; }
    .motivate-cta { font-size: 1em; }
}
.footer-note {
    font-size:0.93em; color:#758fa0 !important; text-align:center; margin-top:18px;
    font-family:"Montserrat",Arial,sans-serif !important;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

# --- DATA ---
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
    st.markdown("<h3 style='color:#0077B6;font-weight:800;margin-bottom:3px;'>DISTOVERSITY | EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | EdTech Entrepreneur | Early Childhood & EdTech Leader")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science', Ethics, and Empowerment.")

    st.markdown("""
<b style='display:block;font-family:Montserrat,sans-serif;color:#19376D;font-size:1.06em;margin-top:8px;margin-bottom:2px;'>Teaching & Educational Mentorship</b>
<div style='font-family:Inter,sans-serif;font-size:1em;font-weight:500;line-height:1.5em;margin-bottom:10px;'>
    • 10+ years ground teaching & empowerment<br>
    • Pedagogy, curriculum development, mentorship
</div>
<b style='display:block;font-family:Montserrat,sans-serif;font-size:1.16em;color:#0d2e42;background:linear-gradient(90deg,#d8f5f7 85%,#f6f6f9 100%);padding:7px 10px 6px 10px;border-radius:7px;border-left: 5px solid #0077B6;margin-top:2px;margin-bottom:8px;'>Domain Expertise</b>
<div style='font-family:Inter,sans-serif;font-size:1em;font-weight:500;line-height:1.62;margin-left:2px;'>
    • Leadership for Footprints franchise growth (all India)<br>
    • 2,000+ students personally counseled/advised<br>
    • Admissions, student guidance (Subharti, Himalayan Garhwal, Noida International, Amity, Manipal, DY Patil, NMIMS)<br>
    • Power BI, Python, Streamlit analytics for student & franchise insights<br>
    • Deep child psychology understanding (Footprints Early Ed)<br>
    • Team Leadership | Ed-Psychology | Business Strategy
</div>
<div style='font-family:Inter,sans-serif;font-size:1em;margin-top:8px;'>
    <b>Our counselling is <span style='color:#008066;'>data-driven</span>, powered by 4D Assessment .<br>
    <span style='color:#0077B6;'>Cost: ₹999/session.</span></b>
</div>
""", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="motivate-cta">
        🌟 <b>Ready to discover your energy and direction?</b><br>
        Let's move beyond confusion and guesswork.
        <b>Book a 4D Assessment —let’s plan your next step, together.</b><br>
        <span style="color:#1a7272;">No more random calls. Real futures, real results.<br>
        <b>Sign up for your session now for just ₹999!</b></span>
        <br>
        <a href='mailto:saad01489@gmail.com?subject=Book%20my%204D%204D Assessment %20Session' target="_blank"><button style='margin-top:6px; background: #059669; color: #fff; border:none; border-radius:5px; padding:7px 18px; font-size:1em; font-weight:600;'>Book My Session</button></a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("<b>Privacy Policy:</b> Your data is always safe and confidential.", unsafe_allow_html=True)
    st.markdown("Copyright © 2025 Distoversity. All rights reserved.", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")
    st.markdown("---")
    st.markdown("## Try Our Career Guidance Platform")
    st.markdown(
        "<a href='https://distoversity-mvp-j4pmyhqdjr7v7ukpgwmyx6.streamlit.app/' target='_blank'>👉 Distoversity Career Platform</a>",
        unsafe_allow_html=True
    )

# --- MAIN TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 My Story (The Journey)",
    "🛤️ Why Teach For India?",
    "🧠 The 4-Genius Framework",
    "🔎 4D Assessment  Demo"
])

with tab1:
    st.header("From Classroom to Changemaker: The Distoversity Journey 🚀")
    st.markdown("##### Built on real ground work with 2,000+ students and India's leading universities.")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <div style="margin-bottom:28px;">
            <div style="font-size:1.14em;color:#0077B6;font-weight:800;margin-bottom:4px;">2015–2019</div>
            <div style="font-weight:700;">My Journey Begins: Teaching as Service</div>
            <div style="color:#475569;">
            I began on the frontline of Indian education—teaching in real classrooms, connecting with students not only as learners but as dreamers, sons, daughters.  
            It was here I saw the gaps: children craving guidance, not just grades—kids battling doubts, pressure, and a system that rarely stopped to see who they truly were.  
            Every day, I witnessed their struggles, their breakthroughs, and learned that education is first about humanity and trust.  
            </div>
        </div>

        <div style="margin-bottom:28px;">
            <div style="font-size:1.14em;color:#0077B6;font-weight:800;margin-bottom:4px;">2019–2024</div>
            <div style="font-weight:700;">Across India’s Top Universities: Learning From 2,000+ Lives</div>
            <div style="color:#475569;">
            For five years, I was not just a counselor, but a listener and a guide for young people at  
            <b>Subharti, Himalayan Garhwal, Noida International University, Amity, Manipal, DY Patil, NMIMS</b> and more.  
            Every face, every story was different—families coming with hope, confusion, fears about the future.  
            I didn’t just match students to programs; I helped parents rediscover pride, I helped students make real-life choices.  
            What I learned: every admission is more than a CRM lead—each is a story, a struggle, a chance to change a life.  
            2,000+ students counseled, each leaving me wiser, more humble, more determined to fix what’s broken.
            </div>
        </div>

        <div style="margin-bottom:28px;">
            <div style="font-size:1.14em;color:#10B981;font-weight:800;margin-bottom:4px;">2024–Present</div>
            <div style="font-weight:700;">Footprints Day Care: Franchise, Childhood, Psychology</div>
            <div style="color:#475569;">
            I led franchise growth for Footprints Day Care—traveling across India, I saw how little ones learn, how mothers and fathers dream for their children,  
            and how school isn’t just an academic ritual: it’s a world of emotional intelligence, personality, mindset.  
            For me, <b>child psychology</b> became the backbone—understanding what makes learning joyful, what damages a child’s will to grow.  
            I worked with teams and parents to make every franchise not a business, but a safe space, a launching pad for real destiny.
            </div>
        </div>

        <div style="margin-bottom:28px;">
            <div style="font-size:1.13em;color:#F97316;font-weight:800;margin-bottom:4px;">2024–Present</div>
            <div style="font-weight:700;">Distoversity and The Four-Dimensional 4D Assessment </div>
            <div style="color:#475569;">
            Out of ten years of listening, teaching, counseling, and growing, I built <b>Distoversity</b>—not as a business,  
            but as a response to a broken market that sees young people as customers, not individuals.  
            My <b> 4D Assessment </b> is not a test—it’s a curriculum to see a person’s full energy: intellect, emotion, action, vision.  
            It’s different because it refuses to let “call centers” and “sales scripts” decide someone’s future.  
            It’s my commitment that every conversation, every counseling session, is based on dignity, empathy, and the will to make every child not just successful in exams,  
            but fulfilled in life.  
            This is my story, and these are the lessons I pass to every student and every family who trusts Distoversity.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="margin-bottom:18px;">
        <span style="font-size:1.07em;color:#256981;font-weight:700;">Impact Snapshots</span>
        <ul style="color:#48514F; font-size:1em;">
            <li>2,000+ students individually counseled, every life a different challenge</li>
            <li>Worked directly with: Subharti, Himalayan Garhwal, NIU, Amity, Manipal, DY Patil, NMIMS and more</li>
            <li>Led pan-India franchise expansion for Footprints Day Care</li>
            <li>Expert in child psychology and real parent empowerment</li>
            <li>Built the 4D Assessment  Model for ethical, dignified guidance—not sales scripts</li>
        </ul>
        <div style="margin-top:14px; color:#207150"><b>Success Story: Riya</b><br>
        Riya found a future mapped to her natural strengths, thanks to Distoversity support—not just selling a generic degree.
        </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("Why Distoversity? Why Teach For India?")
    st.markdown("""
    - Every learner deserves ethical, person-first guidance—not just admissions salesmanship or CRM-driven calls.
    - Real impact = lives transformed (not just enrolled).
    - Blending data, psychology, and ground wisdom for every unique story.
    - India's next mentorship movement—trust, credibility, and real student energy.
    """)
    st.success("🌱 Together, let's build India's next empowered generation.")
    st.info("🤝 Ready to collaborate: [Connect on LinkedIn](https://linkedin.com)")

with tab3:
    st.header("We don't ask for Marks. We ask for Energy.")
    st.write("Distoversity believes real guidance measures your energy, not just academic ability or exam marks.")
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
    st.title("🔎 4D Assessment  Demo")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.caption("Distoversity's exclusive 4D Assessment : built on real teaching, counseling, and psychology—never just a sales script.")
    st.markdown("""
    <div class="motivate-cta">
    🌟 <b>Ready to discover your energy and direction?</b><br>
    Let's move beyond confusion and guesswork.<br>
    <b>Our counselling is data-driven. Every session is powered by 4D Assessment .<br>
    Cost: ₹999/session.</b><br><br>
    <a href='mailto:saad01489@gmail.com?subject=Book%20my%204D%204D Assessment %20Session' target="_blank"><button style='margin-top:5px; background: #059669; color: #fff; border:none; border-radius:5px; padding:9px 20px; font-size:1.09em; font-weight:700;'>Book My Session Now</button></a>
    <br>
    <span style="color:#187180;"><b>No more random sales calls. Real futures guided, not guessed.</b></span>
    </div>
    """, unsafe_allow_html=True)
    if st.session_state.step == 0:
        if st.button("Start 4D Assessment  ➔", type="primary"):
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
        st.markdown(f"""
        <div style="background:linear-gradient(95deg,#e0f2fe 70%,#d3fbe6 100%);
                 border:1.7px solid #bae6fd;
                 border-radius:15px;
                 box-shadow:0 2px 18px #c1f7fc33;
                 padding:26px 22px 18px 22px;
                 margin-bottom:18px;">
            <h2 style="margin-bottom:13px;font-family:Montserrat;color:#18906d;font-size:2.08em;">
                🎉  You are a <span style='color:#156cb7'>{primary}</span>!
            </h2>
            <div style="font-size:1.20em;font-weight:600;margin-bottom:9px;">
                {PROFILE_DESCRIPTIONS[primary]}
            </div>
            <div style="font-size:1.07em;margin-bottom:12px;color:#008066;">
                Top Career Directions: <b>
                {"Product Design, Brand, Strategy" if primary=="Creator" else
                 "PR, HR, Communication, Media" if primary=="Influencer" else
                 "Ops, Projects, Startups" if primary=="Catalyst" else
                 "Finance, Data Science, Engineering"}
                 </b>
            </div>
            <div style="margin:13px 0 2px 0;background:#f8fdff;border-radius:9px;padding:15px;">
            <b style="color:#065f46;">Universities that fit your genius:</b>
        """, unsafe_allow_html=True)
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:10px 7px 6px 7px; border:1.1px solid #bce3fc; border-radius:9px; margin-bottom:10px; background:#f8fdfe;">
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
DISTOVERSITY | EMPOWERING INDIA 🇮🇳<br>
Privacy Policy: We do NOT collect, share, or sell your personal data. All information is confidential.<br>
Copyright © 2025 Distoversity. All rights reserved.
</div>
""", unsafe_allow_html=True)
