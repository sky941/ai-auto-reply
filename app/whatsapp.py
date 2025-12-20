from app.faq_engine import get_faq_reply

def handle_message(from_number: str, to_number: str, message: str):
    client_id = f"client_{to_number[-10:]}"  # 7042432151 → client_7042432151

    reply = get_faq_reply(client_id, message)

    if reply:
        return reply

    return "Thanks for your message 🙏 We’ll get back to you shortly."
