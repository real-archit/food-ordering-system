menu = [
    {"id": 1, "name": "Masala Dosa", "price": 250, "category": "main_course", "available": True},
    {"id": 2, "name": "Shahi Paneer", "price": 290, "category": "main_course", "available": True},
    {"id": 3, "name": "Veg Biryani", "price": 180, "category": "main_course", "available": True},
    {"id": 4, "name": "Jeera Rice", "price": 150, "category": "main_course", "available": True},
    {"id": 5, "name": "Gulab Jamun", "price": 90, "category": "dessert", "available": True}
    
]

def display_menu(menu):
    print("\n=============================")
    print("            Menu             ")
    print("=============================\n")
    print(f"{'Id':<4} {'Name':<25} {'Price':>7}")
    print("--------------------------------------")

    for item in menu:
        if item["available"]:
            print(f"{item['id']:<4} {item['name']:<25} ₹{item['price']:<5}")
        else:
            print(f"{item['id']:<4} {item['name']:<25} {'OUT OF STOCK':>13}")
