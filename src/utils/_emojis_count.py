import emoji


def emojis_count(text: str):
    return len([char for char in text if char in emoji.EMOJI_DATA])
