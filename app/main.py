from fastapi import FastAPI
from app.webhook import router

app = FastAPI(title="WhatsApp Auto Reply SaaS")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "Backend running successfully"}
