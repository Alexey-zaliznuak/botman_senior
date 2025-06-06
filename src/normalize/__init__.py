from normalize.settings import NORMALIZE_KEYWORD


def normalize_string(t: str) -> str:
    t = ''.join(t.lower().split())

    for base_symbol, norm_symbol in NORMALIZE_KEYWORD.items():
        t = t.replace(base_symbol, norm_symbol)

    return t

def bulk_normalize(data: list[str]) -> list[str]:
    data = set(data)
    new = []

    for el in data:
        new.append(normalize_string(el))

    return list(new)
