from crewai import Agent, Task, Crew, Process, LLM


def create_business_crew(api_key, business_info):

    # ---------------------------------------------------------
    # GROQ LLM
    # ---------------------------------------------------------

    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.3
    )

    # ---------------------------------------------------------
    # AGENT 1: BUSINESS ANALYST
    # ---------------------------------------------------------

    business_analyst = Agent(
        role="Business Data Analyst",
        goal=(
            "Analyze the business information provided by the user "
            "and identify important business insights, trends, "
            "strengths, weaknesses and opportunities."
        ),
        backstory=(
            "You are an experienced business analyst. "
            "You carefully examine business information and "
            "turn raw information into clear and useful insights."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # ---------------------------------------------------------
    # AGENT 2: PROBLEM DIAGNOSIS
    # ---------------------------------------------------------

    problem_diagnosis = Agent(
        role="Business Problem Diagnosis Specialist",
        goal=(
            "Identify the main business problems and explain "
            "their possible causes based on the business analysis."
        ),
        backstory=(
            "You are a business consultant who specializes in "
            "finding the root causes of business problems. "
            "You focus on practical and evidence-based diagnosis."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # ---------------------------------------------------------
    # AGENT 3: STRATEGY
    # ---------------------------------------------------------

    strategy_agent = Agent(
        role="Business Strategy Consultant",
        goal=(
            "Create practical strategies that can help the business "
            "solve its identified problems and achieve its goals."
        ),
        backstory=(
            "You are a strategic business consultant. "
            "You create realistic strategies that small and medium "
            "businesses can actually implement."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # ---------------------------------------------------------
    # AGENT 4: MARKETING
    # ---------------------------------------------------------

    marketing_agent = Agent(
        role="Marketing Strategist",
        goal=(
            "Develop marketing strategies, campaign ideas, "
            "promotional ideas and customer engagement approaches "
            "based on the business strategy."
        ),
        backstory=(
            "You are a digital marketing strategist experienced "
            "in social media marketing, customer acquisition, "
            "brand awareness and online campaigns."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # ---------------------------------------------------------
    # AGENT 5: CONTENT
    # ---------------------------------------------------------

    content_agent = Agent(
        role="Marketing Content Specialist",
        goal=(
            "Create useful marketing content based on the business "
            "strategy and marketing recommendations."
        ),
        backstory=(
            "You are a professional content strategist. "
            "You create social media posts, captions, hooks, "
            "content ideas and calls to action."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # ---------------------------------------------------------
    # AGENT 6: ACTION PLANNER
    # ---------------------------------------------------------

    action_planner = Agent(
        role="Business Action Planner",
        goal=(
            "Convert business recommendations into clear, "
            "prioritized and actionable tasks."
        ),
        backstory=(
            "You are a productivity and business operations expert. "
            "You turn strategies into practical steps that a business "
            "owner can follow."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # ---------------------------------------------------------
    # AGENT 7: BUSINESS MANAGER
    # ---------------------------------------------------------

    business_manager = Agent(
        role="Senior Business Manager",
        goal=(
            "Combine all agent outputs into one clear and practical "
            "business improvement plan."
        ),
        backstory=(
            "You are a senior business manager who reviews analysis, "
            "diagnosis, strategy, marketing recommendations and "
            "action plans. You produce a concise final business report."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # =========================================================
    # TASK 1: BUSINESS ANALYSIS
    # =========================================================

    analysis_task = Task(
        description=f"""
        Analyze the following business information:

        {business_info}

        Identify:

        1. Business overview
        2. Main business goals
        3. Important strengths
        4. Important weaknesses
        5. Opportunities
        6. Threats or risks
        7. Important business insights
        8. Areas that need improvement

        Do not invent specific facts that are not provided.
        Clearly separate known information from reasonable assumptions.
        """,

        expected_output="""
        A structured business analysis containing:
        - Business overview
        - Goals
        - Strengths
        - Weaknesses
        - Opportunities
        - Risks
        - Key insights
        """,

        agent=business_analyst
    )

    # =========================================================
    # TASK 2: PROBLEM DIAGNOSIS
    # =========================================================

    diagnosis_task = Task(
        description="""
        Review the business analysis from the previous agent.

        Identify the most important business problems.

        For each problem provide:

        1. Problem
        2. Possible cause
        3. Business impact
        4. Priority

        Focus on the problems that can have the greatest effect
        on the business.

        Do not invent numerical data.
        """,

        expected_output="""
        A prioritized list of business problems with:
        - Problem
        - Possible cause
        - Business impact
        - Priority
        """,

        agent=problem_diagnosis,
        context=[analysis_task]
    )

    # =========================================================
    # TASK 3: STRATEGY
    # =========================================================

    strategy_task = Task(
        description="""
        Based on the business analysis and problem diagnosis,
        develop practical business strategies.

        For each strategy provide:

        1. Strategy name
        2. Problem it addresses
        3. Why it can help
        4. Implementation approach
        5. Expected business benefit
        6. Important considerations

        Keep the strategies realistic for a small or medium business.
        """,

        expected_output="""
        A practical business strategy plan containing:
        - Strategy
        - Problem addressed
        - Implementation
        - Expected benefit
        - Considerations
        """,

        agent=strategy_agent,
        context=[analysis_task, diagnosis_task]
    )

    # =========================================================
    # TASK 4: MARKETING
    # =========================================================

    marketing_task = Task(
        description="""
        Based on the business analysis, problems and strategies,
        create a practical marketing plan.

        Include:

        1. Target audience
        2. Marketing objectives
        3. Marketing channels
        4. Campaign ideas
        5. Promotional ideas
        6. Customer engagement ideas
        7. Suggested calls to action

        Focus on practical digital marketing opportunities.
        """,

        expected_output="""
        A practical marketing plan with:
        - Target audience
        - Objectives
        - Channels
        - Campaign ideas
        - Promotion ideas
        - Engagement ideas
        - CTAs
        """,

        agent=marketing_agent,
        context=[analysis_task, diagnosis_task, strategy_task]
    )

    # =========================================================
    # TASK 5: CONTENT
    # =========================================================

    content_task = Task(
        description="""
        Create marketing content based on the marketing plan.

        Generate:

        1. Five social media content ideas
        2. Three strong hooks
        3. Three sample captions
        4. Three calls to action
        5. Three short-form video ideas

        Keep the content relevant to the business.
        Avoid making unsupported claims.
        """,

        expected_output="""
        A content package containing:
        - 5 content ideas
        - 3 hooks
        - 3 captions
        - 3 CTAs
        - 3 short video ideas
        """,

        agent=content_agent,
        context=[marketing_task, strategy_task]
    )

    # =========================================================
    # TASK 6: ACTION PLAN
    # =========================================================

    action_task = Task(
        description="""
        Convert all recommendations into a practical action plan.

        Create:

        1. Immediate actions
        2. Short-term actions
        3. Medium-term actions
        4. Priority level
        5. Suggested sequence

        Make each action specific and easy to understand.

        The business owner should be able to take the output
        and start implementing it immediately.
        """,

        expected_output="""
        A prioritized action plan containing:
        - Immediate actions
        - Short-term actions
        - Medium-term actions
        - Priority
        - Implementation sequence
        """,

        agent=action_planner,
        context=[
            analysis_task,
            diagnosis_task,
            strategy_task,
            marketing_task,
            content_task
        ]
    )

    # =========================================================
    # TASK 7: FINAL BUSINESS REPORT
    # =========================================================

    final_task = Task(
        description="""
        Create the final AI Business Assistant report.

        Combine the useful information from all previous agents.

        Use the following structure:

        # AI BUSINESS ASSISTANT REPORT

        ## 1. Business Overview

        ## 2. Key Business Insights

        ## 3. Main Problems

        ## 4. Recommended Business Strategies

        ## 5. Marketing Strategy

        ## 6. Content Recommendations

        ## 7. Action Plan

        ## 8. Priority Actions

        ## 9. Final Recommendations

        Keep the report practical, clear and easy for a business
        owner to understand.

        Do not repeat unnecessary information.
        Do not invent facts.
        """,

        expected_output="""
        A complete professional AI Business Assistant report
        containing business analysis, problems, strategies,
        marketing recommendations, content ideas and an
        actionable implementation plan.
        """,

        agent=business_manager,
        context=[
            analysis_task,
            diagnosis_task,
            strategy_task,
            marketing_task,
            content_task,
            action_task
        ]
    )

    # =========================================================
    # CREATE CREW
    # =========================================================

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
