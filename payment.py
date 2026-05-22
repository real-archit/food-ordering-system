import time


def payment_gateway(cart, total):
    
    print("\n==============================")
    print("        💳 PAYMENT              ")
    print("==============================")
    print(f"Amount to Pay: ₹{total}\n")
    
    while True:
        
        perm = input("Press 1 to checkout: ")

        if perm == '1':
            break

        else:
            print("❌ Invalid input.")
            continue

    while True:

        print("\nOptions:")
        print("--------------------")
        print("1. I have paid")
        print("2. Cancel payment\n")


        choice = input("Enter choice: ").strip()

        if choice == "1":
            confirm = input("Confirm payment completed? (y/n): ").strip().lower()

            if confirm == "y":
                print("\n⏳ Verifying payment...")
                time.sleep(1.5)

                
                print("✅ Payment Successful!")
                return "PAID"
                break
                
            
            else:
                print("⚠️ Payment not confirmed. Returning to options.")

        elif choice == "2":
            print("❌ Payment cancelled.")
            return "FAILED"
        