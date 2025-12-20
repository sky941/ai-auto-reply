from app.faq_engine import get_faq_reply, load_client


def handle_message(client_id, message):
    client = load_client(client_id)
    msg = message.lower().strip()

    if msg == "menu":
        return client["menu_message"]

    if msg in client["menu"]:
        return client["menu"][msg]

    reply = get_faq_reply(client_id, msg)
    if reply:
        return reply

    return client["default_reply"]
