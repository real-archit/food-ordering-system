orders = []


def print_order_line(char="-", length=52):
    print(char * length)


def save_order(cart, total):
    order_items = []

    for item in cart:
        order_items.append({
            "id": item["id"],
            "name": item["name"],
            "qty": item["qty"],
            "price": item["price"],
        })

    order = {
        "order_id": len(orders) + 1,
        "items": order_items,
        "total": total,
        "status": "PAID",
    }
    orders.append(order)
    return order


def display_order(order):
    print("\n=============================")
    print("          Your Order         ")
    print("=============================\n")
    print(f"Order ID: {order['order_id']}")
    print(f"Status: {order['status']}\n")
    print(f"{'Id':<4} {'Name':<25} {'Qty':>5} {'Price':>7} {'Total':>8}")
    print_order_line()

    for item in order["items"]:
        item_total = item["price"] * item["qty"]
        print(
            f"{item['id']:<4} "
            f"{item['name']:<25} "
            f"{item['qty']:>5} "
            f"Rs.{item['price']:<4} "
            f"Rs.{item_total:<5}"
        )

    print_order_line()
    print(f"{'Grand Total':>43}: Rs.{order['total']}")


def view_orders():
    if not orders:
        print("--------------------------")
        print("No paid orders available.")
        print("--------------------------")
        return

    for order in orders:
        display_order(order)
