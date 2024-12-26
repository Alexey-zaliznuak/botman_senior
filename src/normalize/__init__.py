NORMALIZE_KEYWORD: dict[str, str] = {
    # latin to kiril
    "a": "а",
    "b": "б",
    "c": "с",
    "d": "д",
    "e": "е",
    "f": "ф",
    "g": "г",
    "h": "х",
    "i": "и",
    "j": "й",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "q": "қ",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "v": "в",
    "w": "щ",
    "x": "кс",
    "y": "ы",
    "z": "з",


    # others
    "ё": "е",
    "а": "о",
    "у": "и",


    # ЛС
    "личк": "лс",
    "личных": "лс",
}

def normalize_string(t: str) -> str:
    t = t.lower()

    for base_symbol, norm_symbol in NORMALIZE_KEYWORD.items():
        t = t.replace(base_symbol, norm_symbol)

    return t

def bulk_normalize(data: list[str]) -> list[str]:
    new = []

    for el in data:
        new.append(normalize_string(el))

    return new
