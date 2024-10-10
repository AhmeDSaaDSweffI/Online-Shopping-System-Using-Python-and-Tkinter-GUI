import tkinter as tk
from tkinter import ttk
from Category_class import category
from tkinter import messagebox

class Remove:
    lol = category()

    def __init__(self):
        self.items = self.lol.get_items()
        self.place = {
            'sports': [0, 0],
            'fashion': [0, 0],
            'electronics': [0, 0],
            'home': [0, 0],
            'books': [0, 0]
        }
        self.root = tk.Tk()
        self.root.title("Remove Items")
        self.root.geometry("1555x1000")
        self.root.config(bg="white")


        self.images=[]


        self.header_frame = tk.Frame(self.root, bg="#3b5998", height=80)
        self.header_frame.pack(fill='x')

        self.header_label = tk.Label(self.header_frame, text="Remove Items from Categories",
                                     font=('Georgia', 20, 'bold'), bg="#3b5998", fg="white", pady=20)
        self.header_label.pack()

        # Notebook
        self.nb = ttk.Notebook(self.root)
        self.nb.pack(fill='both', expand=True, padx=10, pady=10)


        self.f1 = self.create_tab("Fashion", "f1")
        self.f2 = self.create_tab("Sports", "f2")
        self.f3 = self.create_tab("Electronics", "f3")
        self.f4 = self.create_tab("Home", "f4")
        self.f5 = self.create_tab("Books", "f5")


        for category, item_list in self.items.items():
            for item in item_list:
                button = self.Add_item(category, item['path'], item['name'], item['price'], item["brand"], item["model year"])


        admin_button = tk.Button(self.root, text="OPTIONS", font=('Georgia', 12, 'bold'), bg="#4caf50", fg="white",
                                 relief="flat", command=self.gohome)
        admin_button.place(x=700, y=500)

        self.lol.loaddata()
        messagebox.showinfo("GUIDE", "Press on any item to remove it.")

        self.root.mainloop()

    def create_tab(self, tab_text, frame_name):
        frame = tk.Frame(self.nb, bg='white')
        setattr(self, frame_name, frame)
        self.nb.add(frame, text=tab_text)

        button_frame = tk.Frame(frame, bg='white')
        button_frame.pack(fill='both', padx=20, pady=20)
        button_frame.columnconfigure([0, 1, 2], weight=1)
        return button_frame

    def Add_item(self, type, path, name, price, brand, modelyear):
        image = tk.PhotoImage(file=path)
       # image = tk.PhotoImage(file=path).subsample(4, 4)
        item = {'name': name, 'price': price, 'path': path, 'brand': brand, 'model year': modelyear}
        self.images.append(image)

        button_style = {
            "font": ('Georgia', 12, 'bold'),
            "bg": "#3b5998",
            "fg": "white",
            "width": 30,
            "height": 105,
            "relief": "flat",
            "activebackground": "#4caf50",
            "activeforeground": "white"
        }

        if type == "sports":
            button = tk.Button(self.f2, text=name + " " +brand+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['sports'][0], column=self.place['sports'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['sports'][1] += 1
            if self.place['sports'][1] > 2:
                self.place['sports'][1] = 0
                self.place['sports'][0] += 1
            return button

        elif type == "fashion":
            button = tk.Button(self.f1, text=name + " " +brand+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['fashion'][0], column=self.place['fashion'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['fashion'][1] += 1
            if self.place['fashion'][1] > 2:
                self.place['fashion'][1] = 0
                self.place['fashion'][0] += 1
            return button

        elif type == "electronics":
            button = tk.Button(self.f3, text=name + " " +brand+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['electronics'][0], column=self.place['electronics'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['electronics'][1] += 1
            if self.place['electronics'][1] > 2:
                self.place['electronics'][1] = 0
                self.place['electronics'][0] += 1
            return button

        elif type == "home":
            button = tk.Button(self.f4, text=name + " " +brand+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['home'][0], column=self.place['home'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['home'][1] += 1
            if self.place['home'][1] > 2:
                self.place['home'][1] = 0
                self.place['home'][0] += 1
            return button

        elif type == "books":
            button = tk.Button(self.f5, text=name + " " +brand+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['books'][0], column=self.place['books'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['books'][1] += 1
            if self.place['books'][1] > 2:
                self.place['books'][1] = 0
                self.place['books'][0] += 1
            return button



    def gohome(self):
        self.root.destroy()
        from LoginPage import AdminOptions
        AdminOptions()

    def button_clicked(self, item, type):
        self.root.destroy()
        print(f"{item}  {type}")
        from AdminOptions import Admin
        obj = Admin()
        obj.removeItem(item, type)
        from LoginPage import AdminOptions
        AdminOptions()

#Remove()
