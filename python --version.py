python --version
C:\Users\LMRESQUIREINK\Documents\ai_agent_project>
python -m venv venv
.\venv\Scripts\Activate
pip install openai python-dotenv
pip list
print("Virtual Environment is working!")
python main.py
Virtual Environment is working!
from actions import get_response_time, get_weather, get_seo_audit, get_stock_price

# Example Usage
response_time = get_response_time("https://example.com")
print(response_time)

weather = get_weather("New York", "your_openweathermap_api_key")
print(weather)

seo_audit = get_seo_audit("https://example.com")
print(seo_audit)

stock = get_stock_price("AAPL", "your_alpha_vantage_api_key")
print(stock)
What is the response time for learnwithhasan.com?
I need to check the response time for the website.
{
    "function_name": "get_response_time",
    "parameters": {"url": "learnwithhasan.com"}
}
{
    "url": "learnwithhasan.com",
    "response_time": 0.32
}
The response time for learnwithhasan.com is 0.32 seconds.
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
weather = get_weather("New York", os.getenv("OPENWEATHER_API_KEY"))
stock = get_stock_price("AAPL", os.getenv("ALPHA_VANTAGE_API_KEY"))
from actions import get_response_time, get_weather, get_seo_audit, get_stock_price
import os
from dotenv import load_dotenv

load_dotenv()

# Test functions
print("Testing get_response_time:")
print(get_response_time("https://example.com"))

print("Testing get_weather:")
print(get_weather("New York", os.getenv("OPENWEATHER_API_KEY")))

print("Testing get_seo_audit:")
print(get_seo_audit("https://example.com"))

print("Testing get_stock_price:")
print(get_stock_price("AAPL", os.getenv("ALPHA_VANTAGE_API_KEY")))
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting the AI Agent...")
import json

def save_results(data, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
# Define a list of messages to simulate a conversation
test_messages = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "system", "content": "You are a helpful AI assistant"}
]

# Call the function with the test messages
response = generate_text_with_conversation(test_messages)
print("AI Response:", response)

import sys

print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

import sys

def print_python_version():
    """
    Prints the Python version installed on this system.
    """
    print(f"Python Version: {sys.version}")
    print(f"Version Info: {sys.version_info}")

if __name__ == "__main__":
    print_python_version()


