# MCP Demo

A demonstration project showcasing the Model Context Protocol (MCP) with FastMCP servers and LangChain integration.

## Overview

This project demonstrates how to create and use MCP (Model Context Protocol) servers with FastMCP, integrating them with LangChain agents to create AI applications that can use external tools. The demo includes two example servers:

- **Math Server**: Provides basic mathematical operations (addition, multiplication)
- **Weather Server**: Simulates weather data retrieval for any location

## Features

- 🧮 **Math Operations**: Add and multiply numbers using MCP tools
- 🌤️ **Weather Information**: Get simulated weather data for any location
- 🤖 **AI Agent Integration**: Uses LangChain with OpenAI GPT-4 to interact with MCP tools
- 🔄 **Multiple Transport Types**: Demonstrates both stdio and HTTP transports

## Project Structure

```
MCP-Demo/
├── main.py              # Main entry point
├── math_server.py       # MCP server for mathematical operations
├── weather.py           # MCP server for weather information
├── client.py            # Client that integrates MCP servers with LangChain
├── pyproject.toml       # Project configuration and dependencies
├── requirements.txt     # Python dependencies
├── uv.lock             # UV lock file
└── README.md           # This file
```

## Requirements

- Python 3.10 or higher
- OpenAI API key (for the AI agent)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd MCP-Demo
   ```

2. **Install dependencies**:
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv (recommended)
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Running Individual Servers

#### Math Server (stdio transport)
```bash
python math_server.py
```

#### Weather Server (HTTP transport)
```bash
python weather.py
```
The weather server will run on `http://localhost:8000` by default.

### Running the Complete Demo

1. **Start the weather server** (in one terminal):
   ```bash
   python weather.py
   ```

2. **Run the client** (in another terminal):
   ```bash
   python client.py
   ```

The client will demonstrate both math and weather operations using the AI agent.

## MCP Servers

### Math Server (`math_server.py`)

Provides mathematical operations via stdio transport:

- `add(a: int, b: int) -> int`: Adds two numbers
- `multiply(a: int, b: int) -> int`: Multiplies two numbers

### Weather Server (`weather.py`)

Provides simulated weather information via HTTP transport:

- `get_weather(location: str) -> str`: Returns weather data for a given location

## Client Integration (`client.py`)

The client demonstrates how to:

1. Create a `MultiServerMCPClient` with multiple MCP servers
2. Configure different transport types (stdio and HTTP)
3. Integrate MCP tools with LangChain agents
4. Use OpenAI's GPT-4 model to interact with the tools

## Example Interactions

The demo client will perform these example interactions:

1. **Math Query**: "what's (3 + 5) x 12?"
   - Uses the math server's `add` and `multiply` tools
   - Expected result: 96

2. **Weather Query**: "what is the weather in California?"
   - Uses the weather server's `get_weather` tool
   - Returns simulated weather data

## Development

### Adding New Tools

To add new tools to the math server:

```python
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtracts b from a."""
    return a - b
```

To add new tools to the weather server:

```python
@mcp.tool()
async def get_forecast(location: str, days: int = 7) -> str:
    """Get weather forecast for multiple days."""
    # Implementation here
    pass
```

### Transport Types

- **stdio**: Direct process communication (used by math server)
- **streamable_http**: HTTP-based communication (used by weather server)

## Dependencies

- `mcp`: Core Model Context Protocol library
- `langchain-groq`: LangChain integration with Groq
- `langchain-mcp-adapters`: MCP adapters for LangChain
- `langgraph`: Graph-based agent framework
- `langchain-openai`: OpenAI integration for LangChain

## Troubleshooting

1. **Missing OpenAI API Key**: Make sure your `.env` file contains a valid OpenAI API key
2. **Port conflicts**: If port 8000 is busy, modify the port in `weather.py`
3. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for demonstration purposes. Please check individual dependency licenses for production use.

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [LangChain Documentation](https://python.langchain.com/)