from llm_utils import ask_openai

def analyze_order_errors(orders):
    print("DEBUG [error_analyzer] received:", orders)

    if not orders or not isinstance(orders, list):
        return "No order errors or cancellations found."

    cancelled_orders = [o for o in orders if o.get("cancelled_at")]

    if not cancelled_orders:
        return "No order errors or cancellations found."

    prompt = (
        "These orders were cancelled. Analyze the possible causes based on order data and suggest prevention strategies:\n\n"
        f"{cancelled_orders}"
    )

    return ask_openai(prompt)
