from mcp.server.fastmcp import FastMCP

# Create the server — give it a name
mcp = FastMCP("first-python-mcp")


# Tool 1 — simple greeting
@mcp.tool()
def say_hello(name: str) -> str:
    """
    Greets a person by name.
    name: the person's name to greet.
    Returns a greeting message.
    """
    return f"Hello {name}! Your Python MCP is working."


# Tool 2 — simple calculator
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers together.
    a: first number.
    b: second number.
    Returns the sum.
    """
    return a + b


# Tool 3 — reverse a string
@mcp.tool()
def reverse_text(text: str) -> str:
    """
    Reverses any text string given to it.
    text: the string to reverse.
    Returns the reversed string.
    """
    return text[::-1]


# Run the server
if __name__ == "__main__":
    mcp.run()