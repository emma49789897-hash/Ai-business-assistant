import streamlit as st
from agents import create_business_crew


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Business Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8f9fc;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="title">🤖 AI Business Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your business, identify problems, create strategies, '
    'generate marketing content and build an action plan.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="Enter your Groq API key"
    )

    st.info(
        "Your API key is entered only for this session. "
        "Do not hard-code your API key in your source code."
    )

    st.divider()

    st.markdown("### 🤖 AI Agents")

    st.write("1. Business Analyst")
    st.write("2. Problem Diagnosis")
    st.write("3. Strategy Agent")
    st.write("4. Marketing Agent")
    st.write("5. Content Agent")
    st.write("6. Action Planner")
    st.write("7. Business Manager")


# ---------------------------------------------------------
# BUSINESS INFORMATION
# ---------------------------------------------------------

st.subheader("📊 Tell us about your business")

business_name = st.text_input(
    "Business Name",
    placeholder="Example: Fashion Store"
)

business_type = st.text_input(
    "Business Type",
    placeholder="Example: Online clothing store"
)

business_goal = st.text_area(
    "Business Goal",
    placeholder=(
        "Example: Increase sales, improve customer engagement "
        "and grow social media presence."
    ),
    height=100
)

business_problem = st.text_area(
    "Current Business Problem",
    placeholder=(
        "Example: Sales have decreased, social media engagement "
        "is low and we are not getting enough customers."
    ),
    height=120
)

business_data = st.text_area(
    "Additional Business Data",
    placeholder=(
        "Add any useful information such as:\n"
        "- Monthly sales\n"
        "- Number of customers\n"
        "- Social media followers\n"
        "- Website traffic\n"
        "- Products\n"
        "- Target customers\n"
        "- Marketing activities\n"
        "- Competitor information"
    ),
    height=200
)


# ---------------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------------

analyze_button = st.button(
    "🚀 Analyze My Business",
    use_container_width=True,
    type="primary"
)


# ---------------------------------------------------------
# RUN CREW
# ---------------------------------------------------------

if analyze_button:

    if not api_key:
        st.error("Please enter your Groq API key.")
        st.stop()

    if not business_name:
        st.error("Please enter your business name.")
        st.stop()

    if not business_type:
        st.error("Please enter your business type.")
        st.stop()

    if not business_problem:
        st.error("Please describe your current business problem.")
        st.stop()

    # Combine user information

    business_info = f"""
    BUSINESS NAME:
    {business_name}

    BUSINESS TYPE:
    {business_type}

    BUSINESS GOAL:
    {business_goal}

    CURRENT BUSINESS PROBLEM:
    {business_problem}

    ADDITIONAL BUSINESS DATA:
    {business_data}
    """

    # -----------------------------------------------------
    # CREATE CREW
    # -----------------------------------------------------

    try:

        with st.spinner(
            "🤖 AI agents are analyzing your business..."
        ):

            crew = create_business_crew(
                api_key=api_key,
                business_info=business_info
            )

            result = crew.kickoff()

        # -------------------------------------------------
        # DISPLAY RESULT
        # -------------------------------------------------

        st.success("Business analysis completed!")

        st.divider()

        st.subheader("📋 AI Business Report")

        st.markdown(result.raw)

        # -------------------------------------------------
        # DOWNLOAD REPORT
        # -------------------------------------------------

        st.divider()

        st.download_button(
            label="📥 Download Business Report",
            data=result.raw,
            file_name="ai_business_report.txt",
            mime="text/plain",
            use_container_width=True
        )

    except Exception as e:

        st.error(
            "Something went wrong while running the AI agents."
        )

        st.exception(e)
