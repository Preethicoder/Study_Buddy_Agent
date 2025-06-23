import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

from flashcard_generator import FlashcardGeneratorTool
from topic_explainer import TopicExplainerTool
from quiz_creator import QuizCreatorTool
from current_date import CurrentDateTool
from addition import AdditionTool

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Instantiate tools
current_date_tool = CurrentDateTool()
addition_tool = AdditionTool()
topic_tool = TopicExplainerTool()
flashcard_generator_tool =FlashcardGeneratorTool()
quiz_creator_tool = QuizCreatorTool()
tools = [topic_tool,flashcard_generator_tool,quiz_creator_tool]

# Set up model
model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=OPENAI_API_KEY
)

# Create ReAct agent
agent = create_react_agent(model, tools=tools)


if __name__ == "__main__":
    input_topic = input("Enter the topic name you want to learn")
    print(input_topic)
    # Stream responses
    chunks = agent.stream({
        "messages": [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=f"""
    Please provide the following about the {input_topic}, strictly in this order and using clear formatting including emojis:

    1️⃣ **Explain the concept** — give a concise, easy-to-understand explanation of the {input_topic}.

    2️⃣ **Generate flashcards** — create 5 useful flashcards **based only on your explanation above**. Each flashcard should be formatted with a question and answer, using 🃏 emojis and bullet points.

    3️⃣ **Create a quiz** — create 5 short quiz questions **based only on your explanation above**, using a mix of multiple-choice (with 4 options and one correct answer) and short answer formats. Include ❓ emojis and numbering.

    ⚠️ Important: Use only the explanation from step 1 as input for steps 2 and 3. Do not introduce new information.

    Make the final output engaging with headings, spacing, and emojis.
            """)
        ]
    })

    explanation_text = ""
    flashcards_text = ""
    quiz_text = ""

    current_section = "explanation"

    for chunk in chunks:
        if "tools" in chunk and "messages" in chunk["tools"]:
            for tool_msg in chunk["tools"]["messages"]:
                tool_name = tool_msg.name
                content = tool_msg.content

                if tool_name == "topic_explainer":
                    explanation_text += content + "\n\n"
                elif tool_name == "flashcard_generator":
                    flashcards_text += content + "\n\n"
                elif tool_name == "quiz_creator":
                    quiz_text += content + "\n\n"

    # Final Output
    final_output = (
            "📘 **Concept Explanation**\n\n"
            + explanation_text.strip()
            + "\n\n🃏 **Flashcards**\n\n"
            + flashcards_text.strip()
            + "\n\n❓ **Quiz**\n\n"
            + quiz_text.strip()
    )

    print(final_output)  # or return/display it however you like