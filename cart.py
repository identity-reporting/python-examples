from database import get_customer_cart, get_item_from_db



def add_item_to_customer_cart(customer_id, item_id):
    '''
        Given the item id and customer id, creates the cart if it doesn't exist,
        add the item to cart, returns the whole cart object as dictionary.
    '''

    # Get Customer's Cart
    try:

        customer_cart = get_customer_cart(customer_id)

        if not customer_cart:
            raise Exception((
                f"Controller did not return the cart for Customer {customer_id}. "
                f"This may be a problem with our database service. "
                f"Please Try again later."
            ))
        
    except Exception as e:
        return dict(
            http_status = 500,
            error = str(e)
        )

    # Add Item To Cart
    try:
        item_to_add = get_item_from_db(item_id)
        if not item_to_add:
            raise Exception((
                f"Controller did not return the item against item id {item_id}. "
                f"Invalid item ID."
            ))
        customer_cart["items"].append(
            item_to_add
        )
    except Exception as e:
        return dict(
            http_status = 500,
            error = str(e)
        )
    
    # Return cart data
    return dict(
        http_status = 200,
        data = customer_cart
    )
