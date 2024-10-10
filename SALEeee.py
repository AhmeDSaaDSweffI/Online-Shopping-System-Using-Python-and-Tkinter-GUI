import tkinter as tk
from tkinter import messagebox, PhotoImage
import tkinterClass as obj
from Category_class import category
from AdminOptions import Admin

class MakeSale:
    def __init__(self):
        self.ob = category()
        self.root = tk.Tk()
        self.root.title("Make Sale")
        self.root.configure(bg='#ffffff')
        self.root.geometry("1555x10000")

        self.top_frame = tk.Frame(self.root, bg="#3b5998", height=80)
        self.top_frame.pack(fill='x')

        self.title_label = tk.Label(self.top_frame, text="Make a Sale", font=('Georgia', 24, 'bold'), bg="#3b5998",
                                    fg="white")
        self.title_label.pack(pady=20)

        self.form_frame = tk.Frame(self.root, bg='#ffffff')
        self.form_frame.pack(pady=40)

        self.sale_frame = tk.Frame(self.form_frame, bg='#ffffff')
        self.sale_frame.grid(row=0, column=0, pady=20)

        self.icon_sale = tk.Canvas(self.sale_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.sale_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\sale.png")
        self.icon_sale.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_sale.create_image(25, 25, anchor='center', image=self.sale_image)
        self.icon_sale.pack(side='left', padx=5)

        self.label = tk.Label(self.sale_frame, text="Enter Sale Value:", font=('Arial', 14), bg='#ffffff', fg="#333333")
        self.label.pack(side='left', padx=5)

        self.sale_entry = tk.Entry(self.sale_frame, font=('Arial', 14), width=20, bd=2, relief='solid')
        self.sale_entry.pack(side='left', padx=5)

        self.submit_button = tk.Button(self.form_frame, text="Submit", font=('Arial', 14, 'bold'), bg="#3b5998", fg="white", width=10, command=self.submit_sale)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=20)

        self.bottom_frame = tk.Frame(self.root, bg='#ffffff')
        self.bottom_frame.pack(fill='x', pady=10)

        admin_button = tk.Button(self.bottom_frame, text="Admin Options", font=('Arial', 12, 'bold'), bg="#3b5998", fg="white", width=15, command=self.gohome)
        admin_button.pack()

        self.root.mainloop()

    def submit_sale(self):
        sale_value = self.sale_entry.get()
        if not sale_value:
            messagebox.showwarning("Input Error", "Sale value cannot be empty!")
            return

        try:
            sale_value = float(sale_value)
            self.update_items(sale_value)
            messagebox.showinfo("Sale Submitted", f"Sale value of {sale_value} submitted!")
            self.root.destroy()
            obj.MyApp()


        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return

    def gohome(self):
        messagebox.showinfo("Admin Options", "This button would take you to admin options.")
        self.root.destroy()

    def update_items(self, sale_value):
        adm = Admin()
        adm.add_discount(sale_value)

        items = self.ob.get_items()

        for category, item_list in items.items():
            for item in item_list:
                price = item['price'].replace('$', '')
                new_price = float(price) - sale_value
                if (new_price < 0):
                    new_price = 0.0
                item['price'] = f'$ {new_price}'

        self.ob.send(items)  # yeb3at el items lel category


#MakeSale()


