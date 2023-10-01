class CartManager:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        for item in self.cart:
            if item.product.product_id == product.product_id:
                if item.product.quantity_in_stock < quantity:
                    print("Không đủ số lượng sản phẩm trong kho.")
                    return
                item.quantity += quantity
                item.product.quantity_in_stock -= quantity
                return
        if product.quantity_in_stock < quantity:
            print("Không đủ số lượng sản phẩm trong kho.")
            return
        self.cart.append(CartItem(product, quantity))
        product.quantity_in_stock -= quantity

    def remove_from_cart(self, product_id):
        for item in self.cart:
            if item.product.product_id == product_id:
                item.product.quantity_in_stock += item.quantity
                self.cart.remove(item)
                return

    def display_cart(self):
        if not self.cart:
            print("Giỏ hàng của bạn trống.")
        else:
            print("Giỏ hàng của bạn:")
            total_price = 0
            for item in self.cart:
                total_item_price = item.product.price * item.quantity
                total_price += total_item_price
                print(f"=====================")
                print(f"Tên sản phẩm: {item.product.name}")
                print(f"ID sản phẩm: {item.product.product_id}")
                print(f"Giá: {item.product.price} VND")
                print(f"Số lượng: {item.quantity}")
                print(f"Tổng cộng: {total_item_price} VND")
                print(f"=====================")
                print()

            print(f"Tổng giá trị đơn hàng: {total_price} VND")

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
