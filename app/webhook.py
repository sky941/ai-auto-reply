from fastapi import APIRouter, Request
from app.client_loader import load_client_by_phone_number_id
from app.faq_engine import get_reply

router = APIRouter()

@router.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    # Meta WhatsApp Cloud API structure
    value = data["entry"][0]["changes"][0]["value"]
    phone_number_id = value["metadata"]["phone_number_id"]
    message_text = value["messages"][0]["text"]["body"]

    client = load_client_by_phone_number_id(phone_number_id)
    if not client:
        return {"status": "client not found"}

    reply = get_reply(message_text, client)
    if not reply:
        reply = client["default_reply"]

    # For now just log the reply
    print("Reply:", reply)

    return {"status": "ok"}
