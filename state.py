from typing import TypedDict

class ResearchState(TypedDict):
    question: str
    answer: str
    research: list[str]
    stop: bool
    iterations: int