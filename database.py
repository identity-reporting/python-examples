



def get_item_from_db(item_id):
    if not item_id:
        raise Exception("Item ID should be present.")
    
    return dict(
        id = item_id,
        name = f"Item No.{item_id}"
    )

def get_customer_cart(customer_id):
    if not customer_id:
        raise Exception("Customer ID should be present.")
    
    return dict(
        id = customer_id,
        name = f"Customer {customer_id}",
        items = []
    )