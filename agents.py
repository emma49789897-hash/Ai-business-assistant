import os
from crewai import Agent, Task, Crew, Process, LLM


def create_business_crew(api_key, business_info):

    os.environ["GROQ_API_KEY"] = api_key

    # Prevent accidental OpenAI routing
    os.environ.pop("OPENAI_API_KEY", None)

    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.2
    )

    # -------------------------
    # Agents
    # -------------------------

    business_analyst = Agent(
        role="Business Analyst",
        goal="Analyze the business and understand its current situation.",
        backstory="You are an experienced business analyst.",
        llm=llm,
        verbose=True
    )

    problem_diagnosis = Agent(
        role="Problem Diagnosis Specialist",
        goal="Identify the main business problems and their possible causes.",
        backstory="You specialize in finding the root causes of business problems.",
        llm=llm,
        verbose=True
    )

    strategy_agent = Agent(
        role="Business Strategy Expert",
        goal="Create practical strategies to improve business performance.",
        backstory="You are a strategic business consultant.",
        llm=llm,
        verbose=True
    )

    marketing_agent = Agent(
        role="Marketing Expert",
        goal="Create marketing strategies to attract customers and increase sales.",
        backstory="You are a digital marketing specialist.",
        llm=llm,
        verbose=True
    )

    content_agent = Agent(
        role="Content Strategist",
        goal="Create useful marketing content ideas for the business.",
        backstory="You are a creative content strategist.",
        llm=llm,
        verbose=True
    )

    action_planner = Agent(
        role="Action Planner",
        goal="Convert business recommendations into practical actionable tasks.",
        backstory="You specialize in turning strategies into clear action plans.",
        llm=llm,
        verbose=True
    )

    business_manager = Agent(
        role="Business Manager",
        goal="Combine all recommendations into one clear business report.",
        backstory="You are a senior business manager who creates final business plans.",
        llm=llm,
        verbose=True
    )

    # -------------------------
    # Tasks
    # -------------------------

    analysis_task = Task(
        description=f"""
        Analyze the following business:

        {business_info}

        Identify:
        - Current situation
        - Business strengths
        - Weaknesses
        - Opportunities
        - Important observations
        """,
        expected_output="A clear business analysis.",
        agent=business_analyst
    )

    diagnosis_task = Task(
        description="""
        Based on the business analysis, identify the major problems.

        Explain:
        - Main problems
        - Possible root causes
        - Business impact
        """,
        expected_output="A clear problem diagnosis.",
        agent=problem_diagnosis
    )

    strategy_task = Task(
        description="""
        Create practical strategies to solve the identified problems.

        Include:
        - Short-term strategies
        - Long-term strategies
        - Growth opportunities
        """,
        expected_output="A practical business strategy.",
        agent=strategy_agent
    )

    marketing_task = Task(
        description="""
        Create a marketing strategy based on the business analysis.

        Include:
        - Target customers
        - Marketing channels
        - Customer acquisition ideas
        - Sales improvement ideas
        """,
        expected_output="A practical marketing strategy.",
        agent=marketing_agent
    )

    content_task = Task(
        description="""
        Create useful content ideas for the business.

        Include:
        - Social media content ideas
        - Promotional ideas
        - Educational content
        - Engagement content
        """,
        expected_output="A list of useful marketing content ideas.",
        agent=content_agent
    )

    action_task = Task(
        description="""
        Convert all recommendations into an actionable plan.

        Include:
        - Priority
        - Action
        - Expected result
        - Suggested timeline
        """,
        expected_output="A practical action plan.",
        agent=action_planner
    )

    final_task = Task(
        description="""
        Create the final AI Business Assistant report.

        Organize the report into:

        1. Executive Summary
        2. Business Analysis
        3. Main Problems
        4. Business Strategies
        5. Marketing Strategy
        6. Content Ideas
        7. Action Plan
        8. Final Recommendations

        Make the report clear, practical and easy to understand.
        """,
        expected_output="A complete business improvement report.",
        agent=business_manager
    )

    # -------------------------
    # Crew
    # -------------------------

    crew = Crew(
        agents=[
            business_analyst,
            problem_diagnosis,
            strategy_agent,
            marketing_agent,
            content_agent,
            action_planner,
            business_manager
        ],
        tasks=[
            analysis_task,
            diagnosis_task,
            strategy_task,
            marketing_task,
            content_task,
            action_task,
            final_task
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew
