from app.faq_engine import get_faq_reply

def handle_message(from_number: str, to_number: str, message: str):
    # SANDBOX MODE: client is sender
    client_id = f"client_{from_number[-10:]}"

    reply = get_faq_reply(client_id, message)

    if reply:
        return reply

    return "Thanks for your message 🙏 We’ll get back to you shortly."
