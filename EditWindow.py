import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import PhotoImage
from AdminOptions import Admin

# el window bta3t el admin lama ye3ml edit
class Edit:
    def __init__(self,dict,type):
        self.path=0
        self.image=0
        self.value=dict
        self.cat=type
        self.path = ""
        self.img = None

        upload_photo = lambda: self.upload_photo()

        self.root = tk.Tk()
        self.root.title("My GUI Application")
        self.root.configure(bg='#ffffff')
        self.root.geometry("500x500")

        # self.label = tk.Label(self.root, text="ADD ITEM", font=('Georgia', 20), bg='#ffffff')
        # self.label.pack(pady=20, padx=20)

        self.header_frame = tk.Frame(self.root, bg="#3b5998", height=80)
        self.header_frame.pack(fill='x')

        self.header_label = tk.Label(self.header_frame, text="EDIT Item",
                                     font=('Georgia', 20, 'bold'), bg="#3b5998", fg="white", pady=20)
        self.header_label.pack()

        self.frame = tk.Frame(self.root, padx=10, pady=10, bg='#ffffff')
        self.frame.pack(padx=20, pady=10)

        self.name_frame = tk.Frame(self.frame, bg='#ffffff')
        self.name_frame.pack(pady=10)

        self.icon_name = tk.Canvas(self.name_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.name_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\new.png")
        self.icon_name.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_name.create_image(25, 25, anchor='center', image=self.name_image)
        self.icon_name.pack(side='left', padx=5)

        self.label_name = tk.Label(self.name_frame, text="Enter the item name:", bg='#ffffff', font=('Georgia', 12))
        self.label_name.pack(side='left', padx=5)

        self.entry_name = tk.Entry(self.name_frame, bg='#ffffff', font=('Georgia', 12))
        self.entry_name.pack(side='left', padx=5)

        self.price_frame = tk.Frame(self.frame, bg='#ffffff')
        self.price_frame.pack(pady=10)

        self.icon_price = tk.Canvas(self.price_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.price_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\price.png")
        self.icon_price.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_price.create_image(25, 25, anchor='center', image=self.price_image)
        self.icon_price.pack(side='left', padx=5)

        self.label_price = tk.Label(self.price_frame, text="Enter the item price:", bg='#ffffff', font=('Georgia', 12))
        self.label_price.pack(side='left', padx=5)

        self.entry_price = tk.Entry(self.price_frame, bg='#ffffff', font=('Georgia', 12))
        self.entry_price.pack(side='left', padx=5)

        self.brand_frame = tk.Frame(self.frame, bg='#ffffff')
        self.brand_frame.pack(pady=10)

        self.icon_brand = tk.Canvas(self.brand_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.brand_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\brand.png")
        self.icon_brand.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_brand.create_image(25, 25, anchor='center', image=self.brand_image)
        self.icon_brand.pack(side='left', padx=5)

        self.label_brand = tk.Label(self.brand_frame, text="Enter the item brand:", bg='#ffffff', font=('Georgia', 12))
        self.label_brand.pack(side='left', padx=5)

        self.entry_brand = tk.Entry(self.brand_frame, bg='#ffffff', font=('Georgia', 12))
        self.entry_brand.pack(side='left', padx=5)

        self.year_frame = tk.Frame(self.frame, bg='#ffffff')
        self.year_frame.pack(pady=10)

        self.icon_year = tk.Canvas(self.year_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.year_image = PhotoImage(
            file=r"C:\Users\Abdallah\Desktop\projectimages\WhatsApp Image 2024-09-17 at 17.03.06 (3).png")
        self.icon_year.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_year.create_image(25, 25, anchor='center', image=self.year_image)
        self.icon_year.pack(side='left', padx=5)

        self.label_year = tk.Label(self.year_frame, text="Enter the model year:", bg='#ffffff', font=('Georgia', 12))
        self.label_year.pack(side='left', padx=5)

        self.entry_year = tk.Entry(self.year_frame, bg='#ffffff', font=('Georgia', 12))
        self.entry_year.pack(side='left', padx=5)

        self.frame3 = tk.Frame(self.root, padx=10, bg='#ffffff')
        self.frame3.pack(pady=10)

        self.upload_button = tk.Button(self.frame3, text="Upload Photo", command=upload_photo, bg="#3b5998", fg="white",
                                       font=('Georgia', 12))
        self.upload_button.pack(pady=10, padx=5)

        self.photo_label = tk.Label(self.frame3, bg='#ffffff')
        self.photo_label.pack(pady=10)



        self.submit = tk.Button(self.root, text="EDIT", command=self.Edit_selected_value,bg="#3b5998", fg="white", font=('Georgia', 12))
        self.submit.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        admin_button = tk.Button(self.root, text="OPTIONS", command=self.gohome, font=('Arial', 12, 'bold'))
        admin_button.place(x=1600, y=0)

        self.root.mainloop()

    def upload_photo(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.gif")]
        )

        self.img = tk.PhotoImage(file=file_path)
        self.path = file_path
        self.photo_label.config(image=self.img)

    def Edit_selected_value(self):

        type = self.cat
        path = self.path
        name = self.entry_name.get()
        price = self.entry_price.get()
        modelyear = self.entry_year.get()
        brand = self.entry_brand.get()
        obj=Admin()                                      #dict
        result=obj.updateitem(self.cat, path, name, price, self.value,brand,modelyear)
        #print(price)
        #print(result)
        if result =="Edited" :
            messagebox.showinfo("Success", "Item updated successfully!")
            self.root.destroy()
            from main import MyApp
            MyApp()
        else :
            messagebox.showinfo("INVALID", "TRY AGAIN INVALID DATA")
            return






    def onClosing(self):
        if messagebox.askyesno(title="Quit", message="Are you sure you want to exit?"):
            print("Closing....")
            self.root.destroy()
    def gohome(self):
        self.root.destroy()
        from LoginPage import AdminOptions
        AdminOptions()



#Edit("sports",{'name': 'T-shirt', 'price': '$20', 'path': r"C:\Users\Abdallah\Desktop\Isolated_black_t_shirt_opened.png"})