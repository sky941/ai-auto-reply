from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI(title="JKDS WhatsApp Business Support")

def handle_message(message: str) -> str:
    msg = message.strip().lower()

    if msg in ["hi", "hello", "start"]:
        return (
            "👋 *Welcome to JKDS Business Support*\n"
            "How can we assist you today?\n\n"
            "1️⃣ About JKDS\n"
            "2️⃣ Services Overview\n"
            "3️⃣ Contact & Offices\n"
            "4️⃣ Request a Consultation\n\n"
            "Reply with a number."
        )

    elif msg == "1":
        return (
            "📌 *About JKDS*\n"
            "JKDS is a professional services firm offering\n"
            "taxation, corporate advisory, accounting,\n"
            "audit and compliance support to businesses."
        )

    elif msg == "2":
        return (
            "📋 *Our Services*\n"
            "• Registrations & Licences\n"
            "• Audit & Assurance Services\n"
            "• Compliance Services\n"
            "• Advisory & Management Support\n"
            "• Tax Assessments & Litigation Help"
        )

    elif msg == "3":
        return (
            "📍 *Contact & Offices*\n"
            "Noida Office: D-85, Sector-63, Noida, UP 201301\n"
            "Delhi Office: S-505 School Block, Shakarpur, Delhi\n"
            "📞 +91 8826479697\n"
            "✉️ info@cajkds.com"
        )

    elif msg == "4":
        return (
            "🗓 *Request a Consultation*\n"
            "Please send:\n"
            "• Your Name\n"
            "• Business Name\n"
            "• Contact Details\n"
            "• Brief Query"
        )

    return "❓ Please type *Hi* to start."

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    message = form.get("Body", "")

    reply_text = handle_message(message)

    response = MessagingResponse()
    response.message(reply_text)

    return PlainTextResponse(str(response))
