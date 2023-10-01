from product import Product
from cart import CartManager, CartItem

def create_sample_products():
    # Tạo các sản phẩm mẫu
    product1 = Product(1, "Sản phẩm 1", 100, 10, 0, "image1.jpg", "Mô tả sản phẩm 1", 4.5)
    product2 = Product(2, "Sản phẩm 2", 50, 20, 0, "image2.jpg", "Mô tả sản phẩm 2", 4.0)
    product3 = Product(3, "Sản phẩm 3", 75, 15, 0, "image3.jpg", "Mô tả sản phẩm 3", 3.8)
    
    return [product1, product2, product3]

def main():
    cart_manager = CartManager()
    
    # Tạo danh sách các sản phẩm mẫu và thêm chúng vào giỏ hàng
    sample_products = create_sample_products()
    for product in sample_products:
        cart_manager.add_to_cart(product, 1)
    
    while True:
        print("\nChương trình Quản lý Giỏ hàng")
        print("1. Hiển thị Giỏ hàng")
        print("2. Thêm sản phẩm vào Giỏ hàng")
        print("3. Xóa sản phẩm khỏi Giỏ hàng")
        print("4. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            cart_manager.display_cart()
        elif choice == '2':
            product_id = int(input("Nhập ID sản phẩm: "))
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm (VND): "))
            quantity_in_stock = int(input("Nhập số lượng sản phẩm trong kho: "))
            quantity_to_buy = int(input("Nhập số lượng sản phẩm muốn mua: "))
            image_url = input("Nhập URL ảnh sản phẩm: ")
            description = input("Nhập mô tả sản phẩm: ")
            rating = float(input("Nhập đánh giá của người tiêu dùng: "))
            
            product = Product(product_id, name, price, quantity_in_stock, quantity_to_buy, image_url, description, rating)
            cart_manager.add_to_cart(product, quantity_to_buy)
            print("Sản phẩm đã được thêm vào Giỏ hàng!")
        elif choice == '3':
            product_id = int(input("Nhập ID sản phẩm để xóa: "))
            cart_manager.remove_from_cart(product_id)
            print("Sản phẩm đã được xóa khỏi Giỏ hàng!")
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
