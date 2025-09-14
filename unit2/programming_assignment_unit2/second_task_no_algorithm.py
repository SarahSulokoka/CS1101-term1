def calculate_price(items):
    
    # Calculate the total price for items with discounts for combos
    # items: list of item numbers (1, 2, or 3)
    # returns: total price after discounts
    
    # Prices for each item
    price1 = 200.0
    price2 = 400.0
    price3 = 600.0
    
    # Count how many of each item
    count1 = items.count(1)
    count2 = items.count(2)
    count3 = items.count(3)
    
    total = 0
    
    # First apply gift pack discount (all 3 items)
    while count1 >= 1 and count2 >= 1 and count3 >= 1:
        total += (price1 + price2 + price3) * 0.75  # 25% discount
        count1 -= 1
        count2 -= 1
        count3 -= 1
    
    # Then apply two-item combo discounts
    # Combo 1: Item 1 + 2
    while count1 >= 1 and count2 >= 1:
        total += (price1 + price2) * 0.9  # 10% discount
        count1 -= 1
        count2 -= 1
    
    # Combo 2: Item 2 + 3
    while count2 >= 1 and count3 >= 1:
        total += (price2 + price3) * 0.9  # 10% discount
        count2 -= 1
        count3 -= 1
    
    # Combo 3: Item 1 + 3
    while count1 >= 1 and count3 >= 1:
        total += (price1 + price3) * 0.9  # 10% discount
        count1 -= 1
        count3 -= 1
    
    # Add any remaining individual items (no discount)
    total += count1 * price1
    total += count2 * price2
    total += count3 * price3
    
    return total

def generate_catalog():
    
    # Display the store catalog with prices
   
    print("Online Store")
    print("----------------------")
    print("Product(S)\tPrice")
    print("Item 1\t\t200.0")
    print("Item 2\t\t400.0")
    print("Item 3\t\t600.0")
    print("Combo 1(Item 1 + 2)\t540.0")
    print("Combo 2(Item 2 + 3)\t900.0")
    print("Combo 3(Item 1 + 3)\t720.0")
    print("Combo 4(Item 1 + 2 + 3)\t900.0")
    print("\nFor delivery Contact: 98764678899")

# Display the catalog
generate_catalog()