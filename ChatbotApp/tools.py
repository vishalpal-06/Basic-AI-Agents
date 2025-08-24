from langchain_community.tools import DuckDuckGoSearchResults
from langchain.tools import tool
import datetime 
import math

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression (e.g., 2+2, sqrt(16))."""
    try:
        return str(eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt}))
    except Exception as e:
        return f"Error: {e}"

@tool
def get_time(_: str) -> str:
    """Returns the current system time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


search_tool = DuckDuckGoSearchResults(max_results=2)

tools = [calculator, get_time, search_tool]
