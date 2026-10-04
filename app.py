import streamlit as st
from agents import create_business_crew

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Business Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    /* Main Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #172554 45%,
            #312e81 100%
        );
        color: white;
    }

    /* Hide Streamlit Header */
    header {
        visibility: hidden;
    }

    /* Main Container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero Section */
    .hero {
        padding: 35px;
        border-radius: 25px;
        background: linear-gradient(
            135deg,
            rgba(37, 99, 235, 0.35),
            rgba(124, 58, 237, 0.35)
        );
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 45px;
        margin-bottom: 10px;
        color: white;
    }

    .hero p {
        font-size: 18px;
        color: #dbeafe;
    }

    /* Cards */
    .card {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .card h3 {
        color: #c4b5fd;
    }

    /* Section Titles */
    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
        color: white;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 14px;
        font-size: 17px;
        font-weight: 700;
        color: white;
        background: linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        );
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(124,58,237,0.4);
    }

    /* Input Fields */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255,255,255,0.08);
        color: white;
        border-radius: 12px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #111827,
            #1e1b4b
        );
    }

    /* Success */
    .success-box {
        background: rgba(34,197,94,0.12);
        border: 1px solid rgba(34,197,94,0.3);
        padding: 18px;
        border-radius: 15px;
    }

    /* Feature Cards */
    .feature {
        text-align: center;
        padding: 20px;
        border-radius: 18px;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.12);
        height: 150px;
    }

    .feature-icon {
        font-size: 35px;
    }

    .feature-title {
        font-size: 17px;
        font-weight: 700;
        margin-top: 8px;
    }

    .feature-text {
        font-size: 13px;
        color: #cbd5e1;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("## 🤖 AI Business Assistant")

    st.markdown("""
    <div class="card">
        <h3>🚀 AI-Powered Business Analysis</h3>
        <p>
        Analyze your business, identify problems,
        create strategies, generate marketing ideas,
        and build actionable tasks.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧠 AI Agents")

    st.markdown("""
    **📊 Business Analyst**  
    Analyzes your business

    **🔍 Problem Diagnosis**  
    Finds major problems

    **🎯 Strategy Agent**  
    Creates business strategies

    **📢 Marketing Agent**  
    Suggests marketing approaches

    **✍️ Content Agent**  
    Generates content ideas

    **✅ Action Planner**  
    Creates actionable tasks
    """)

    st.markdown("---")

    st.caption("Powered by CrewAI + Groq")


# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">

    <h1>🤖 AI Business Assistant</h1>

    <p>
    Your intelligent multi-agent business partner.
    Analyze problems, discover opportunities,
    create strategies and turn ideas into action.
    </p>

</div>
""", unsafe_allow_html=True)


# -----------------------------
# Features
# -----------------------------
st.markdown(
    '<div class="section-title">✨ What can AI Business Assistant do?</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Analyze</div>
        <div class="feature-text">
        Understand your business data
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Diagnose</div>
        <div class="feature-text">
        Identify business problems
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Strategize</div>
        <div class="feature-text">
        Build practical strategies
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🚀</div>
        <div class="feature-title">Take Action</div>
        <div class="feature-text">
        Turn ideas into tasks
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# -----------------------------
# Business Information
# -----------------------------
st.markdown(
    '<div class="section-title">📋 Tell us about your business</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    business_name = st.text_input(
        "Business Name",
        placeholder="e.g. Fashion Hub"
    )

    business_type = st.text_input(
        "Business Type",
        placeholder="e.g. Facebook Page / E-commerce Store"
    )

    business_goal = st.selectbox(
        "Main Business Goal",
        [
            "Increase Sales",
            "Increase Brand Awareness",
            "Get More Customers",
            "Improve Social Media",
            "Improve Customer Engagement",
            "Grow Online Business"
        ]
    )


with col2:

    business_problem = st.text_area(
        "Current Business Problem",
        placeholder="e.g. Low sales, low engagement, fewer customers...",
        height=120
    )

    additional_data = st.text_area(
        "Additional Business Information",
        placeholder="Add products, target audience, location, social media details, etc.",
        height=120
    )


# -----------------------------
# Analyze Button
# -----------------------------
st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button(
    "🚀 Analyze My Business"
)


# -----------------------------
# Run AI Crew
# -----------------------------
if analyze:

    if not business_name:
        st.warning("Please enter your business name.")

    elif not business_type:
        st.warning("Please enter your business type.")

    elif not business_problem:
        st.warning("Please describe your business problem.")

    else:

        # Get API key from Streamlit Secrets
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            st.error(
                "Groq API key is not configured. "
                "Please add GROQ_API_KEY to Streamlit Secrets."
            )
            st.stop()

        business_info = f"""
Business Name: {business_name}

Business Type: {business_type}

Business Goal: {business_goal}

Current Problem: {business_problem}

Additional Information:
{additional_data}
"""

        with st.spinner(
            "🤖 AI agents are analyzing your business..."
        ):

            try:

                crew = create_business_crew(
                    api_key=api_key,
                    business_info=business_info
                )

                result = crew.kickoff()

                st.markdown(
                    '<div class="section-title">📊 Your AI Business Report</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="card">',
                    unsafe_allow_html=True
                )

                st.markdown(result.raw)

                st.markdown("</div>", unsafe_allow_html=True)

                st.success(
                    "✅ Business analysis completed successfully!"
                )

                st.download_button(
                    label="📥 Download Business Report",
                    data=result.raw,
                    file_name="AI_Business_Report.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    "Something went wrong while running the AI agents."
                )

                st.code(str(e))
