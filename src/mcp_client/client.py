from __future__ import annotations

from typing import Any

import httpx


class McpClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def list_tools(self) -> list[dict[str, Any]]:
        with httpx.Client(timeout=10.0) as client:
            resp = client.get(f"{self.base_url}/tools")
            resp.raise_for_status()
            return resp.json()

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{self.base_url}/tools/call",
                json={"name": name, "arguments": arguments},
            )
            resp.raise_for_status()
            return resp.json()
