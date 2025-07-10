import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="U of M Data engine")

@mcp.tool()
def get_term(s_campus: str) -> str:
    """Get the current term for a campus"""
    if s_campus == "UMNTC":
        return "TwinCitiesTerm"
    else:
        return "MadeUpTermValue"

if __name__ == "__main__":
    mcp.run(transport="stdio")
