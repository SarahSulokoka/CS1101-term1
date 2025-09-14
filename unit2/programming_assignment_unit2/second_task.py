def calculate_price(items):
    
    # Calculate the total price for a purchase based on item combinations and applicable discounts.
    
    # Parameters:
    # items (list): A list of integers representing items purchased (1, 2, and/or 3)
    
    # Returns:
    # float: The total price after applying applicable discounts
    
    # Define individual item prices
    prices = {1: 200.0, 2: 400.0, 3: 600.0}
    
    # Count how many of each item is in the purchase
    item_counts = {1: items.count(1), 2: items.count(2), 3: items.count(3)}
    
    # Calculate base price without any discounts
    base_price = sum(prices[item] for item in items)
    
    # Check if all three items are present (gift pack)
    if all(count >= 1 for count in item_counts.values()):
        # Calculate how many complete gift packs we can form
        gift_packs = min(item_counts.values())
        
        # Calculate price for gift packs (25% discount)
        gift_price = gift_packs * (prices[1] + prices[2] + prices[3]) * 0.75
        
        # Remove the items used in gift packs
        remaining_items = []
        for item, count in item_counts.items():
            remaining_items.extend([item] * (count - gift_packs))
        
        # Calculate price for remaining items
        remaining_price = calculate_price(remaining_items)
        
        return gift_price + remaining_price
    
    # Check if any two-item combos can be formed
    elif (item_counts[1] >= 1 and item_counts[2] >= 1) or \
         (item_counts[1] >= 1 and item_counts[3] >= 1) or \
         (item_counts[2] >= 1 and item_counts[3] >= 1):
        
        # Find which two-item combo can be formed
        if item_counts[1] >= 1 and item_counts[2] >= 1:
            combo_items = (1, 2)
        elif item_counts[1] >= 1 and item_counts[3] >= 1:
            combo_items = (1, 3)
        else:
            combo_items = (2, 3)
        
        # Form one two-item combo (10% discount)
        combo_price = (prices[combo_items[0]] + prices[combo_items[1]]) * 0.9
        
        # Remove the items used in the combo
        remaining_items = items.copy()
        remaining_items.remove(combo_items[0])
        remaining_items.remove(combo_items[1])
        
        # Calculate price for remaining items
        remaining_price = calculate_price(remaining_items)
        
        return combo_price + remaining_price
    
    # If no combos can be formed, return base price (no discount)
    else:
        return base_price

def generate_catalog():
    """
    Generate the online store catalog with all individual items and combinations.
    """
    print("Online Store")
    print("----------------------")
    print("Product(S)\tPrice")
    
    # Individual items
    print("Item 1\t\t200.0")
    print("Item 2\t\t400.0")
    print("Item 3\t\t600.0")
    
    # Two-item combos
    print("Combo 1(Item 1 + 2)\t540.0")
    print("Combo 2(Item 2 + 3)\t900.0")
    print("Combo 3(Item 1 + 3)\t720.0")
    
    # Gift pack (all three items)
    print("Combo 4(Item 1 + 2 + 3)\t900.0")
    print("\nFor delivery Contact:98764678899")

# Generate and display the catalog
generate_catalog()