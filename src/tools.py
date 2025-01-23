from langchain_core.tools import tool
from src.config import llm
from langchain.prompts import ChatPromptTemplate

@tool
def cancel_order(query: str) -> dict:
    """Simulate order cancelling"""
    prompt = ChatPromptTemplate.from_template("""
        Extract the order_id from this text and return it as a JSON object.
        Text: {text}
        Rules:
        - The order_id should be a string
        - If you see a number after "order_id" or "order", that's the order_id
        - Return format must be exactly: {{"order_id": "223"}} (with the actual number)
        - Do not include any other text in your response, only the JSON object
    """)
    
    result = llm.invoke(prompt.format(text=query))
    print("\nLLM Response:", result.content)
    try:
        import json
        data = json.loads(result.content)
        print("Parsed JSON:", data)
        order_id = data.get("order_id")
        print("Order ID:", order_id)
    except Exception as e:
        print("JSON Parse Error:", str(e))
        return {"error": "Could not parse order_id"}

    if not order_id:
        return {"error": "Missing 'order_id'."}

    return {"order_status": "Order stands cancelled"} 