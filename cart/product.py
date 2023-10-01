class Product:
    def __init__(self, product_id, name, price, quantity_in_stock, quantity_to_buy, image_url, description, rating):
        self.product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock
        self._quantity_to_buy = quantity_to_buy
        self._image_url = image_url
        self._description = description
        self._rating = rating

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        self._quantity_in_stock = value

    @property
    def quantity_to_buy(self):
        return self._quantity_to_buy

    @quantity_to_buy.setter
    def quantity_to_buy(self, value):
        self._quantity_to_buy = value

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
