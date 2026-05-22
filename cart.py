cart = [ ]

def print_line(char="-", length=41):
    print(char * length)

def add_to_cart(cart, item):
    for c in cart:
        if c['id'] == item['id']:
            c['qty'] += 1
            print_line()
            print(f"🔁 Increased quantity of {item['name']}")
            print_line()
            return
    
    cart.append({
        'id': item['id'],
        'name': item['name'],
        'qty': 1,
        'price': item['price']
    })

def view_cart(cart):
    if not cart:
        print_line(length=17)
        print("🛒 Cart is empty")
        print_line(length=17)
        return
    
    total = 0
    for item in cart:
        item_total = item['price'] * item['qty']
        total += item_total
        print_line(char="-", length=52)
        print(f"{item['name']} | Qty: {item['qty']} | ₹{item_total}")
    
    print_line(char="-", length=52)
    print(f"💵 Total: ₹{total}")

def remove_item(cart, item_id):
    for item in cart:
        if item['id'] == item_id:
            cart.remove(item)
            print("🗑️ Item removed from cart")
            return
        
        
        
