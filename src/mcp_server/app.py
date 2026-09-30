from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="MCP-style Tool Server", version="0.1.0")


class ToolDef(BaseModel):
    name: str
    description: str
    input_schema: dict[str, Any]


class CallRequest(BaseModel):
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)


TOOLS: dict[str, ToolDef] = {
    "echo": ToolDef(
        name="echo",
        description="Echo text back for connectivity checks",
        input_schema={"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]},
    ),
    "add": ToolDef(
        name="add",
        description="Add two numbers",
        input_schema={
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"],
        },
    ),
}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tools", response_model=list[ToolDef])
def list_tools() -> list[ToolDef]:
    return list(TOOLS.values())


@app.post("/tools/call")
def call_tool(req: CallRequest) -> dict[str, Any]:
    if req.name not in TOOLS:
        raise HTTPException(status_code=404, detail="Unknown tool")
    if req.name == "echo":
        return {"content": req.arguments.get("text", "")}
    if req.name == "add":
        return {"content": float(req.arguments["a"]) + float(req.arguments["b"])}
    raise HTTPException(status_code=400, detail="Unhandled tool")
