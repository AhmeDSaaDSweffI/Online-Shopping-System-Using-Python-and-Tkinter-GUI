import json
from stack import Stack
from cart_logic import CartLogic


class USER :

    current=-1
    def __init__(self):
        self.object=CartLogic()

        self.__users= {}
        self.loaddata()
        self.st=Stack()

    def register (self,name,phone,mail,gender,governorate,password,age,nationalid) :
        self.loaddata()
        if name.isnumeric() == False:
            if phone.isnumeric() :
               if gender.lower() == "male" or gender.lower() == "female" :
                   if governorate.isnumeric() == False:
                       if age.isnumeric():
                           if nationalid.isnumeric and len(nationalid) == 14 :
                               if nationalid not in self.__users.keys() :
                                    self.__users[nationalid]=({'name' :name,'phone' :phone,'mail' :mail ,'gender' :gender ,"governorate":governorate,'password':password,'age':age,'nationalid':nationalid})
                                    self.object.prepare(nationalid) #yeb3at lel cart el id yegahez mkan fel file
                                    self.write_data()
                                    USER.current = nationalid
                                    return "ADDED"
                               else :
                                   return "duplicate info"

                           else :
                               return "wrong National id"

                       else :
                           return "wrong age"
                   else :
                       return "wrong governorate"

               else :
                   return "wrong gender"
            else:
                return "wrong phone number"

    def login(self, mail, password):
        self.loaddata()
        for nationalid, user_data in self.__users.items():
            if user_data['mail'].strip().lower() == mail.strip().lower():
                if user_data['password'] == password:
                    USER.current = nationalid
                    return "Done"
                else:
                    return "wrong pass"
        return "wrong mail"

    def write_data(self):
        with open("data1.json", "w") as file:
            json.dump(self.__users, file)

    def loaddata(self):
        file = open("data1.json", "r")
        data = json.load(file)
        self.__users = data
       # print(self.users)
        file.close()



    def go_to_page(self,type):
        self.st.push(type)

    def go_back (self) :
        if self.st.isEmpty() :
            return -1
        res= self.st.peek()

        return res
    def pop(self) :
        self.st.pop()

    def size(self):
        return self.st.stacksize()

    def get_current(self):
        return USER.current
onj=USER()
#print(onj.get_current())




