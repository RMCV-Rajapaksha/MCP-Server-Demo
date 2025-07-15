from mcp.server.fastmcp import FastMCP  

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # Simulating a weather API call
    # In a real application, you would use an actual weather API here
    return f"It's sunny in {location} with a temperature of 25°C."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
    # mcp.run(host="