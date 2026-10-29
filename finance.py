from agno.agent import Agent

from agno.models.openrouter import OpenRouter
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.6-27b"),
        tools=[DuckDuckGoTools(), YFinanceTools(), ],
        description="You are an investment Analyst that researches stoch prices, analyst recommendations, and stock fundamentals",
        instructions="Use given tool whenever possible. Format your response using tables to display data where possible.",
        add_datetime_to_context=True,
        debug_mode=True
    )


finance_agent = build_agent()

# finance_agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)   # NVDA is a symbol in US for Nvidia stock market, each stock market has a symbol


finance_agent.print_response("Share the MSFT stock price in INR and analyst recommendations", markdown=True)