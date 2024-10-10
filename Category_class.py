#el category logical class
import json
class category :

    def __init__(self):

        self.__items = {}
        self.loaddata()
        #momken n5lih ye3ml load lel items men el file
    def Add_item(self, type, path, name, price,brand,modelyear):

        self.__items[type].append({'name':name ,'price':"$"+price,'path':path,'brand':brand,'model year':modelyear})
        self.witedata()
    def sort_name(self):
        newm={}
        for i in list(self.__items.keys()) :
            newm.update({i:self.quick_sort_name(self.__items[i])})
        return newm

    def sort_price(self):
        newm = {}
        for i in list(self.__items.keys()) :
            newm.update({i:self.quick_sort_price(self.__items[i])})
        return newm

    def sort_modelyear(self):
        newm = {}
        for i in list(self.__items.keys()) :
            newm.update({i:self.quick_sort_year(self.__items[i])})
        return newm


    def quick_sort_year(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]['model year']
            pivot=int(pivot)

            left = []
            middle = []
            right = []

            for x in arr:
                l=int(x['model year'])
                if l < pivot:
                    left.append(x)
                elif l == pivot:
                    middle.append(x)
                else:
                    right.append(x)

            return self.quick_sort_year(left) + middle + self.quick_sort_year(right)


    def sort_brand(self):
        newm = {}
        for i in list(self.__items.keys()) :
            newm.update({i:self.quick_sort_brand(self.__items[i])})
        return newm
    def quick_sort_brand(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]['brand']
            pivot = pivot.lower()

            left = []
            middle = []
            right = []

            for x in arr:
                l = x['brand'].lower()
                if l < pivot:
                    left.append(x)
                elif l == pivot:
                    middle.append(x)
                else:
                    right.append(x)

            return self.quick_sort_brand(left) + middle + self.quick_sort_brand(right)



    def quick_sort_name(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]['name']
            pivot=pivot.lower()

            left = []
            middle = []
            right = []

            for x in arr:
                l=x['name'].lower()
                if l < pivot:
                    left.append(x)
                elif l == pivot:
                    middle.append(x)
                else:
                    right.append(x)

            return self.quick_sort_name(left) + middle + self.quick_sort_name(right)

    def quick_sort_price(self, arr) :
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]['price']
            pivot=float(pivot.replace('$', ''))
            print(pivot)
            left = []
            middle = []
            right = []

            for x in arr:
                l = float(x['price'].replace('$', ''))
                print(l)
                if l < pivot:
                    left.append(x)
                elif l == pivot:
                    middle.append(x)
                else:
                    right.append(x)
            return self.quick_sort_price(left) + middle + self.quick_sort_price(right)
    def sort_pricedec(self):
        newm = {}
        for i in list(self.__items.keys()) :
            newm.update({i:self.quick_sort_pricedec(self.__items[i])})
        return newm



    def quick_sort_pricedec(self, arr) :
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]['price']
            pivot=float(pivot.replace('$', ''))
            print(pivot)
            left = []
            middle = []
            right = []

            for x in arr:
                l = float(x['price'].replace('$', ''))
                print(l)
                if l > pivot:
                    left.append(x)
                elif l == pivot:
                    middle.append(x)
                else:
                    right.append(x)
            return self.quick_sort_pricedec(left) + middle + self.quick_sort_pricedec(right)

    def get_items (self) :
        self.loaddata()
        return self.__items

    def search(self, target_name):

        for category, items in list(self.__items.items()):
            sorted_items = self.quick_sort_name(items)
            result = self.binary_search(sorted_items, target_name)
            if result != -1 :
                return [result,category]
            return -1







    def binary_search(self, sorted_items ,target_name):

        low, high = 0, len(sorted_items) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_name = sorted_items[mid]['name'].lower()

            if mid_name == target_name.lower():
                return sorted_items[mid]
            elif mid_name.lower() < target_name.lower():
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def update_item(self,type,dict,new):
        index=-1
        for i in range(len(self.__items[type])):
            if (self.__items[type][i]['name'] == dict['name'] and
                    self.__items[type][i]['price'] == dict['price'] and
                    self.__items[type][i]['path'] == dict['path'] and
                    self.__items[type][i]['brand'] == dict['brand'] and
                    self.__items[type][i]['model year'] == dict['model year']):
                index = i
                break
        print(index)
        print(dict)
        print(new)
        self.__items[type][index] = new
        self.witedata()
    def loaddata(self):
        file=open("items.json","r")
        data=json.load(file)
        self.__items=data
        print(self.__items)
        file.close()

    def witedata(self):
        file = open("items.json", "w")
        json.dump(self.__items, file, indent=2)

        file.close()

    def send(self,dict):   #ya5od b3d el sale
        self.__items=dict
        self.witedata()

    def removeitem(self,type,dict):
        self.loaddata()
        self.__items[type].remove(dict)
        self.witedata()
    def increase(self,price):
        self.loaddata()

        for category, item_list in self.__items.items():
            for item in item_list:
                oldprice = item['price'].replace('$', '')
                new_price = float(oldprice) + float(price)
                if(new_price<0):
                    new_price=0.0
                item['price'] = f'$ {new_price}'
        self.witedata()













        

