from fastapi import FastAPI, HTTPException
from orchestrator import run_all_agents

app = FastAPI()

@app.get("/analyze")
def analyze():
    try:
        return run_all_agents()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
