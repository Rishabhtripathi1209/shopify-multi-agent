import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load .env reliably
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Debug check
print("DEBUG SHOPIFY_SHOP:", os.getenv("SHOPIFY_SHOP"))

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_API_PASSWORD = os.getenv("SHOPIFY_API_PASSWORD")
SHOPIFY_SHOP = os.getenv("SHOPIFY_SHOP")
SHOPIFY_API_VERSION = os.getenv("SHOPIFY_API_VERSION", "2024-01")

def fetch_orders():
    try:
        url = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_API_PASSWORD}@{SHOPIFY_SHOP}/admin/api/{SHOPIFY_API_VERSION}/orders.json"
        params = {
            "limit": 50,
            "status": "any",
            "fields": "id,created_at,processed_at,financial_status,fulfillment_status,line_items,total_price,cancelled_at"
        }
        response = requests.get(url, params=params, verify=False)
        response.raise_for_status()
        return response.json().get("orders", [])
    except Exception as e:
        return [{"error": str(e)}]
