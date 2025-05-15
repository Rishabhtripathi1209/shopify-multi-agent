from llm_utils import ask_openai

def analyze_shipping_delays(orders):
    print("DEBUG [delay] received:", orders)

    if not orders or not isinstance(orders, list):
        return "No orders provided to analyze shipping delays."

    delayed_orders = [o for o in orders if o.get("processed_at") and not o.get("fulfillment_status")]

    if not delayed_orders:
        return "No shipping delays detected."

    prompt = (
        "You're an expert in Shopify logistics. The following orders were processed "
        "but remain unfulfilled. Analyze and explain possible reasons for delay and "
        "recommend process improvements:\n\n"
        f"{delayed_orders}"
    )

    return ask_openai(prompt)
