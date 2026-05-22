# 🍽️ Food Ordering System

A terminal-based food ordering application built with Python that lets users browse a menu, manage a cart, process payments, and track order history — all from the command line.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Menu](#menu)
- [How It Works](#how-it-works)
- [Known Issues & Improvements](#known-issues--improvements)

---

## ✨ Features

- 📜 Browse a categorized food menu with availability status
- 🛒 Add items to cart with automatic quantity management
- 💳 Checkout with a simulated payment gateway
- 🧾 View detailed order summaries with item-wise totals
- 📦 Track all past paid orders in a session
- ❌ Remove items from cart
- 🔁 Handles duplicate item additions by incrementing quantity

---

## 📁 Project Structure

```
food-ordering-system/
│
├── main.py          # Entry point; main menu loop and flow control
├── menu.py          # Menu data and display logic
├── cart.py          # Cart operations (add, view, remove)
├── order.py         # User input handling for item selection
├── payment.py       # Simulated payment gateway
└── view_order.py    # Order saving, display, and history
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies — uses only the Python standard library

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/food-ordering-system.git

# Navigate into the project directory
cd food-ordering-system

# Run the application
python main.py
```

---

## 🖥️ Usage

On launch, you'll see the main menu:

```
=============================
    Food Ordering System
=============================

1. Order Food
2. View Cart
3. View Orders
4. Exit
```

| Option | Description |
|--------|-------------|
| **1. Order Food** | Displays the menu and prompts for an item ID to add to your cart |
| **2. View Cart** | Shows all cart items with quantities and totals; proceed to checkout or add more |
| **3. View Orders** | Lists all successfully paid orders in the current session |
| **4. Exit** | Exits the application |

### Placing an Order

1. Select **Order Food** from the main menu
2. Browse the displayed menu
3. Enter the **Item ID** of your desired dish (`0` to go back)
4. The item is added to your cart (or its quantity is increased if already present)
5. Go to **View Cart** to checkout

### Checkout Flow

1. View your cart to confirm items
2. Choose to add more or proceed to payment
3. Confirm payment in the simulated payment gateway
4. A detailed order receipt is displayed upon success

---

## 🍛 Menu

| ID | Item | Category | Price |
|----|------|----------|-------|
| 1 | Masala Dosa | Main Course | ₹250 |
| 2 | Shahi Paneer | Main Course | ₹290 |
| 3 | Veg Biryani | Main Course | ₹180 |
| 4 | Jeera Rice | Main Course | ₹150 |
| 5 | Gulab Jamun | Dessert | ₹90 |

---

## ⚙️ How It Works

```
main.py
  ├── menu.py        →  Displays available items
  ├── order.py       →  Validates and captures user item selection
  ├── cart.py        →  Manages cart state (add / view / remove)
  ├── payment.py     →  Simulates payment confirmation flow
  └── view_order.py  →  Saves and displays order history
```

- **Cart state** is maintained as an in-memory list throughout the session.
- **Orders** are stored in a session-level list and cleared on exit (no persistent storage).
- **Payment** is simulated — no real transaction occurs.

---

## 🐛 Known Issues & Improvements

| Area | Issue / Suggestion |
|------|--------------------|
| `order.py` | Duplicate `return get_user_order(menu)` after item not found check |
| `payment.py` | Unreachable `break` after `return "PAID"` |
| Data persistence | Orders and cart reset on every run; consider adding JSON/SQLite storage |
| Menu management | Menu items are hardcoded; an admin interface could allow dynamic updates |
| Remove from cart | `remove_item()` is defined in `cart.py` but not yet exposed in the main menu |
| Input validation | Cart removal and payment flows could benefit from stronger input validation |

---

## 📄 License

This project is open source.
