class shop_product:
    def __init__(self,id,name,price,stock_quantity,buy_amount=None):
        self._id = id
        self._name = name
        self._price = price
        self._stock_quantity = stock_quantity
        self._buy_amount = buy_amount
    def __repr__(self):
        return f'shop_product({str(self.id)},{str(self.name)},{str(self.price)},{str(self.stock_quantity)},{str(self.buy_amount)})'
    
    def __str__(self):
        return f'id: {self.id}\nname: {self.name}\nprice: {str(self.price)}\nstock quantitty: {str(self.stock_quantity)}\nbuy amount: {str(self.buy_amount)}'
        
    #getters

    @property
    def total_price(self):
        if self.buy_amount != None:
            return self.price*self.buy_amount
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def price(self):
        return self._price
    
    @property
    def stock_quantity(self):
        return self._stock_quantity
    
    @property
    def buy_amount(self):
        return self._buy_amount
    
    #setters
    @name.setter
    def name(self,new_name):
        self._name = new_name
    
    @price.setter
    def price(self,new_price):
        self._price = new_price
    
    @stock_quantity.setter
    def stock_quantity(self,new_stock_quantity):
        self._stock_quantity = new_stock_quantity
    
    @buy_amount.setter
    def buy_amount(self,value):
        self._buy_amount = value
    
    @total_price.setter
    def total_price(self,price,buy):
        if self.buy_amount != None:
            self.price = price
            self.buy_amount = buy



class Product_manager:
    def __init__(self):
        self._product_list = []
    
    @property
    def product_list(self):
        return self._product_list
    
    @product_list.setter
    def product_list(self,value):
        self._product_list = value
    
    def create_product(self,user_id):
        id = user_id
        name = str(input('Input name: '))
        price = int(input('Price per item: '))
        stock_quantity = int(input('Stock quantity: '))
        cart_item = shop_product(id,name,price,stock_quantity)
        self.product_list.append(cart_item)

    
    def show_items(self):
        total = 0
        if len(self.product_list) >0:
            for items in self.product_list:
                print('\n--------\n')
                print(
                    f'ID: {items.id}'
                    f'\nName: {items.name}'
                    f'\nPrice: {items.price}'
                    f'\nStock quantitty: {items.stock_quantity}'
                )
                if items.buy_amount != None:
                    print(f'Buy amount: {items.buy_amount}')
                if items.total_price != None:
                    total += items.total_price
            print('\n--------\n')
            if total != 0:
                print(f'Total price: {total}VND')
        else:
            print('No item available')


    def delete_items(self,user_input):
        for items in self.product_list:
            if items.name == user_input or items.id == user_input:
                self.product_list.remove(items)
                print('Item removed successfully')

    
    def buy_items(self,user_input):
        for items in self.product_list:
            if items.name == user_input or items.id == user_input:
                buy = int(input('Amount to buy: '))
                if buy <= items.stock_quantity:
                    items.buy_amount = buy
                    items.stock_quantity -= buy
                    print(f'Item bought successfully\nAmount left in stock: {items.stock_quantity}')
                else:
                    print('Buy amount exceeds stock quantity')
                
    #test
    # hello world