def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Get user input and display results
try:
    # Get input from user
    original_price = float(input("Enter the original price of the item: $"))
    discount = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount)

    # Display message based on whether discount was applied
    if discount >= 20:
        print(f"\nDiscount of {discount}% applied!")
        print(f"Original price: ${original_price:.2f}")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"\nNo discount was applied. Price remains: ${final_price:.2f}")
        print(f"Note: Minimum 20% discount required to apply discount.")

except ValueError:
    print("Please enter valid numeraical values for price and discount percentage.")