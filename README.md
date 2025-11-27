# LangGraph & LangChain Demo Project

This project demonstrates how to use LangGraph and LangChain to build powerful LLM applications. It includes two main demos:

1. **LangGraph Demo**: Shows how to create stateful, multi-actor applications with complex workflows
2. **LangChain Demo**: Demonstrates basic LLM chaining and prompt templating

## 🚀 Features

### LangGraph Demo
- **State Management**: Manage conversation state across multiple turns
- **Workflow Design**: Create complex, multi-step LLM workflows
- **Node-based Architecture**: Break down applications into modular components

### LangChain Demo
- **LLM Chaining**: Connect multiple LLM calls in sequence
- **Prompt Templating**: Create dynamic prompts with variables
- **Easy Integration**: Works with OpenAI's GPT models

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

### LangGraph Demo
```bash
python langgraph_demo.py
```

### LangChain Demo
1. Create a `.env` file with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```
2. Run the demo:
   ```bash
   python langchain_demo.py
   ```

## 🏗️ Project Structure

- `langgraph_demo.py`: LangGraph workflow demonstration
- `langchain_demo.py`: LangChain chaining and templating demo
- `requirements.txt`: Project dependencies
- `README.md`: This documentation file

## 🤖 How It Works

### LangGraph Demo
Implements a workflow with three nodes:
1. **Retrieve**: Fetches relevant information
2. **Generate**: Processes information to generate a response
3. **Update State**: Maintains conversation history

### LangChain Demo
Shows how to:
1. Initialize LLM models
2. Create and use prompt templates
3. Chain multiple operations together
4. Handle model responses

## 🧪 Example Outputs

### LangGraph Demo Output
```
Node 'retrieve':
  Output: {'retrieved_docs': ['LangGraph is a library...']}
--------------------------------------------------
Node 'generate':
  Output: {'generation': 'You asked: ...'}
```

### LangChain Demo Output
```
Q: What is LangChain?
A: LangChain is a framework...
--------------------------------------------------
Q: How does LangChain help with LLM applications?
A: LangChain provides tools...
```

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

### LangGraph
- [Documentation](https://langchain-ai.github.io/langgraph/)
- [GitHub](https://github.com/langchain-ai/langgraph)

### LangChain
- [Documentation](https://python.langchain.com/)
- [GitHub](https://github.com/langchain-ai/langchain)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
