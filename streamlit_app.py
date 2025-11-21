import streamlit as st
import pandas as pd
import time
import random
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Mohd Saad | Distoversity",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- FORCE LIGHT THEME CSS (NUCLEAR OPTION) ---
st.markdown("""
    <style>
    /* 1. FORCE WHITE BACKGROUND ON EVERYTHING */
    [data-testid="stAppViewContainer"], .stApp, header, footer {
        background-color: #F4F9FD !important;
        color: #0F172A !important;
    }
    
    /* 2. FORCE SIDEBAR WHITE */
    section[data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
    }

    /* 3. FIX TEXT COLORS (Force Dark Blue/Black) */
    h1, h2, h3, h4, h5, h6, p, span, div, label, li {
        color: #0F172A !important;
        -webkit-text-fill-color: #0F172A !important; /* Webkit fix for Samsung */
    }
    
    /* Specific Headers Color */
    h1, h2, h3 {
        color: #003366 !important;
        -webkit-text-fill-color: #003366 !important;
    }

    /* 4. FIX INPUT BOXES (Samsung often makes these black) */
    input, textarea, select, div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #CBD5E1 !important;
    }
    
    /* 5. FIX CARDS & CONTAINERS */
    .d-card, .story-card, div[data-testid="stExpander"], .stMarkdown {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }

    /* 6. FIX CHAT MESSAGES */
    /* User Message Bubble */
    .stChatMessage[data-testid="user-message"] {
        background-color: #E0F2FE !important;
        color: #000000 !important;
    }
    /* Assistant Message Bubble */
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* 7. BUTTONS */
    button {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }
    
    /* 8. FIX LINKS */
    a {
        color: #0077B6 !important;
        -webkit-text-fill-color: #0077B6 !important;
    }
    </style>
    """, unsafe_allow_html=True)    

# --- 3. EDUVEER BOT DATA ---
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

# --- 4. SESSION STATE ---
if "messages" not in st.session_state: st.session_state.messages = []
if "step" not in st.session_state: st.session_state.step = 0
if "q_index" not in st.session_state: st.session_state.q_index = 0
if "scores" not in st.session_state: st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}

# --- 5. SIDEBAR (THE PERSON) ---
with st.sidebar:
    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", width=160)
    
    st.title("Mohd Saad")
    st.markdown("**Founder | Ed-Tech Intrapreneur**")
    st.caption("📍 New Delhi, India")
    
    st.markdown("---")
    st.success("🎯 **Mission:** To replace 'Sales' in education with 'Science'.")
    
    st.markdown("### 🛠 Skills")
    st.code("Python & Streamlit")
    st.code("LLM & AI Agents")
    st.code("Franchise Expansion")
    st.code("Ed-Psychology")

    st.markdown("---")
    st.markdown("[LinkedIn](https://linkedin.com) | [Email](mailto:saad01489@gmail.com)")

# --- 6. MAIN TABS ---
tab1, tab2, tab3 = st.tabs(["📖 My Story (The Hook)", "🧠 The 4-Genius Framework", "🤖 Eduveer AI (Live Demo)"])

# --- TAB 1: THE STORY (THE HOOK) ---
with tab1:
    st.header("From Assembly Lines to Assembling Futures 🚀")
    st.markdown("##### *Why I quit a stable job to fix the Education System.*")
    st.divider()

    col1, col2 = st.columns([2, 1])
    with col1:
        # STORY CARD 1: THE FACTORY
        st.markdown("""
        <div class="story-card">
            <div class="story-year">2018 - 2020</div>
            <div class="story-title">🏭 The Factory Floor Reality</div>
            <div class="story-text">
                My journey didn't start in a fancy office. It started at <b>Oppo Mobile & Yazaki</b>. 
                I worked 12-hour shifts as a Line Engineer, assembling SMT boards. 
                <br><br>
                <b>The Lesson:</b> I learned that India has millions of hardworking youth who are treated like machines. 
                They have the grit, but they lack the <i>Guidance</i>. I felt trapped, assembling products instead of building lives.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # STORY CARD 2: THE CONFLICT
        st.markdown("""
        <div class="story-card" style="border-left-color: #F97316;">
            <div class="story-year">2021 - 2024</div>
            <div class="story-title">📞 The "Sales" Trap</div>
            <div class="story-text">
                I moved to Education Counseling (Amity/Manipal). I spoke to <b>2,000+ students</b>.
                But I faced a hard truth: <b>Education had become a transaction.</b>
                <br><br>
                Counselors were pushed to "close deals" and sell degrees. Students were just "Leads".
                I realized: <i>"We are selling maps to people who don't even know where they want to go."</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # STORY CARD 3: THE SOLUTION
        st.markdown("""
        <div class="story-card" style="border-left-color: #10B981;">
            <div class="story-year">2024 - Present</div>
            <div class="story-title">🚀 Distoversity & Eduveer</div>
            <div class="story-text">
                I decided to stop complaining and start building. 
                I founded <b>Distoversity</b> to bring Ethics back into counseling.
                <br><br>
                I combined <b>Psychology (4-Genius Framework)</b> with <b>Technology (AI Agents)</b>.
                Now, I don't just sell degrees; I architect careers.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.info("💡 **Why TFI?**")
        st.markdown("""
        I have the **Grit** of a factory worker.
        I have the **Empathy** of a counselor.
        I have the **Vision** of a founder.
        
        I want to bring this combination of **Operations + Tech + Heart** to Teach For India's Staff Team.
        """)

# --- TAB 2: THE FRAMEWORK ---
with tab2:
    st.header("We don't ask for Marks. We ask for Energy.")
    st.write("The core philosophy of Distoversity: You cannot judge a fish by its ability to climb a tree.")
    
    c1, c2 = st.columns(2)
    with c1:
        energy = st.selectbox("Select a Profile to Analyze:", ["Dynamo (Creator)", "Blaze (Influencer)", "Tempo (Catalyst)", "Steel (Analyst)"])
    
    with c2:
        if "Dynamo" in energy:
            st.success("🌟 **Dynamo (Creator):** Innovation-driven. Needs freedom. Bad at routine.")
        elif "Blaze" in energy:
            st.warning("🔥 **Blaze (Influencer):** People-driven. Needs conversation. Bad at spreadsheets.")
        elif "Tempo" in energy:
            st.info("🤝 **Tempo (Catalyst):** Timing-driven. Needs harmony. Bad at chaos.")
        elif "Steel" in energy:
            st.error("📊 **Steel (Analyst):** Data-driven. Needs clarity. Bad at hype.")

# --- TAB 3: EDUVEER BOT ---
with tab3:
    st.title("🤖 Eduveer AI Demo")
    st.caption("Experience the tech: A Logic-based counselor for remote India.")

    # LOGIC CONTROLLER
    if st.session_state.step == 0:
        if st.button("Start AI Assessment ➔", type="primary"):
            st.session_state.step = 1
            st.rerun()

    elif st.session_state.step == 1:
        curr = QUESTIONS[st.session_state.q_index]
        st.markdown(f"**Q{st.session_state.q_index + 1}:** {curr['q']}")
        cols = st.columns(2)
        for i, (txt, en) in enumerate(curr["options"]):
            if cols[i%2].button(txt, key=f"btn_{i}"):
                st.session_state.scores[en] += 1
                if st.session_state.q_index < 2:
                    st.session_state.q_index += 1
                else:
                    st.session_state.step = 2
                st.rerun()

    elif st.session_state.step == 2:
        primary = max(st.session_state.scores, key=st.session_state.scores.get)
        st.success(f"🎉 **Result: You are a {primary}!**")
        st.write("Here are the universities that match your DNA:")
        
        matches = [u for u in UNIVERSITIES if primary in u["best_for"]]
        for u in matches:
            st.markdown(f"""
            <div style="padding:15px; border:1px solid #ddd; border-radius:10px; margin-bottom:10px;">
                <h4>{u['name']}</h4>
                <p><b>Fee:</b> {u['fee']} | <b>Pkg:</b> {u['high_pkg']}</p>
            </div>
            """, unsafe_allow_html=True)
            
        if st.button("Restart Demo"):
            st.session_state.step = 0
            st.session_state.scores = {"Creator": 0, "Influencer": 0, "Analyst": 0, "Catalyst": 0}
            st.rerun()
