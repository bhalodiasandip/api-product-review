from typing import Dict
from dataclasses import dataclass

@dataclass
class Conversation:
    step: str # one of: start, waiting_product, waiting_name, waiting_review, done
    product_name: str = ""
    user_name: str = ""

# contact -> Conversation
CONVS: Dict[str, Conversation] = {}

def handle_incoming(contact: str, text: str):
    text = (text or "").strip()
    conv = CONVS.get(contact)

    # start new conversation if none
    if not conv:
        conv = Conversation(step="waiting_product")
        CONVS[contact] = conv
        return ("Which product is this review for?", None)

    # If waiting for product name
    if conv.step == "waiting_product":
        conv.product_name = text
        conv.step = "waiting_name"
        return (f"What's your name?", None)


    if conv.step == "waiting_name":
        conv.user_name = text
        conv.step = "waiting_review"
        return (f"Please send your review for {conv.product_name}.", None)


    if conv.step == "waiting_review":
        conv_review = text
        # prepare payload
        payload = {
            "contact_number": contact,
            "user_name": conv.user_name,
            "product_name": conv.product_name,
            "product_review": conv_review,
        }
        # clear conversation
        CONVS.pop(contact, None)
        reply = f"Thanks {payload['user_name']} -- your review for {payload['product_name']} has been recorded."
        return (reply, payload)

    # fallback
    CONVS.pop(contact, None)
    return ("Which product is this review for?", None)