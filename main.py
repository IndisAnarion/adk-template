import os
from re import A
from dotenv import load_dotenv
from fastapi import Request
from google.adk.cli.fast_api import get_fast_api_app
from sympy import true

load_dotenv()

AGENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),     "agents")

# Create FastAPI app using ADK's built-in function
app = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=true
)

# Add custom health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for load balancer and monitoring."""
    return {
        "status": "healthy",
        "service": "integration-system",
        "agents": ["bi_agent", "employee_agent"],
        "web_interface": true,
    }

if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting KAI Integration System Server")
    print("=" * 50)
    print(f"📊 Agent Directory: {AGENT_DIR}")
    print(f"🌐 Web Interface: {'Enabled' if true else 'Disabled'}")
    print(f"🔗 Server URL: http://localhost:9999")

    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=9999,
        log_level="info"
    )