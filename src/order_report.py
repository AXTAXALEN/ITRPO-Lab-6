def build_order_report(items, customer_name="Гость"):
    s = 0
    for item in items:
        if item.get("active", True):
            s += item["price"] * item["quantity"]
    q = 0
    for item in items:
        if item.get("active", True):
            q += item["quantity"]
    if s >= 1000:
        d = s * 0.1
    else:
        d = 0
    s = s - d
    if q > 0:
        if s >= 1000:
            delivery = 0
        else:
            delivery = 200
    else:
        delivery = 0
    result = round(s + delivery, 2)
    text = f"{customer_name}: {q} шт.; к оплате {result:.2f}"
    return {"quantity": q, "total": result, "text": text}
