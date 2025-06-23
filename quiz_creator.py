from typing import Any, Dict
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI

class QuizCreatorTool(BaseTool):
    name: str = "quiz_creator"
    description: str = (
        "Create a quiz based on the explanation text. "
        "Input should be a dictionary with a key 'content' that contains the explanation."
    )

    def _run(self, content: str) -> str:
        """Run the tool synchronously."""
        prompt = (
            f"You are a helpful tutor. Based on the following explanation, create a quiz to test understanding:\n\n"
            f"Explanation:\n{content}\n\n"
            f"🎯 Generate 5 questions:\n"
            f"- Mix multiple-choice and short-answer types.\n"
            f"- For multiple-choice, give 4 options and mark the correct one with *(Correct)*.\n"
            f"- Keep questions clear, concise, and age-appropriate.\n"
        )
        llm = ChatOpenAI(model="gpt-4o-mini")
        response = llm.invoke(prompt)
        return response.content

    def _arun(self, content: str) -> str:
        raise NotImplementedError("Async version not implemented.")
