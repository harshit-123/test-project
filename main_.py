from typing import TypedDict
from langgraph.graph import StateGraph, END

class GraphState(TypedDict):
    message: str
    question: str

def welcome(state: GraphState) -> dict:
    state['message'] = "Hello Good Morning."
    return stat

def question(state: GraphState) -> dict:
    state['question'] = "How are you?"
    return state

def display(state: GraphState) -> dict:
    print(state['message'])
    print(state['question'])
    return {}

graph = StateGraph(GraphState)

graph.add_node("welcome", welcome)
graph.add_node("question", question)
graph.add_node("display", display)

graph.set_entry_point("welcome")
graph.add_edge("welcome", "question")   
graph.add_edge("question", "display")  
graph.add_edge("display", END)

app = graph.compile()

final_state = app.invoke({})
