# 🔬 AI Research Assistant

An intelligent research agent built with **LangGraph** and **FastAPI** that autonomously searches Wikipedia and arXiv to answer research questions. Unlike a simple chatbot, this agent evaluates the quality of its own research and loops back to search again if the information isn't good enough — only stopping when it's confident in the answer.

---

## 🚀 Demo

Send a POST request to `/ask` with a research question and get a detailed, sourced answer back.

**Request:**
```json
{
  "question": "What are the latest breakthroughs in quantum computing?"
}
```

**Response:**
```json
{
  "answer": "Quantum computing has seen significant breakthroughs in recent years..."
}
```

---

## 🧠 How It Works

This project uses a **LangGraph agent** — not a simple pipeline. The agent has a decision loop:

```
User Question
      ↓
[Research Node] → Searches Wikipedia + arXiv
      ↓
[Decide Node] → LLM evaluates: "Is this research good enough?"
      ↓
   YES → [Answer Node] → Writes final answer → User
   NO  → [Research Node] → Searches again (max 2 iterations)
```

The key difference from a standard RAG pipeline: **the agent controls its own flow**. It can search multiple times, evaluate its findings, and only answer when it has sufficient information.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | LangGraph |
| LLM | Groq (llama-3.3-70b-versatile) |
| Search Tools | arXiv API, Wikipedia API |
| API Layer | FastAPI |
| LLM Orchestration | LangChain |
| Package Manager | uv |

---

## 📁 Project Structure

```
ai-research-assistant/
├── main.py        # FastAPI app — handles HTTP requests
├── graph.py       # LangGraph — connects nodes and defines flow
├── nodes.py       # Agent nodes — research, decide, answer
├── tools.py       # Search tools — Wikipedia and arXiv
├── state.py       # Shared state — passed between all nodes
├── .env           # API keys (not committed)
└── pyproject.toml # Dependencies managed by uv
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
```

**2. Create and activate virtual environment**
```bash
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
uv add langchain langchain-groq langchain-community langgraph arxiv wikipedia fastapi uvicorn python-dotenv
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

**5. Run the server**
```bash
uvicorn main:app --reload
```

**6. Test the API**

Open your browser at `http://127.0.0.1:8000/docs` to use the interactive Swagger UI.

---

## 📡 API Reference

### POST `/ask`

Ask a research question and get a detailed answer.

**Request Body:**
```json
{
  "question": "string"
}
```

**Response:**
```json
{
  "answer": "string"
}
```

---

## 🔑 Key Concepts

**State** — A shared dictionary passed between every node, containing the question, research results, final answer, iteration count, and stop flag.

**Nodes** — Individual functions that each do one job:
- `research_node` — searches Wikipedia and arXiv
- `decide_node` — evaluates research quality using LLM
- `answer_node` — generates the final answer

**Conditional Edges** — After `decide_node`, the graph checks if research is good enough. If yes → write answer. If no → search again.

---

## 🔮 Future Improvements

- [ ] Add more search tools (Google Scholar, PubMed)
- [ ] Stream responses in real time
- [ ] Add memory for follow-up questions
- [ ] Deploy to cloud (Railway / Render)
- [ ] Build a frontend UI

---

## 👨‍💻 Author

**Hamas** — Computer Engineering Graduate | AI Engineer in Progress

- LinkedIn: [your-linkedin]
- GitHub: [your-github]

---

## 📄 License

MIT License — feel free to use and modify.