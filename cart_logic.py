import json

class CartLogic:
    def __init__(self):
        json_file_path = 'cart.json'
        with open(json_file_path, 'r') as f:
            self.__cart_data = json.load(f)

        self.delivery_fees_by_governorate = {
            "Cairo": 20,
            "Giza": 25,
            "Alexandria": 30,
            "Luxor": 40,
            "Aswan": 50,
            "Suez": 35,
            "Ismailia": 30,
            "Hurghada": 45,
            "Sharm El-Sheikh": 60
        }

        self.__cart_items = []

    def get_cart_items(self, national_id):
        self.load_data()
        return self.__cart_data.get(national_id, None)

    def calculate_total_recursive(self, cart_items, index=0):
        if index >= len(cart_items):
            return 0
        item = cart_items[index]
        price = item['price'].replace('$', '')
        item_total = float(price)
        return item_total + self.calculate_total_recursive(cart_items, index + 1)

    def calculate_total(self, national_id, governorate):
        self.__cart_items = self.get_cart_items(national_id)
        if self.__cart_items:
            total_price = self.calculate_total_recursive(self.__cart_items)
            delivery_fees = self.delivery_fees_by_governorate.get(governorate, 50)
            total = total_price + delivery_fees
            return total_price, delivery_fees, total
        return None, None, None

    def load_data(self):
        file = open("cart.json", "r")
        data = json.load(file)
        self.__cart_data = data
        file.close()

    def witedata(self):
        file = open("cart.json", "w")
        json.dump(self.__cart_data, file, indent=2)
        file.close()

    def add_item(self, item,id):
        self.load_data()
        self.__cart_data[id].append(item)
        self.witedata()
    def prepare(self,id):   # 3shan lma ne3ml user gedid aw ne3ml buy aw ne3ml clear lel cart
        self.load_data()
        self.__cart_data[id] = []
        self.witedata()

    def remove_item(self,item,id):
        self.load_data()
        self.__cart_data[id].remove(item)
        self.witedata()



