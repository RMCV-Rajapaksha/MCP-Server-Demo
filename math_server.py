from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """_summary_
    Adds two numbers.
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """_summary_
    Multiplies two numbers.
    """
    return a * b





if __name__ == "__main__":
    mcp.run(transport="stdio" )
    # mcp.run(host="