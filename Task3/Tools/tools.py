from agents import RunContextWrapper,Agent,function_tool

ORDER_DB = {"123": "Shipped", "456": "Processing", "789": "Delivered"}

# Function for is enabled
def is_order_query(ctx: RunContextWrapper, agent) -> bool:
    text = str(ctx.context.get("input", "")).lower()  
    return any(k in text for k in ["order", "status"])

# function tool with is_enabled and error_function
@function_tool(is_enabled=is_order_query)
def get_order_status(order_id: str) -> str:
    """Fetches the order status from fake database"""
    print("get order tool fired >>>>>>")
    status = ORDER_DB.get(order_id)
    if not status:
      
        return f"❌ Order {order_id} not found. Please check the ID again."
    return f"✅ Order {order_id} is currently {status}."
