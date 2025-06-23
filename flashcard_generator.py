from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI


class FlashcardGeneratorTool(BaseTool):
    name: str = "flashcard_generator"
    description: str = (
        "Generate flashcards from a given explanation. "
        "Input should be a dictionary with a key 'notes' that includes the previously generated explanation."
    )

    def _run(self, explanation: str) -> str:
        """Run the tool synchronously."""
        prompt = (
            "Based on the following explanation, generate 5 clear and concise flashcards.\n\n"
            f"Explanation:\n{explanation}\n\n"
            "Format the flashcards like this:\n"
            "Q: [Question]\n"
            "A: [Answer]\n\n"
            "Use simple language suitable for learners."
        )
        llm = ChatOpenAI(model="gpt-4o-mini")
        response = llm.invoke(prompt)
        return response.content

    def _arun(self, explanation: str) -> str:
        raise NotImplementedError("Async version not implemented.")
