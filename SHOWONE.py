import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from cart_gui import CartGUI
from cart_logic import CartLogic
from USERE import USER


class Show:
    def __init__(self, item_type, item_dict):
        self.root = tk.Tk()
        self.root.title("SHOW ONE ITEM")
        self.root.geometry("1555x1000")
        self.root.config( bg='#ffffff')

        self.item_dict = item_dict
        self.item_type = item_type

        self.titleFrame = tk.Frame(self.root, bg='#3b5998')
        self.titleFrame.pack(fill='x')
        title_label = tk.Label(self.titleFrame, text="Item Details", font=('Georgia', 20, 'bold'), fg='white',
                               bg='#3b5998')
        title_label.pack(pady=10)

        self.itemFrame = tk.Frame(self.root, bg='#ffffff', relief='solid', bd=2)
        self.itemFrame.pack(fill='both', padx=20, pady=0)

        self.Add_item(self.item_type, self.item_dict['path'], self.item_dict['name'], self.item_dict['price'],
                      self.item_dict['brand'], self.item_dict['model year'])
        self.label = tk.Label(self.root, text="Press the item to add it to the cart", font=('Georgia', 12, 'italic'),
                              bg='#ffffff')
        self.label.pack(pady=0)


        buttonFrame = tk.Frame(self.root, bg='#f0f0f0')
        buttonFrame.pack( pady=20)
        back_button = tk.Button(buttonFrame, text="Back", font=('Georgia', 12, 'bold'), bg='#3b5998', fg='white',
                                width=10, command=self.back)
        back_button.grid(row=0, column=0, padx=10)


        go_button = tk.Button(buttonFrame, text="Go to Cart", font=('Georgia', 12, 'bold'), bg='#3b5998', fg='white',
                              width=10,command=self.GoToCart)
        go_button.grid(row=0, column=1, padx=10)

        messagebox.showinfo("GUIDE", "PRESS ON ANY ITEM TO ADD IT TO CART")

        self.root.mainloop()

    def Add_item(self, item_type, path, name, price, brand, modelyear):

        image = PhotoImage(file=path)
        image_frame = tk.Frame(self.itemFrame, bg='#ffffff')
        image_frame.pack(pady=20)
        item = {'name': name, 'price': price, 'path': path, 'brand': brand, 'model year': modelyear}


        button_text = f"{name}\n{brand} {modelyear}\n{price}"
        button = tk.Button(image_frame, text=button_text, font=('Georgia', 12, 'bold'), image=image, compound='top',
                           bg='#f9f9f9', bd=2, relief='raised')
        button.config(command=lambda item=item: self.button_clicked(item, type))
        button.pack(padx=10, pady=10, fill='both')

        details_label = tk.Label(image_frame, text=f"Name: {name}\nPrice: {price}", font=('Georgia', 14, 'italic'),
                                 bg='#ffffff', fg='#3b5998')
        details_label.pack(pady=(10, 0))
        self.image = image



    def GoToCart(self):
        self.root.destroy()
        CartGUI()

    def back(self):
        self.root.destroy()
        from userGUI import MyApp
        MyApp()
    def button_clicked(self, item,type):
        self.ob.add_item(item, self.forgo.get_current())








