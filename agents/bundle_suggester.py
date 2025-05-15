from llm_utils import ask_openai

def suggest_bundles(orders):
    print("DEBUG [bundle_suggester] received:", orders)

    if not orders or not isinstance(orders, list):
        return "No orders available for bundle suggestion."

    all_line_items = [item for order in orders for item in order.get("line_items", [])]

    if not all_line_items:
        return "No product line items found for bundle suggestion."

    prompt = (
        "Analyze the following product line items from different orders. "
        "Suggest bundles or frequently bought together recommendations:\n\n"
        f"{all_line_items}"
    )

    return ask_openai(prompt)
