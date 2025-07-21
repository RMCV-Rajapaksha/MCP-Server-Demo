import json
from mcp.server.fastmcp import FastMCP  

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # Simulating a weather API call
    # In a real application, you would use an actual weather API here
    weather_data = {
        "location": location,
        "condition": "sunny",
        "temperature": 25,
        "unit": "°C",
        "humidity": 60,
        "wind_speed": 10,
        "wind_unit": "km/h"
    }
    return json.dumps(weather_data, indent=2)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    # mcp.run(host="localhost", port=8000)  # Alternative HTTP server setup

    # To run: python weather.py 