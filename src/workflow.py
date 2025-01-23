from src.nodes import (
    categorize_query, check_inventory, compute_shipping,
    process_payment, call_model_2, call_tools_2, route_query_1
)
from src.tools import cancel_order
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode

def create_workflow():
    # Create the workflow
    workflow = StateGraph(MessagesState)
    
    # Add nodes
    workflow.add_node("RouteQuery", categorize_query)
    workflow.add_node("CheckInventory", check_inventory)
    workflow.add_node("ComputeShipping", compute_shipping)
    workflow.add_node("ProcessPayment", process_payment)
    
    # Add tool nodes
    tools_2 = [cancel_order]
    tool_node_2 = ToolNode(tools_2)
    
    workflow.add_conditional_edges(
        "RouteQuery",
        route_query_1,
        {
            "PlaceOrder": "CheckInventory",
            "CancelOrder": "CancelOrder"
        }
    )
    workflow.add_node("CancelOrder", call_model_2)
    workflow.add_node("tools_2", tool_node_2)
    
    # Define edges
    workflow.add_edge(START, "RouteQuery")
    workflow.add_edge("CheckInventory", "ComputeShipping")
    workflow.add_edge("ComputeShipping", "ProcessPayment")
    workflow.add_conditional_edges(
        "CancelOrder",
        call_tools_2,
        {
            "tools_2": "tools_2",
            "end": END
        }
    )
    workflow.add_edge("tools_2", "CancelOrder")
    workflow.add_edge("ProcessPayment", END)
    
    return workflow.compile() 