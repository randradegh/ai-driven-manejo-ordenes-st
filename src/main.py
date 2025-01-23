import os
from dotenv import load_dotenv
from src.workflow import create_workflow
from IPython.display import display, Image

def main():
    # Load environment variables
    load_dotenv()
    
    # Create the workflow
    agent = create_workflow()
    
    # Test cancel order
    print("\nTesting Cancel Order:")
    user_query = "I wish to cancel order_id 223"
    for chunk in agent.stream(
        {"messages": [("user", user_query)]},
        stream_mode="values",
    ):
        chunk["messages"][-1].pretty_print()
    
    # Test place order
    print("\nTesting Place Order:")
    user_query = "customer_id: customer_14 : I wish to place order for item_51 with order quantity as 4 and domestic"
    for chunk in agent.stream(
        {"messages": [("user", user_query)]},
        stream_mode="values",
    ):
        chunk["messages"][-1].pretty_print()

if __name__ == "__main__":
    main() 