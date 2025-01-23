import random
from typing import Literal
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState
from langgraph.graph import END
import pandas as pd
from src.tools import cancel_order
from src.config import llm

# Load data
inventory_df = pd.read_csv("data/inventory.csv")
customers_df = pd.read_csv("data/customers.csv")

# Convert to dictionaries
inventory = inventory_df.set_index("item_id").T.to_dict()
customers = customers_df.set_index("customer_id").T.to_dict()

# Add near the top of the file, after llm initialization
tools_2 = [cancel_order]
llm_with_tools_2 = llm.bind_tools(tools_2)

def categorize_query(state: MessagesState) -> MessagesState:
    """Categorize user query into PlaceOrder or CancelOrder"""
    prompt = ChatPromptTemplate.from_template(
        "Categorize user query into PlaceOrder or CancelOrder. "
        "Respond with either 'PlaceOrder' or 'CancelOrder' Query: {state}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    category = chain.invoke({"state": state}).content
    return {"query": state, "category": category}

def check_inventory(state: MessagesState) -> MessagesState:
    """Check if the requested item is in stock."""
    prompt = ChatPromptTemplate.from_template("""
        Extract the item_id and quantity from this text and return as JSON:
        {text}
        Return format: {{"item_id": "item_XX", "quantity": number}}
    """)
    
    result = llm.invoke(prompt.format(text=str(state)))
    try:
        import json
        data = json.loads(result.content)
        item_id = data.get("item_id")
        quantity = data.get("quantity")
    except:
        return {"error": "Could not parse item_id or quantity"}

    if not item_id or not quantity:
        return {"error": "Missing 'item_id' or 'quantity'."}

    if inventory.get(item_id, {}).get("stock", 0) >= quantity:
        print("IN STOCK")
        return {"status": "In Stock"}
    return {"query": state, "order_status": "Out of Stock"}

def compute_shipping(state: MessagesState) -> MessagesState:
    """Calculate shipping costs."""
    prompt = ChatPromptTemplate.from_template("""
        Extract the item_id, quantity, and customer_id from this text and return as JSON:
        {text}
        Return format: {{"item_id": "item_XX", "quantity": number, "customer_id": "customer_XX"}}
    """)
    
    result = llm.invoke(prompt.format(text=str(state)))
    try:
        import json
        data = json.loads(result.content)
        item_id = data.get("item_id")
        quantity = data.get("quantity")
        customer_id = data.get("customer_id")
    except:
        return {"error": "Could not parse order details"}

    if not all([item_id, quantity, customer_id]):
        return {"error": "Missing order details"}

    location = customers[customer_id]['location']
    weight_per_item = inventory[item_id]["weight"]
    total_weight = weight_per_item * quantity
    rates = {"local": 5, "domestic": 10, "international": 20}
    cost = total_weight * rates.get(location, 10)
    print(f"Cost: ${cost:.2f}, Location: {location}")

    return {"query": state, "cost": f"${cost:.2f}"}

def process_payment(state: MessagesState) -> MessagesState:
    """Simulate payment processing."""
    prompt = ChatPromptTemplate.from_template("""
        Extract the cost from this text and return as JSON:
        {text}
        Return format: {{"cost": "number"}}
    """)
    
    result = llm.invoke(prompt.format(text=str(state)))
    try:
        import json
        data = json.loads(result.content)
        cost = data.get("cost")
    except:
        return {"error": "Could not parse cost"}

    if not cost:
        return {"error": "Missing 'amount'."}
    
    print(f"PAYMENT PROCESSED: {cost} and order successfully placed!")
    payment_outcome = random.choice(["Success", "Failed"])
    return {"payment_status": payment_outcome}

def call_model_2(state: MessagesState):
    """Use the LLM to decide the next step."""
    messages = state["messages"]
    response = llm_with_tools_2.invoke(str(messages))
    return {"messages": [response]}

def call_tools_2(state: MessagesState) -> Literal["tools_2", "end"]:
    """Route workflow based on tool calls."""
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "tools_2"
    return "end"

def route_query_1(state: MessagesState) -> str:
    """Route the query based on its category."""
    print(state)
    if state["category"] == "PlaceOrder":
        return "PlaceOrder"
    elif state["category"] == "CancelOrder":
        return "CancelOrder" 