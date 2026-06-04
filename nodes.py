from state import ResearchState
from tools import search_arxiv, search_wikipedia
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def research_node(state: ResearchState):
    question = state["question"]
    wiki_results = search_wikipedia(question)
    arxiv_results = search_arxiv(question)
    return {"research": [wiki_results, arxiv_results], "iterations": state["iterations"] + 1}

llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

def decide_node(state: ResearchState):
    research = state["research"]
    finalresearch = "\n".join(research)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant. You are given a research to write an answer, say yes if the research is good enough to write the answer, otherwise say no"),
        ("human", "{finalresearch}")
    ])
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({
        "finalresearch": finalresearch
    })

    if response.lower().startswith("yes"):
        return {"stop": True}
    else:
        return {"stop": False}

def answer_node(state: ResearchState):
    research = state["research"]
    question = state["question"]
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Write a detailed answer based on the give research: {research}"),
        ("human", "{question}")
    ])

    finalresearch = "\n".join(research)

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "research": finalresearch,
        "question": question
    })
    return {"answer": response}



