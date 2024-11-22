def beauti_time_arg(time: str):
    value = int(time[:-1])
    unit = time[-1]

    units = {
        "d": ("день", "дня", "дней"),
        "h": ("час", "часа", "часов"),
        "m": ("минута", "минуты", "минут"),
    }

    if unit not in units:
        raise ValueError("Неподдерживаемая единица времени. Используйте 'd', 'h', 'm'.")

    word_forms = units[unit]
    if value % 10 == 1 and value % 100 != 11:
        word = word_forms[0]
    elif 2 <= value % 10 <= 4 and not (12 <= value % 100 <= 14):
        word = word_forms[1]
    else:
        word = word_forms[2]

    # Формируем итоговую строку
    return f"{value} {word}"