import re


def parse_time(time_str: str) -> int:
    match = re.match(r"(\d+)([mhd])", time_str)
    if not match:
        raise ValueError("Неправильный формат времени. Используйте m (минуты), h (часы) или d (дни).")

    value, unit = int(match.group(1)), match.group(2)

    if unit == "m":
        return value * 60
    elif unit == "h":
        return value * 3600
    elif unit == "d":
        return value * 86400
    else:
        raise ValueError("Неподдерживаемый формат времени.")
