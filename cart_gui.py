import tkinter as tk
from tkinter import ttk
from cart_logic import CartLogic  # Import the CartLogic class
from USERE import USER
from tkinter import messagebox

class CartGUI:



    def __init__(self):
        self.place = [0, 0]
        self.logic = CartLogic()
        self.obj=USER()
        self.cart = tk.Tk()
        self.cart_frame = tk.Frame(self.cart)
        self.cart.title("Shopping Cart")
        self.cart.geometry("1100x1100")

        ######################################################
        self.f1 = tk.Frame(self.cart, bg='lightgrey')
        self.f1.pack(fill='both', padx=20, pady=20)

        self.buttonFrame = tk.Frame(self.f1, bg='lightgrey')
        self.buttonFrame.pack(fill='both', padx=20, pady=20)
        self.buttonFrame.columnconfigure([0, 1, 2], weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)

        self.images = []

        self.category = self.obj.get_current()  #yeb3at el current natioal
        self.logic.load_data()
        items = self.logic.get_cart_items(self.category)
        back_button = tk.Button(self.cart, text="GO TO CATEGORIES",font=('Arial', 12, 'bold'),relief='raised', borderwidth=2,bg="#3b5998",fg='white', command=self.back)
        back_button.place(x=1400, y=0)


        if items is not None and len(items)>0 :

            for item in items:
                self.Add_item(item['path'], item['name'], item['price'],item['brand'],item['model year'])



########################################################################################

       # self.national_id_label = tk.Label(self.cart_frame, text="Enter National ID:", font=("arial", 16))
        #self.national_id_label.grid(row=0, column=0, pady=20)
        #self.national_id_entry = tk.Entry(self.cart_frame, font=("arial", 16))
       #self.national_id_entry.grid(row=0, column=1, pady=20)


           # self.show_items_button = tk.Button(self.cart_frame, text="Show Items", font=("arial", 16), command=self.show_items)
           # self.show_items_button.grid(row=0, columnspan=2, pady=20)

           # self.show_items_button = tk.Button(self.cart_frame, text="Show Items", font=("Arial", 16), bg="#3b5998",
                                   #       fg='white', command=self.show_items)
            #self.show_items_button.grid(row=0, columnspan=2, pady=20)

            #self.cart_listbox = tk.Listbox(self.cart_frame,width=60, height=15, font=("Arial", 16))
            #self.cart_listbox.grid(row=2, columnspan=2, pady=20)

            self.calcTotal_button = tk.Button(self.cart_frame, text="Calculate Price", font=("Arial", 16), bg="#3b5998", fg="white", relief='raised', command=self.load_cart)
            self.calcTotal_button.grid(row=5, column=0, pady=20)

            self.calcTotal_button = tk.Button(self.cart_frame, text="PURCHASE", font=("Arial", 16), bg="#3b5998", fg="white", relief='raised',
                                              command=self.buy_cart)
            self.calcTotal_button.grid(row=5, column=1, pady=20)

            self.calcTotal_button = tk.Button(self.cart_frame, text="CLEAR", font=("Arial", 16), bg="#3b5998", fg="white", relief='raised',
                                              command=self.clear_cart)
            self.calcTotal_button.grid(row=5, column=2, pady=20)





            self.total_price_label = tk.Label(self.cart_frame, text="Items Price:", font=("arial", 16))
            self.total_price_label.grid(row=6, column=0, pady=20)
            self.total_price_entry = tk.Label(self.cart_frame, text="", font=("arial", 16))
            self.total_price_entry.grid(row=6, column=1, pady=20)

            self.governorate_label = tk.Label(self.cart_frame,  text="Select Governorate:", font=("Arial", 16), bg="white")
            self.governorate_label.grid(row=7, column=0, pady=20)
            self.selected_governorate = tk.StringVar(self.cart_frame)
            self.selected_governorate.set("Cairo")
            self.governorate_menu = tk.OptionMenu(self.cart_frame, self.selected_governorate, *self.logic.delivery_fees_by_governorate.keys())
            self.governorate_menu.grid(row=7, column=1, pady=20)

            self.delivery_fees_label = tk.Label(self.cart_frame, text="Delivery Fees:",  font=("Arial", 16), bg="white")
            self.delivery_fees_label.grid(row=8, column=0, pady=20)
            self.delivery_fees_entry = tk.Label(self.cart_frame, text="", font=("arial", 16))
            self.delivery_fees_entry.grid(row=8, column=1, pady=20)
            messagebox.showinfo("GUIDE", "PRESS ON ANY ITEM TO REMOVE IT FROM THE CART")

            self.cart_frame.pack()
        else :
            messagebox.showerror("Error", "NO items in the cart")
            self.back()




        self.cart.mainloop()

    def show_items(self):
        self.logic.load_data()
        national_id =self.category
        #self.cart_listbox.delete(0, tk.END)

        items = self.logic.get_cart_items(national_id)
        if items and len(items)>0:
            for item in items:
                item_details = f"{item['name']} - Price: {item['price']} - Brand: {item['brand']} - Model Year: {item['model year']}"
                #self.cart_listbox.insert(tk.END, item_details)

    def load_cart(self):
        self.logic.load_data()
        national_id = self.category
        governorate = self.selected_governorate.get()
        total_price, delivery_fees, total = self.logic.calculate_total(national_id, governorate)

        if total_price is not None:
            #self.cart_listbox.delete(0, tk.END)
            items = self.logic.get_cart_items(national_id)
            for item in items:
                item_details = f"{item['name']} - Price: {item['price']} - Brand: {item['brand']} - Model Year: {item['model year']}"
                #self.cart_listbox.insert(tk.END, item_details)

            self.total_price_entry.config(text=f"{total_price:.2f}")
            self.delivery_fees_entry.config(text=f"{delivery_fees:.2f}    Total Price: {total:.2f}")




    def Add_item(self, path, name, price,brand,modelyear):
        image = tk.PhotoImage(file=path)
        item = {'name': name, 'price': price, 'path': path,'brand':brand,'model year':modelyear}
        self.images.append(image)


        button = tk.Button(self.buttonFrame, text=f"{name} {price}", font=('Arial', 12, 'bold'), image=image,
                           compound='bottom')
        button.grid(row=self.place[0], column=self.place[1], padx=10, pady=10, sticky='nsew')
        button.config(command=lambda item=item: self.button_clicked(item))


        self.place[1] += 1
        if self.place[1] > 2:
            self.place[1] = 0
            self.place[0] += 1


        return button

    def back(self):
        self.cart.destroy()
        from userGUI import MyApp
        ob = MyApp()

    def buy_cart(self):
        self.load_cart()
        messagebox.showinfo("THANK YOU", "THANK YOU")
        self.logic.prepare(self.category)
        self.cart.destroy()
        from userGUI import MyApp
        ob = MyApp()

    def clear_cart(self):

        messagebox.showinfo("THANK YOU", "CART IS EMPTY RIGHT NOW")
        self.logic.prepare(self.category)
        self.cart.destroy()
        from userGUI import MyApp
        ob = MyApp()

    def button_clicked(self, item):
        self.logic.remove_item(item,self.category)
        messagebox.showinfo("THANK YOU", "REMOVED")
        self.cart.destroy()
        CartGUI()




#CartGUI()