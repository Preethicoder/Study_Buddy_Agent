from typing import Any

from langchain_core.tools import BaseTool


class AdditionTool(BaseTool):
    name: str = "add_numbers"
    description: str = "Add two numbers. Accepts a dictionary with 'a' and 'b' as keys."

    def _run(self, a: float, b: float) -> float:
        """Synchronous addition"""
        return a + b

    def _arun(self, a: float, b: float) -> float:
        """Asynchronous addition"""
        return a + b