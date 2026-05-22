def get_user_order(menu):
  
    cust_order = input("Enter item ID (0 to exit): ").strip()
    
    if not cust_order.isdigit():
        print("-----------------------------------------")
        print("❌ Invalid input. Please enter a number.")
        print("-----------------------------------------")
        return get_user_order(menu)
    
    item_id = int(cust_order)

    if item_id == 0:
        return None
    
    
    item = next((dish for dish in menu if dish['id'] == item_id), None)
        
    if item is None:
        print("------------------------------")
        print("❌ Item not found. Try again.")
        print("------------------------------")
        return get_user_order(menu)
        return get_user_order(menu)
    if not item['available']:
        print("-------------------------")
        print("⚠️ Item is out of stock.")
        print("-------------------------")
        return get_user_order(menu)
        
    else:
        print("----------------------------------------------------")
        print(f"✅ You selected: {item['name']} (₹{item['price']})")
        print("----------------------------------------------------")
        return item

