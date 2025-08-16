def calculate_discount(price, discount_percent):
    """
    Calculate the final price after discount if discount_percent is 20% or higher.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if final_price < original_price:
        print(f"Discount applied. Final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
