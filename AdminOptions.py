from Category_class import category
import json


# el admin logical class

class Admin :


    def __init__(self):
        self.__discounts=[]
        self.loaddiscounts()



    def Additem(self,type, path, name, price,brand,modelyear):
        if type.lower() in ["sports","fashion","Home","electronics","books"] :

          try :
                float(price)
                int(modelyear)
                if brand =="" :
                    int("no")
                if name =="" :
                    int("no")
                if path =="":
                    int("no")

                str(brand)
                str(name)
                obj = category()
                obj.Add_item(type, path, name, price,brand,modelyear)
                return "Added"
          except :
                return "invalid info"
        else :
            return "invalid type"

    def updateitem (self,type, path, name, price,dict,brand,modelyear):
        if type.lower() in ["sports", "fashion", "Home", "electronics", "books"]:
            try:
                float(price)
                int(modelyear)
                if brand =="" :
                    int("no")
                if name =="" :
                    int("no")
                if path =="":
                    int("no")

                str(brand)
                str(name)
                obj = category()
                obj.update_item(type, dict,{'name':name ,'price':"$"+price,'path':path,'brand':brand,'model year':modelyear})
                return "Edited"
            except:
                return "invalid info"
        else:
            return "invalid type"

    def loaddiscounts(self):
        file=open("discounts.json","r")
        data=json.load(file)
        self.__discounts=data

        file.close()

    def writediscounts(self):
        file = open("discounts.json", "w")
        json.dump(self.__discounts, file, indent=2)
        file.close()


    def removeItem(self,dict,type):
        obj = category()
        obj.removeitem(type, dict)
        return "Edited"

    def remove_last_discount(self):
        self.loaddiscounts()
        if len(self.__discounts)==0:
            return "THERE IS NO DISCOUNTS!!!!"
        else :
            price=self.__discounts[-1]
            obj = category()
            obj.increase(price)
            self.__discounts=self.__discounts[0:len( self.__discounts)-1]
            self.writediscounts()
            return "REMOVED"




    def add_discount(self,price):
        self.loaddiscounts()
        self.__discounts.append(price)
        self.writediscounts()







#Admin()


