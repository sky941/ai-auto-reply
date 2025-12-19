import json
from pathlib import Path

CLIENTS_DIR = Path("data/clients")

def load_client_by_phone_number_id(phone_number_id: str):
    for file in CLIENTS_DIR.glob("*.json"):
        with open(file, "r") as f:
            client = json.load(f)
            if client["phone_number_id"] == phone_number_id:
                return client
    return None
