import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL, CLEAN CSS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
body, html, [data-testid="stAppViewContainer"], .stApp {
    font-family: "Inter", "Montserrat", Arial, sans-serif !important;
}
section[data-testid="stSidebar"] > div {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0;
    width: 320px !important;
    min-width: 320px !important;
    max-width: 99vw !important;
    box-sizing: border-box;
}
@media screen and (max-width: 600px) {
    section[data-testid="stSidebar"] > div {
        min-width: 97vw !important;
        width: 97vw !important;
    }
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

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h3 style='color:#0077B6;font-weight:800;'>DISTOVERSITY | EMPOWERING INDIA 🇮🇳</h3>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("Founder | EdTech Entrepreneur | Early Childhood & EdTech Leader")
    st.caption("📍 New Delhi, India")
    st.success("🎯 Mission: Replace 'Sales' in education with 'Science', Ethics, and Empowerment.")
    st.markdown("### 🚀 Key Skills & Domain Expertise")
    st.markdown("""
**Teaching & Educational Mentorship**  
• 10+ years ground teaching & empowerment  
• Pedagogy, curriculum development, mentorship  

**Data Analyst & EdTech Solutions**  
• Power BI, Python, Streamlit, franchise & student analytics  

**Domain Expertise: Franchise Expansion, Counseling**  
• Leadership for Footprints franchise growth (all India)  
• Admissions, student guidance (Subharti, Himalayan Garhwal, Noida International, Amity, Manipal, DY Patil, NMIMS)  
• Ed-Psychology | Team Leadership | Business Strategy
    """)
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

tab1, tab2, tab3, tab4 = st.tabs([
    "📖 My Story (The Journey)",
    "🛤️ Why Teach For India?",
    "🧠 The 4-Genius Framework",
    "🔎 Assessment Demo"
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
            <div style="font-size:1.14em;color:#0077B6;font-weight:800;margin-bottom:4px;">2020–2024</div>
            <div style="font-weight:700;">Across India’s Top Universities: Learning From 2,000+ Lives</div>
            <div style="color:#475569;">
            For four years, I was not just a counselor, but a listener and a guide for young people at  
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
            <div style="font-weight:700;">Distoversity and The Four-Dimensional Assessment</div>
            <div style="color:#475569;">
            Out of ten years of listening, teaching, counseling, and growing, I built <b>Distoversity</b>—not as a business,  
            but as a response to a broken market that sees young people as customers, not individuals.  
            My <b>4D Assessment</b> is not a test—it’s a curriculum to see a person’s full energy: intellect, emotion, action, vision.  
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
            <li>Built the 4D Assessment Model for ethical, dignified guidance—not sales scripts</li>
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
    st.title("🔎 Assessment Demo")
    st.markdown("<h3 style='color:#0077B6;'>EMPOWERING INDIA</h3>", unsafe_allow_html=True)
    st.caption("Distoversity's exclusive 4D Assessment: built on real teaching, counseling, and psychology—never just a sales script.")
    if st.session_state.step == 0:
        if st.button("Start Assessment ➔", type="primary"):
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
