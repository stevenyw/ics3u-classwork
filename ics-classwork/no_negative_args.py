# The error is a ValueError, it says it can't be negative, on line 20, and it happened because item_price was 0.
# I see "price can't be negative", but not quantity can't be negative, because it checked for price first.

def main():
    item_price = -2.99
    quantity = -3
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")


def calc_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.

    Returns:
        The subtotal
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")
        
    if quantity < 0:
        raise ValueError("Quantity can't be negative!")

    return price * quantity



if __name__ == "__main__":
    main()
