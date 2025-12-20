from app.faq_engine import get_faq_reply, load_client


def handle_message(from_number, to_number, message):
    client_id = to_number.replace("whatsapp:", "").replace("+", "")
    reply = get_faq_reply(client_id, message)
    return reply
