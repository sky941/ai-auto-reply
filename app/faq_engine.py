import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAQ_DIR = os.path.join(BASE_DIR, "data", "faqs")


def load_client(client_id):
    """
    Loads client JSON config
    """
    path = os.path.join(FAQ_DIR, f"client_{client_id}.json")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Client config not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_faq_reply(client_id, message):
    client = load_client(client_id)

    for faq in client.get("faqs", []):
        for keyword in faq.get("keywords", []):
            if keyword.lower() in message.lower():
                return faq["answer"]

    return None
