import streamlit as st
import pandas as pd
import time
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Mohd Saad | Founder, Distoversity | Empowering India",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FORCE LIGHT THEME CSS (ENHANCED) ---
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
    .story-card {
        padding: 20px;
        border-left: 4px solid #0077B6;
        background: linear-gradient(135deg, #FFFFFF 0%, #F0F9FF 100%);
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .story-year {
        color: #0077B6 !important;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 8px;
    }
    .story-title {
        color: #003366 !important;
        font-size: 1.3rem;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .story-text {
        color: #334155 !important;
        line-height: 1.6;
        font-size: 1rem;
    }
    .stChatMessage[data-testid="user-message"] {
        background-color: #E0F2FE !important;
        color: #000000 !important;
    }
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #E2E8F0 !important;
    }
    button { color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; }
    a { color: #0077B6 !important; -webkit-text-fill-color: #0077B6 !important; }
    .footer-note { font-size:0.95rem; color:#475569 !important; text-align:center; margin-top:30px; padding:20px; border-top: 2px solid #E2E8F0; }
    .empowering-badge {
        background: linear-gradient(135deg, #0077B6 0%, #00B4D8 100%);
        color: white !important;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- UNIVERSITY & ASSESSMENT DATA ---
UNIVERSITIES = [
    {"name": "Amity Online", "programs": ["MBA", "MCA"], "fee": "₹1.75L", "badges": ["UGC", "NAAC A+"], "best_for": ["Analyst"], "high_pkg": "₹18 LPA"},
    {"name": "Manipal Jaipur", "programs": ["MBA", "BCA"], "fee": "₹1.50L", "badges": ["AICTE", "NAAC A+"], "best_for": ["Creator"], "high_pkg": "₹14 LPA"},
    {"name": "LPU Online", "programs": ["MBA", "BA"], "fee": "₹98k", "badges": ["UGC", "AICTE"], "best_for": ["Catalyst"], "high_pkg": "₹12 LPA"},
    {"name": "NMIMS Global", "programs": ["MBA (Executive)"], "fee": "₹4.0L", "badges": ["Top Ranked"], "best_for": ["Influencer"], "high_pkg": "₹24 LPA"}
]

QUESTIONS = [
    {"q": "When solving problems, you prefer:", "options": [("💡 Innovation & Creativity", "Creator"), ("🗣️ Discussion & Collaboration", "Influencer"), ("📊 Data & Analysis", "Analyst"), ("⚡ Quick Action & Results", "Catalyst")]},
    {"q": "Your ideal workspace would be:", "options": [("🎨 Creative Studio", "Creator"), ("📢 Collaborative Boardroom", "Influencer"), ("💻 Research Lab", "Analyst"), ("🏗️ Active Fieldwork", "Catalyst")]},
    {"q": "What truly motivates you?", "options": [("🚀 Creating Something New", "Creator"), ("🤝 Connecting with People", "Influencer"), ("🔍 Analyzing & Solving", "Analyst"), ("✅ Getting Things Done", "Catalyst")]}
]

PROFILE_DESCRIPTIONS = {
    "Creator": "**Innovative, visionary, and big-picture thinker.** You love launching new ideas and thinking outside the box. Best career fit: Product Designer, Brand Strategist, Innovation Manager, Entrepreneur.",
    "Influencer": "**Natural leader, communicator, and team energizer.** You inspire others and excel at building relationships. Best career fit: Public Relations, Human Resources, Client Relations, Media & Communications.",
    "Catalyst": "**Action-oriented, efficient, and results-driven.** You get things done and thrive in structured environments. Best career fit: Operations Manager, Logistics Coordinator, Project Manager, Execution Expert.",
    "Analyst": "**Precise, data-driven, and problem-solver.** You love diving deep into facts and solving complex puzzles. Best career fit: Financial Analyst, Data Scientist, Engineer, Research Specialist."
}

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state: st.session_state.messages = []
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
if "profile_result" not in st.session_state: st.session_state.profile_result = None

# --- SIDEBAR: PROFESSIONAL BIO ---
with st.sidebar:
    st.markdown("<div class='empowering-badge'>🇮🇳 EMPOWERING INDIA</div>", unsafe_allow_html=True)
    st.title("Mohd Saad")
    st.markdown("**Founder & EdTech Entrepreneur**")
    st.caption("📍 New Delhi, India")
    st.success("🎯 **Mission:** Replace 'Sales' in Education with 'Science'")
    
    st.markdown("### 🛠 Core Skills")
    st.code("✓ Python & Streamlit Development")
    st.code("✓ AI/LLM Integration & Agents")
    st.code("✓ Franchise Growth & Expansion")
    st.code("✓ Educational Psychology")
    
    st.markdown("### 💼 Experience")
    st.markdown("• **Distoversity** - Founder")
    st.markdown("• **Eduveer** - Creator")
    st.markdown("• **2000+ Students** Counseled")
    
    st.markdown("---")
    st.markdown("**🔒 Privacy Commitment:** Your data is 100% confidential. We never sell or share personal information.")
    st.markdown("**© 2025 Distoversity.** All rights reserved.")
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs([
    "📖 My Journey (Why I Built This)", 
    "🧠 The 4-Genius Framework", 
    "🤖 Eduveer AI (Live Demo)"
])

# --- TAB 1: STORY & JOURNEY ---
with tab1:
    st.header("From Factory Assembly Lines to Assembling Futures 🚀")
    st.markdown("##### *Why I left job security to transform India's education system*")
    st.markdown("<div class='empowering-badge'>🇮🇳 EMPOWERING INDIA</div>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.markdown("""
        <div class="story-card">
            <div class="story-year">2018 - 2020</div>
            <div class="story-title">🏭 Chapter 1: The Factory Floor Reality</div>
            <div class="story-text">
                My professional journey started at <b>Oppo Mobile & Yazaki</b>, working 12-hour shifts as a Line Engineer, assembling SMT circuit boards on manufacturing floors.<br><br>
                <b>The Awakening:</b> I witnessed millions of talented Indian youth with incredible grit but zero guidance. I felt trapped—assembling products when I could be building futures.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="story-card" style="border-left-color: #F97316;">
            <div class="story-year">2021 - 2024</div>
            <div class="story-title">📞 Chapter 2: The "Education Sales" Trap</div>
            <div class="story-text">
                I transitioned to education counseling at <b>Amity & Manipal</b>, personally guiding over <b>2,000+ students</b>. But I discovered a painful truth: education had become purely transactional, not transformational.<br><br>
                Students were treated as "leads." Counselors "closed deals" instead of opening doors to dreams. I knew there had to be a better way.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="story-card" style="border-left-color: #10B981;">
            <div class="story-year">2024 - Present</div>
            <div class="story-title">🚀 Chapter 3: Building Distoversity & Eduveer</div>
            <div class="story-text">
                I made a choice: to build something better. <b>Distoversity</b> combines <b>Educational Psychology (4-Genius Framework)</b> with <b>AI Technology</b>.<br><br>
                I don't sell degrees. <b>I architect futures.</b> Every student deserves guidance based on who they are, not what commission they generate.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.info("💡 **Why This Matters**")
        st.markdown("""
        **What I Bring:**
        - ⚙️ **Grit** of a factory worker  
        - ❤️ **Empathy** of a counselor  
        - 🚀 **Vision** of a founder  
        
        I combine **Operations + Technology + Heart** to create real impact in Indian education.
        
        **The Mission:** Help every Indian student discover their unique genius and find their perfect career path.
        """, unsafe_allow_html=True)
        
        st.success("**Ready to transform education in India!**")

# --- TAB 2: FRAMEWORK EXPLANATION ---
with tab2:
    st.header("🧠 The 4-Genius Framework: Career DNA, Not Just Marks")
    st.write("**Core Philosophy:** We don't judge students by marks alone. We discover their natural energy and potential.")
    st.markdown("<div class='empowering-badge'>🇮🇳 EMPOWERING INDIA</div>", unsafe_allow_html=True)
    st.info("💡 **Inspired by:** Educational Psychology + Multiple Intelligence Theory")
    
    st.divider()
    
    c1, c2 = st.columns(2)
    
    with c1:
        energy = st.selectbox(
            "🔍 Explore Each Career Profile:", 
            ["Creator", "Influencer", "Catalyst", "Analyst"]
        )
    
    with c2:
        if energy:
            st.markdown(f"### {energy} Profile")
            st.markdown(PROFILE_DESCRIPTIONS[energy])
            
            if energy == "Creator": 
                st.success("🌟 **Strengths:** Vision-driven, innovative, loves freedom.\n\n⚠️ **Watch Out:** May struggle with routine tasks and repetition.")
            elif energy == "Influencer": 
                st.warning("🔥 **Strengths:** People-driven, excellent communicator, team builder.\n\n⚠️ **Watch Out:** Needs collaboration, avoids isolation.")
            elif energy == "Catalyst": 
                st.info("⚡ **Strengths:** Results-driven, organized, thrives on structure.\n\n⚠️ **Watch Out:** Dislikes chaos and unclear expectations.")
            elif energy == "Analyst": 
                st.error("📊 **Strengths:** Data-driven, precise, loves solving complex problems.\n\n⚠️ **Watch Out:** Needs clarity, dislikes hype without facts.")
    
    st.divider()
    st.markdown("### 🎯 Why This Framework Works")
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Students Assessed", "2,000+")
    col_b.metric("Accuracy Rate", "94%")
    col_c.metric("Career Clarity", "10x Better")

# --- TAB 3: INTERACTIVE AI DEMO ---
with tab3:
    st.title("🤖 Eduveer AI: Your Personal Career Guide")
    st.markdown("<div class='empowering-badge'>🇮🇳 EMPOWERING INDIA</div>", unsafe_allow_html=True)
    st.caption("✨ Logic-based AI career counselor designed for every Indian student")

    if st.session_state.step == 0:
        st.markdown("### 🎯 Discover Your Career DNA in 3
