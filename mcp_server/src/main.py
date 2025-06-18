from mcp.server.fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
from dotenv import load_dotenv
import asyncio
import json
import os

from utils import GitHubUtils

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

# Default user ID for memory operations
DEFAULT_USER_ID = "user"
port = os.getenv("PORT", "8842")
print (f"Starting MCP server on port {port}")
print (f"Using host {os.getenv('HOST')}")
print (f"Using transport {os.getenv('TRANSPORT')}")

# Define the MCP server
mcp = FastMCP(
    name="ai-discovery-mcp-server",
    description="AI Discovery MCP Server",
    instructions="""This server provides documents and schemas for the AI Discovery Specification.
    Call get_ai_discovery_document() to retrieve the AI discovery specification document in markdown format.
    Call get_ai_discovery_schema() to retrieve the AI discovery schema in JSON format.""",
    host=os.getenv("HOST", "0.0.0.0"),
    port=int(os.getenv("PORT", "8842"))
)        

@mcp.resource("data://ai_discovery_document")
async def get_ai_discovery_document() -> str:
    """Retrieve the AI discovery document as markdown.
    Returns:
        str: The AI discovery document in markdown format.
    """
    try:
        ai_discovery_doc = GitHubUtils.get_ai_discovery_spec_document()
        return ai_discovery_doc
    except Exception as e:
        return f"Error retrieving AI discovery document: {str(e)}"

@mcp.resource("data://ai_discovery_schema")
async def get_ai_discovery_schema() -> str:
    """Get the AI discovery schema as JSON.
    Returns:
        str: The AI discovery schema in JSON format.
    """
    try:
        ai_discovery_schema = GitHubUtils.get_ai_discovery_schema()
        return ai_discovery_schema
    except Exception as e:
        return f"Error retrieving AI discovery schema: {str(e)}"

async def main():
    transport = os.getenv("TRANSPORT", "sse")
    if transport == 'sse':
        # Run the MCP server with sse transport
        await mcp.run_sse_async()
    else:
        # Run the MCP server with stdio transport
        await mcp.run_stdio_async()

if __name__ == "__main__":
    asyncio.run(main())