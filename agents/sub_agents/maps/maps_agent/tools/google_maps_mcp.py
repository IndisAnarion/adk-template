import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

google_maps_mcp_tools: MCPToolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx',
        args=[
            "-y",
            "@modelcontextprotocol/server-google-maps",
        ],
        env={
            "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY")
        }
    )
)