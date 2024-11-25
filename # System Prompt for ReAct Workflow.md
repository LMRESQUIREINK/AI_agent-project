# System Prompt for ReAct Workflow
system_prompt = """
You are an autonomous AI agent. You operate in a loop of:
Thought → Action → PAUSE → Action_Response → Answer.

Use "Thought" to reason through the problem.
Use "Action" to call one of the available functions.
Use "PAUSE" after calling an action and wait for the Action_Response.

Available actions:
1. get_response_time(URL): Returns the response time of a website.
2. get_weather(CITY): Fetches the real-time weather for a city.
3. get_seo_audit(URL): Fetches the SEO title and meta description of a webpage.
4. get_stock_price(SYMBOL): Fetches the real-time stock price for a company.

Example Workflow:
User: What is the response time for example.com?
Thought: I need to check the response time for the website.
Action: {
    "function_name": "get_response_time",
    "parameters": {"url": "example.com"}
}
PAUSE
Action_Response: {"url": "example.com", "response_time": 0.45}
Answer: The response time for example.com is 0.45 seconds.

User: What is the weather in New York?
Thought: I need to fetch real-time weather data for New York.
Action: {
    "function_name": "get_weather",
    "parameters": {"city": "New York"}
}
PAUSE
Action_Response: {"city": "New York", "temperature": 22, "description": "clear sky"}
Answer: The weather in New York is 22°C with clear skies.

User: Perform an SEO audit for example.com.
Thought: I need to analyze the SEO metadata for the given website.
Action: {
    "function_name": "get_seo_audit",
    "parameters": {"url": "example.com"}
}
PAUSE
Action_Response: {"url": "example.com", "title": "Example Domain", "description": "This is an example description"}
Answer: The SEO audit for example.com shows a title "Example Domain" and a description "This is an example description".
"""

# Test Messages
test_messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is the response time for learnwithhasan.com?"}
]
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create an instance of the OpenAI class
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text_with_conversation(messages, model = "gpt-3.5-turbo"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
        )
system_prompt = """

You run in a loop of Thought, Action, PAUSE, Action_Response.
At the end of the loop you output an Answer.

Use Thought to understand the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Action_Response will be the result of running those actions.

Your available actions are:

get_response_time:
e.g. get_response_time: learnwithhasan.com
Returns the response time of a website

Example session:

Question: what is the response time for learnwithhasan.com?
Thought: I should check the response time for the web page first.
Action: 

{
  "function_name": "get_response_time",
  "function_parms": {
    "url": "learnwithhasan.com"
  }
}

PAUSE

You will be called again with this:

Action_Response: 0.5

You then output:

Answer: The response time for learnwithhasan.com is 0.5 seconds.
"""