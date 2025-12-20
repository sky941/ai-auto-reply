import json

def load_faq(client_id):
    with open(f"data/faqs/{client_id}.json") as f:
        return json.load(f)

def get_faq_reply(client_id, message):
    faqs = load_faq(client_id)
    msg = message.lower()

    for faq in faqs:
        for keyword in faq["keywords"]:
            if keyword in msg:
                return faq["answer"]

    return None
