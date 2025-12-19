def get_reply(message: str, client: dict) -> str | None:
    msg = message.lower().strip()

    # Greeting
    if msg in ["hi", "hello", "hey"]:
        return client["greeting"]

    # Menu options
    if msg in client["menu"]:
        return client["menu"][msg]

    # Keyword based FAQ
    for faq in client["faqs"]:
        for keyword in faq["keywords"]:
            if keyword in msg:
                return faq["answer"]

    return None
