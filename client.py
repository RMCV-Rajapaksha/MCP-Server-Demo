from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI  # OpenAI model instead of Groq

from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            # "math": {
            #     "command": "python",
            #     "args": ["mathserver.py"],  # Ensure correct absolute path
            #     "transport": "stdio",
            # },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running
                "transport": "streamable_http",
            }
        }
    )

    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    tools = await client.get_tools()

    # Use OpenAI model (choose "gpt-4" or "gpt-3.5-turbo")
    model = ChatOpenAI(model="gpt-4o")  

    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    print("Math response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
    )
    print("Weather response:", weather_response['messages'][-1].content)

asyncio.run(main())
