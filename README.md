# LangGraph Demo Project

This project demonstrates how to use LangGraph to build stateful, multi-actor applications with Large Language Models (LLMs). LangGraph provides a powerful way to create complex workflows and state machines for LLM applications.

## 🚀 Features

- **State Management**: Easily manage conversation state across multiple turns
- **Modular Design**: Break down complex workflows into manageable nodes
- **Flexible Integration**: Works with various LLM providers through LangChain
- **Visualization**: Built-in tools for visualizing your workflow graphs

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/langgraph-demo.git
   cd langgraph-demo
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Usage

Run the demo script:
```bash
python langgraph_demo.py
```

## 🏗️ Project Structure

- `langgraph_demo.py`: Main implementation of the LangGraph workflow
- `requirements.txt`: Project dependencies
- `README.md`: This documentation file

## 🤖 How It Works

The demo implements a simple workflow with three nodes:

1. **Retrieve**: Fetches relevant information based on the conversation
2. **Generate**: Processes the retrieved information to generate a response
3. **Update State**: Updates the conversation history with the new response

## 🧪 Example Output

When you run the demo, you'll see the flow of data through the graph:
```
Node 'retrieve':
  Output: {'retrieved_docs': ['LangGraph is a library for building stateful, multi-actor applications with LLMs.']}
--------------------------------------------------
Node 'generate':
  Output: {'generation': 'Based on the information: LangGraph is a library for building stateful, multi-actor applications with LLMs.. This is a demo response from LangGraph.'}
--------------------------------------------------
Node 'update_state':
  Output: {'messages': [{'role': 'user', 'content': 'Tell me about LangGraph'}, {'role': 'assistant', 'content': 'Based on the information: LangGraph is a library for building stateful, multi-actor applications with LLMs.. This is a demo response from LangGraph.'}], 'generation': 'Based on the information: LangGraph is a library for building stateful, multi-actor applications with LLMs.. This is a demo response from LangGraph.'}
--------------------------------------------------

Final response:
Based on the information: LangGraph is a library for building stateful, multi-actor applications with LLMs.. This is a demo response from LangGraph.
```

## 📚 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
