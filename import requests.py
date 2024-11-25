import requests
from bs4 import BeautifulSoup


# Function 1: Get Website Response Time
def get_response_time(url: str) -> dict:
    """
    Fetches the response time for a given website.
    Args:
        url (str): The URL of the website to check.
    Returns:
        dict: A dictionary containing the response time or an error message.
    """
    try:
        response = requests.get(url, timeout=10)
        return {"url": url, "response_time": response.elapsed.total_seconds()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# Function 2: Get Weather Data
def get_weather(city: str, api_key: str) -> dict:
    """
    Fetches real-time weather data for a given city using OpenWeatherMap API.
    Args:
        city (str): Name of the city to get weather for.
        api_key (str): OpenWeatherMap API key.
    Returns:
        dict: Weather details including temperature, description, etc.
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data.get("name", city),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# Function 3: Perform SEO Audit
def get_seo_audit(url: str) -> dict:
    """
    Performs a basic SEO audit of a webpage by extracting its title and meta description.
    Args:
        url (str): The URL to analyze.
    Returns:
        dict: SEO details like the page title and meta description.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the title
        title = soup.title.string if soup.title else "No title found"

        # Extract the meta description
        meta_description = soup.find("meta", attrs={"name": "description"})
        description = meta_description["content"] if meta_description else "No description found"

        return {"url": url, "title": title, "description": description}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# Function 4: Fetch Stock Price
def get_stock_price(symbol: str, api_key: str) -> dict:
    """
    Fetches the real-time stock price of a company using Alpha Vantage API.
    Args:
        symbol (str): The stock symbol (e.g., AAPL for Apple).
        api_key (str): Alpha Vantage API key.
    Returns:
        dict: Current stock price and other details.
    """
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        quote = data.get("Global Quote", {})
        return {
            "symbol": quote.get("01. symbol", symbol),
            "price": quote.get("05. price", "N/A"),
            "change": quote.get("09. change", "N/A"),
            "percent_change": quote.get("10. change percent", "N/A"),
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# Dictionary of Available Actions
available_actions = {
    "get_response_time": get_response_time,
    "get_weather": lambda city: get_weather(city, "your_openweathermap_api_key"),
    "get_seo_audit": get_seo_audit,
    "get_stock_price": lambda symbol: get_stock_price(symbol, "your_alpha_vantage_api_key"),
}
def get_response_time(url):
    if url == "learnwithhasan.com":
        return 0.5
    if url == "google.com":
        return 0.3
    if url == "openai.com":
        return 0.4