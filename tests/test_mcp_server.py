from fastapi.testclient import TestClient
from src.mcp_server.app import app

client = TestClient(app)


def test_list_and_call_echo():
    tools = client.get("/tools").json()
    assert any(t["name"] == "echo" for t in tools)
    result = client.post("/tools/call", json={"name": "echo", "arguments": {"text": "ping"}}).json()
    assert result["content"] == "ping"
