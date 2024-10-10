import tkinter as tk
from tkinter import messagebox

# el options beta3t el admin
class AdminOptions:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Admin Options")
        self.root.geometry("500x500")


        self.title_label = tk.Label(self.root, text="Admin Options", font=('Georgia', 20, 'bold'), bg="#3b5998", fg="white")
        self.title_label.pack(pady=20)


        self.ADDButton = tk.Button(self.root, text="Add Item", bg = "#3b5998", fg = "white", font = ('Georgia', 12), command=self.goToAddItem)
        self.ADDButton.pack(pady=10)


        self.Makesale = tk.Button(self.root, text="Make Sale",bg = "#3b5998", fg = "white", font = ('Georgia', 12), command=self.goToMakeSale)
        self.Makesale.pack(pady=10)


        self.SeeCategories = tk.Button(self.root, text="Edit and See Categories", bg = "#3b5998", fg = "white", font = ('Georgia', 12), command=self.goToCategories)
        self.SeeCategories.pack(pady=10)

        self.SeeCategories2 = tk.Button(self.root, text="Remove Item",bg = "#3b5998", fg = "white", font = ('Georgia', 12),
                                       command=self.goToRemove)
        self.SeeCategories2.pack(pady=10)
        self.SeeCategories3 = tk.Button(self.root, text="Remove Last Discount", bg = "#3b5998", fg = "white", font = ('Georgia', 12),
                                        command=self.removediscount)
        self.SeeCategories3.pack(pady=10)


        self.root.mainloop()

    def goToAddItem(self):
        self.root.destroy()
        from tkinterClass import MyGUI
        obj=MyGUI()

    def goToMakeSale(self):
        self.root.destroy()
        from SALEeee import MakeSale
        MakeSale()

    def goToCategories(self):
        self.root.destroy()
        from main import MyApp
        obj=MyApp()

    def goToRemove(self):
        self.root.destroy()
        from removeitemGUI import Remove
        obj = Remove()

    def removediscount(self):
        from AdminOptions import Admin
        obj=Admin()
        res=obj.remove_last_discount()
        messagebox.showinfo("ERROR",res)






