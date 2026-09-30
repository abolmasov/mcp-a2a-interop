from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any
import uuid


class A2ATask(BaseModel):
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    intent: str
    payload: dict[str, Any] = Field(default_factory=dict)


class A2AResult(BaseModel):
    task_id: str
    status: str
    output: dict[str, Any] = Field(default_factory=dict)


class LocalPeerAgent:
    """Minimal in-process peer agent for A2A-style delegation demos."""

    def handle(self, task: A2ATask) -> A2AResult:
        return A2AResult(
            task_id=task.task_id,
            status="completed",
            output={"echo_intent": task.intent, "accepted_payload": task.payload},
        )
