from src.a2a.protocol import A2ATask, LocalPeerAgent


def test_peer_agent_completes_task():
    agent = LocalPeerAgent()
    result = agent.handle(A2ATask(intent="summarize", payload={"doc": "x"}))
    assert result.status == "completed"
    assert result.output["echo_intent"] == "summarize"
