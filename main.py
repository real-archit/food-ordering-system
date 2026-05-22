from cart import add_to_cart, cart, view_cart
from menu import display_menu, menu
from order import get_user_order
from payment import payment_gateway
from view_order import display_order, save_order, view_orders


def print_banner():
    print("=============================")
    print("    Food Ordering System     ")
    print("=============================")


def show_main_menu():
    print("\n1. Order Food")
    print("2. View Cart")
    print("3. View Orders")
    print("4. Exit\n")


def calculate_total(items):
    return sum(item["price"] * item["qty"] for item in items)


def handle_order_food():
    display_menu(menu)
    print()

    item = get_user_order(menu)
    if item is None:
        print("Exited")
        return

    add_to_cart(cart, item)


def handle_view_cart():
    if not cart:
        view_cart(cart)
        return

    view_cart(cart)

    while True:
        add_more = input("Add more items? (y/n): ").strip().lower()

        if add_more == "y":
            return

        if add_more == "n":
            total = calculate_total(cart)
            payment_status = payment_gateway(cart, total)

            if payment_status == "PAID":
                order = save_order(cart, total)
                cart.clear()
                display_order(order)

            return

        print("--------------------------")
        print("Enter valid input.")
        print("--------------------------")


def handle_view_orders():
    view_orders()


def main():
    print_banner()

    while True:
        show_main_menu()
        customer_action = input("Enter your choice: ").strip()

        if customer_action == "1":
            handle_order_food()
        elif customer_action == "2":
            handle_view_cart()
        elif customer_action == "3":
            handle_view_orders()
        elif customer_action == "4":
            print("----------------------------")
            print("Thank you for visiting :)")
            print("----------------------------")
            break
        else:
            print("-----------------------")
            print("Enter valid input.")
            print("-----------------------")


if __name__ == "__main__":
    main()
