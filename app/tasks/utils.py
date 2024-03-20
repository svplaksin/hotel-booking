def plural_days(n: int) -> str:
    """Склонение день/дня/дней"""
    days = ['день', 'дня', 'дней']

    if n % 10 == 1 and n % 100 != 11:
        return f"{n} {days[0]}"
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return f"{n} {days[1]}"
    else:
        return f"{n} {days[2]}"
