from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Define the state of our graph
class State(TypedDict):
    messages: List[Dict[str, str]]
    generation: str

# Define the nodes of our graph
def retrieve(state: State) -> dict:
    """Retrieve relevant information based on the conversation history."""
    # This is a simplified example - in a real app, you'd query a database or API here
    return {"retrieved_docs": ["LangGraph is a library for building stateful, multi-actor applications with LLMs."]}

def generate(state: State) -> dict:
    """Generate a response based on the retrieved information."""
    # Get the last message from the conversation
    last_message = state["messages"][-1]["content"] if state["messages"] else ""
    
    # In a real app, you'd use an LLM here
    response = f"You asked: '{last_message}'. "
    response += "LangGraph is a library for building stateful, multi-actor applications with LLMs. "
    response += "This is a demo response from the LangGraph workflow."
    
    return {
        "generation": response, 
        "messages": state["messages"] + [{"role": "assistant", "content": response}]
    }

# Create the workflow
workflow = StateGraph(State)

# Add nodes to the workflow
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

# Define the edges
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Set the entry point
workflow.set_entry_point("retrieve")

# Compile the workflow
app = workflow.compile()

# Example usage
if __name__ == "__main__":
    # Initialize the state with a user message
    initial_state = {
        "messages": [
            {"role": "user", "content": "Tell me about LangGraph"}
        ],
        "generation": ""
    }
    
    print("Starting LangGraph workflow...\n")
    
    # Run the workflow
    for output in app.stream(initial_state):
        for key, value in output.items():
            if key != "__end__":
                print(f"Node '{key}':")
                print(f"  Output: {value}")
                print("-" * 50)
    
    # Get the final state
    final_state = app.invoke(initial_state)
    
    print("\nFinal response:")
    print("-" * 50)
    print(final_state["generation"])
    
    print("\nFull conversation:")
    print("-" * 50)
    for msg in final_state["messages"]:
        print(f"{msg['role'].title()}: {msg['content']}")
