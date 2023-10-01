from da_cart import shop_product,Product_manager

def input_check(user_input):
    for items in bought.product_list:
        if items.id == user_input or items.name == user_input:
            return True
    return False    

bought = Product_manager()
def main():
    item_1 = shop_product('1','item_1',75,6)
    item_2 = shop_product('2','item_2',100,8)
    bought.product_list.append(item_1)
    bought.product_list.append(item_2)
    
    while True:
        print()
        print(
            '---Cart management program---'
            '\n1. Add item to cart'
            '\n2. Show items in cart '
            '\n3. Delete item from cart'
            '\n4. Buy item'
            '\n5. Exit'
        )

        choice = int(input('Input your choice: '))
        if choice == 1:
            id = str(input('Product id: '))
            if input_check(id):
                print('ID already exists')
                continue
            else:
                Product_manager.create_product(bought,id)
            print(bought.product_list)

        elif choice == 2:
            Product_manager.show_items(bought)

        elif choice == 3:
            item_to_delete = str(input('Name or id of item to delete: '))
            if input_check(item_to_delete):
                Product_manager.delete_items(bought,item_to_delete)
            else:
                print('Invalid name or id')

        elif choice == 4:
            user_input = str(input('Name or id you want to buy: '))
            if input_check(user_input):
                Product_manager.buy_items(bought,user_input)
            else:
                print('Invalid name or ID')
        elif choice == 5:
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()

#test