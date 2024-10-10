import tkinter as tk
from Category_class import category
from tkinter import messagebox
from tkinter import ttk

from cart_gui import CartGUI
from cart_logic import CartLogic
from USERE import USER



class MyApp:
    place = {
        'sports': [0, 0],
        'fashion': [0, 0],
        'electronics': [0, 0],
        'home': [0, 0],
        'books': [0, 0]
    }
    lol = category()
    ob = CartLogic()
    # beta3t el stack ely gowa el user
   # print(USER.current, "aaaaa")

    forgo = USER()
    def __init__(self):
        self.items = self.lol.get_items()
        self.place = {
            'sports': [0, 0],
            'fashion': [0, 0],
            'electronics': [0, 0],
            'home': [0, 0],
            'books': [0, 0]
        }
        self.images=[]
        self.bg_color = '#ffffff'
        self.button_color = "#3b5998"
        self.button_text_color = '#ffffff'
        self.highlight_color = "#ffffff"

        self.root = tk.Tk()
        self.root.title("USER MAIN WINDOW")
        self.root.geometry("1555x1000")
        self.root.configure(bg=self.bg_color)



        self.nb = ttk.Notebook(self.root)
        self.nb.pack(fill='both', expand=True, padx=10, pady=10)

        self.f1 = self.create_tab("Fashion", "f1")
        self.f2 = self.create_tab("Sports", "f2")
        self.f3 = self.create_tab("Electronics", "f3")
        self.f4 = self.create_tab("Home", "f4")
        self.f5 = self.create_tab("Books", "f5")

        for category, item_list in self.items.items():
             for item in item_list:
                 button = self.Add_item(category, item['path'], item['name'], item['price'], item["brand"],
                                           item["model year"])



        go_button = tk.Button(self.root, text="Cart", font=('Helvetica', 14, 'bold'), bg=self.button_color, fg=self.button_text_color, relief='raised', command=self.GoToCart)
        go_button.place(x=1400, y=20, width=100, height=40)

        back_button = tk.Button(self.root, text="Back", font=('Helvetica', 14, 'bold'), bg=self.button_color, fg=self.button_text_color, relief='raised', command=self.back)
        back_button.place(x=1300, y=20, width=100, height=40)

        self.submit_button = tk.Button(self.root, text="Sort", font=('Helvetica', 12, 'bold'), bg=self.button_color,
                                       fg=self.button_text_color, relief='raised', command=self.sortbyprice)
        self.submit_button.place(x=670, y=800, width=80, height=40)

        self.search_button = tk.Button(self.root, text="Search", font=('Helvetica', 12, 'bold'), bg=self.button_color,
                                       fg=self.button_text_color, relief='raised', command=self.searchh)
        self.search_button.place(x=670, y=750, width=80, height=40)

        self.search_entry = tk.Entry(self.root, font=('Helvetica', 12))
        self.search_entry.place(x=770, y=755, width=220, height=30)

        self.choices = ["name", "price dec", "price inc", "brand name", "model year"]
        self.selectedValue = tk.StringVar()
        self.dropDownMenu = ttk.Combobox(self.root, values=self.choices, textvariable=self.selectedValue,
                                         font=('Helvetica', 12))
        self.selectedValue.set(self.choices[0])
        self.dropDownMenu.place(x=770, y=805, width=170, height=30)

        self.nb.bind("<<NotebookTabChanged>>", self.tofront)



        self.root.mainloop()



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
            "height": 125,
            "relief": "flat",
            "activebackground": "#4caf50",
            "activeforeground": "white"
        }

        if type == "sports":
            button = tk.Button(self.f2, text=name + "\n" +brand+" "+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['sports'][0], column=self.place['sports'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['sports'][1] += 1
            if self.place['sports'][1] > 2:
                self.place['sports'][1] = 0
                self.place['sports'][0] += 1
            return button

        elif type == "fashion":
            button = tk.Button(self.f1, text=name + "\n" +brand+" "+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['fashion'][0], column=self.place['fashion'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['fashion'][1] += 1
            if self.place['fashion'][1] > 2:
                self.place['fashion'][1] = 0
                self.place['fashion'][0] += 1
            return button

        elif type == "electronics":
            button = tk.Button(self.f3, text=name + "\n" +brand+" "+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['electronics'][0], column=self.place['electronics'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['electronics'][1] += 1
            if self.place['electronics'][1] > 2:
                self.place['electronics'][1] = 0
                self.place['electronics'][0] += 1
            return button

        elif type == "home":
            button = tk.Button(self.f4, text=name + "\n" +brand+" "+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['home'][0], column=self.place['home'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['home'][1] += 1
            if self.place['home'][1] > 2:
                self.place['home'][1] = 0
                self.place['home'][0] += 1
            return button

        elif type == "books":
            button = tk.Button(self.f5, text=name + "\n" +brand+" "+str(modelyear)+ "\n"+str(price), image=image, compound='bottom', **button_style)
            button.grid(row=self.place['books'][0], column=self.place['books'][1], padx=10, pady=10, sticky='nsew')
            button.config(command=lambda item=item: self.button_clicked(item, type))
            self.place['books'][1] += 1
            if self.place['books'][1] > 2:
                self.place['books'][1] = 0
                self.place['books'][0] += 1
            return button

    def create_tab(self, tab_text, frame_name):
        frame = tk.Frame(self.nb, bg='white')
        setattr(self, frame_name, frame)
        self.nb.add(frame, text=tab_text)

        button_frame = tk.Frame(frame, bg='white')
        button_frame.pack(fill='both', padx=20, pady=20)
        button_frame.columnconfigure([0, 1, 2], weight=1)
        return button_frame

    def sortbyprice(self):
        self.root.destroy()
        item = self.selectedValue.get()
        selected_index = self.choices.index(item)

        from sorteddd import sorte
        sorte(selected_index)

    def tofront(self,event=None):
        selected_tab = self.nb.index(self.nb.select())

        if selected_tab == 0:
            self.forgo.go_to_page("fashion")
            print(selected_tab)


        elif selected_tab == 1:
            self.forgo.go_to_page("sports")
            print(selected_tab)
        elif selected_tab == 2 :
            self.forgo.go_to_page("electronics")
            print(selected_tab)
        elif selected_tab ==3 :
            self.forgo.go_to_page("home")
            print(selected_tab)
        elif selected_tab ==4 :
            self.forgo.go_to_page("books")
            print(selected_tab)
    def back(self):
        if self.forgo.size()>1 :
            self.forgo.pop()
            res=self.forgo.go_back()

            print(res)
            if res==-1 :
                messagebox.showerror("NO BACK", "YOU CAN'T GO BACK")
                return
            if res == "fashion":
                self.nb.select(0)
                self.forgo.pop()
            elif res == "sports":
                self.nb.select(1)
                self.forgo.pop()
            elif res == "electronics":

                self.nb.select(2)
                self.forgo.pop()
            elif res =="home" :

                self.nb.select(3)
                self.forgo.pop()
            elif res =="books" :
                print(res)
                self.nb.select(4)
                self.forgo.pop()
        else:
            messagebox.showerror("NO BACK", "YOU CAN'T GO BACK")

    def button_clicked(self, item,type):
        print(self.forgo.get_current())
        self.ob.add_item(item,self.forgo.get_current())

    def searchh(self):
        s=self.search_entry.get()
        s=s.strip().lower()
        print(s)
        if not s:
            messagebox.showwarning("Input Error", "Sale value cannot be empty!")
            return
        obj=category()
        res=obj.search(s)
        if res != -1 :
            self.root.destroy()
            from SHOWONE import Show
            objec=Show(res[1],res[0])
        else:
            messagebox.showerror("Input Error", "NOT FOUND ENTER IT AGAIN")
            return
    def GoToCart (self) :
        self.root.destroy()
        CartGUI()












#MyApp()











