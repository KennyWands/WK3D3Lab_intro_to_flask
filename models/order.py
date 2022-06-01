class Order:
    def __init__(self, get_customer_name, get_order_date, get_order_quantity, get_item):
        self.name = get_customer_name
        self.order_date = get_order_date
        self.order_quantity = get_order_quantity
        self.item = get_item
