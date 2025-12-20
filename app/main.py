from fastapi import FastAPI, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from app.whatsapp import handle_message

app = FastAPI()

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()

    from_number = form.get("From").replace("whatsapp:", "")
    to_number = form.get("To").replace("whatsapp:", "")
    message = form.get("Body", "")

    print("📩 From:", from_number)
    print("📲 To (Client):", to_number)
    print("💬 Message:", message)

    reply_text = handle_message(from_number, to_number, message)

    twiml = MessagingResponse()
    twiml.message(reply_text)

    return Response(content=str(twiml), media_type="application/xml")