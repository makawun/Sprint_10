def extract_price_number(raw: str) -> str:
    return "".join(ch for ch in raw if ch.isdigit())