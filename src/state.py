from typing import TypedDict, Optional

class State(TypedDict):
    query: str
    category: Optional[str]
    next_node: Optional[str]
    item_id: Optional[str]
    order_status: Optional[str]
    cost: Optional[str]
    payment_status: Optional[str]
    location: Optional[str]
    quantity: Optional[int] 