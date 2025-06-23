
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI




class TopicExplainerTool(BaseTool):
    name:str ="topic_explainer"
    description:str = "Explains a topic clearly. Input should be a dictionary with a key 'topic'."

    def _run(self,topic:str):
        """Run the tool synchronously."""
        prompt = f"Explain the topic '{topic}' in a simple and clear way for a student."
        llm = ChatOpenAI(model="gpt-4o-mini")
        response = llm.invoke(prompt)
        return response.content