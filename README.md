# 🧠 Shopify Multi-Agent Order Analyzer

This project is a multi-agent system powered by OpenAI and FastAPI that analyzes Shopify order data to identify inefficiencies, errors, and opportunities for bundling. It supports both **real-time Shopify integration** and **mock data simulation** for testing.

---

## 🚀 Features

- 🔍 **Shipping Delay Detector** — flags orders that are processed but not fulfilled
- ⚠️ **Order Error Analyzer** — identifies reasons behind cancelled orders
- 🛒 **Bundle Suggester** — finds frequently co-purchased items to suggest bundles
- 🔄 Toggle between **real Shopify API** and **mock data**
- 🧪 Toggle between **real OpenAI** and **mock LLM output**
- ⚡ FastAPI backend with a single `/analyze` endpoint
- ✅ Easily testable with or without live data

---

## 🔧 Folder Structure

```
shopify_multi_agent/
├── Services/
│   ├── shopify_client.py         # Real Shopify API integration
│   └── create_mock_data.py       # Mock order data
├── agents/
│   ├── delay_detector.py
│   ├── error_analyzer.py
│   ├── bundle_suggester.py
├── llm_utils.py                  # OpenAI + Mock toggle
├── orchestrator.py              # Core agent runner
├── main.py                      # FastAPI app
├── .env                         # Local secrets (ignored in Git)
├── .gitignore
└── README.md
```

---

## 🧪 `.env` Setup

Create a `.env` file in the root directory with this structure:

```env
# Shopify API (only needed for real data mode)
SHOPIFY_API_KEY=your_shopify_api_key
SHOPIFY_API_PASSWORD=your_shopify_password
SHOPIFY_SHOP=your-store.myshopify.com
SHOPIFY_API_VERSION=2024-01

# OpenAI
OPENAI_API_KEY=your_openai_key

# Toggle features
USE_MOCK_LLM=true  # set to false to use real OpenAI
```

---

## 🔄 Switch Between Real and Mock Modes

| Feature         | Setting                      |
|----------------|------------------------------|
| Use mock LLM    | `USE_MOCK_LLM=true` in `.env` |
| Use mock orders | Edit `orchestrator.py` to use `generate_mock_orders()` |

---

## 🚀 Run the App

Make sure dependencies are installed:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then open in your browser:

```
http://127.0.0.1:8000/analyze
```

Or visit interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## ✅ Example Response

```json
{
  "shipping_delays": "Order #101 may be delayed due to lack of fulfillment update...",
  "order_errors": "Order #102 was cancelled due to inventory mismatch...",
  "bundle_suggestions": "Wireless Mouse + USB-C Hub are frequently co-ordered..."
}
```

---

## 📦 Future Improvements

- HTML dashboard or React frontend
- Email/PDF reporting of analysis
- Agent-to-agent coordination logic
- Slack/Teams alerts integration

---

## 📜 License

MIT License © 2025 Rishabh Tripathi