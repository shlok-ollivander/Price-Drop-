from datetime import datetime
from math import exp

MAX_DISCOUNT = 0.7


def calculate_discount(days_left, shelf_life, demand=0.5):
    if shelf_life <= 0:
        return MAX_DISCOUNT

    pct_used = 1 - (days_left / shelf_life)
    pct_used = max(0, min(1, pct_used))

    steepness = 4 * (1 - 0.6 * demand)

    discount = MAX_DISCOUNT * (1 - exp(-steepness * pct_used))
    discount = min(discount, MAX_DISCOUNT)

    return round(discount, 3)


def calculate_price(original_price, days_left, shelf_life, demand=0.5):
    discount = calculate_discount(days_left, shelf_life, demand)
    new_price = round(original_price * (1 - discount), 2)

    return {
        "original_price": original_price,
        "discount_percent": round(discount * 100, 1),
        "new_price": new_price,
        "days_until_expiry": days_left,
        "demand_score": demand,
    }


def days_between(expiry_date):
    expiry = datetime.fromisoformat(expiry_date)
    diff = expiry - datetime.now()
    days = diff.total_seconds() / 86400
    return max(days, 0)