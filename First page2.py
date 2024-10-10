import tkinter as tk
from tkinter import PhotoImage, messagebox
from register2 import Register
from USERE import USER

class MyGUI:
    ob = USER()

    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#ffffff')
        self.root.title("My Application")
        self.root.geometry("1555x1000")


        self.image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\WhatsApp Image 2024-09-17 at 01.15.07_aa4bd3ba.gif")
        self.image_login = tk.Canvas(self.root, width=777.5, height=1000, bg='#ffffff', highlightthickness=0)
        self.image_login.place(x=0, y=170)
        self.image_login.create_image(0, 0, anchor='nw', image=self.image)


        self.login_frame = tk.Frame(self.root, width=777.5, height=1000, bg='#ffffff')
        self.login_frame.place(x=777.5, y=0)


        self.label1 = tk.Label(self.login_frame, text="My Application", font=('Georgia', 30, 'bold'), bg='#ffffff', fg='#333333')
        self.label1.pack(pady=(50, 40))

        self.label2 = tk.Label(self.login_frame, text="Welcome back to your favorite shopping app!", font=('Georgia', 20), bg='#ffffff', fg='#333333')
        self.label2.pack(pady=20)

        self.username_frame = tk.Frame(self.login_frame, bg='#ffffff')
        self.username_frame.pack(pady=10, padx=20, anchor='w', fill='x')


        self.icon_canvas = tk.Canvas(self.username_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.icon_canvas.pack(side='left', padx=0)
        self.icon_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\WhatsApp Image 2024-09-17 at 13.57.20 (2).png")
        self.icon_canvas.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_canvas.create_image(25, 25, anchor='center', image=self.icon_image)

        self.label4 = tk.Label(self.username_frame, text="UserName / Email :", font=('Helvetica', 16), bg='#ffffff', fg='#333333')
        self.label4.pack(side='left', padx=0)


        self.entry1 = tk.Entry(self.login_frame, font=('Helvetica', 16), bg='#ffffff', bd=1, relief='solid')
        self.entry1.pack(pady=10, padx=20, fill=tk.X)

        self.pass_frame = tk.Frame(self.login_frame, bg='#ffffff')
        self.pass_frame.pack(pady=10, padx=20, anchor='w', fill='x')

        self.icon_pass = tk.Canvas(self.pass_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.icon_pass.pack(side='left', padx=0)
        self.pass_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\WhatsApp Image 2024-09-17 at 13.57.20 (1).png")
        self.icon_pass.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_pass.create_image(25, 25, anchor='center', image=self.pass_image)

        self.label5 = tk.Label(self.pass_frame, text="Password :", font=('Helvetica', 16), bg='#ffffff', fg='#333333')
        self.label5.pack(pady=10, padx=20, anchor='w')


        self.entry2 = tk.Entry(self.login_frame, font=('Helvetica', 16), show='*', bg='#ffffff', bd=1, relief='solid')
        self.entry2.pack(pady=10, padx=20, fill=tk.X)


        self.button1 = tk.Button(self.login_frame, text="Login", height=2, width=20, font=('Georgia', 14, 'bold'), bg='#4CAF50', fg='white', bd=0, relief='flat', command=self.login)
        self.button1.pack(pady=20)


        self.label6 = tk.Label(self.login_frame, text="Don't have an account?", font=('Georgia', 16), bg='#ffffff', fg='#333333')
        self.label6.pack(pady=(30, 5))

        self.sign_up = tk.Label(self.login_frame, text="Sign UP", font=('Georgia', 16, 'bold'), bg='#ffffff', fg='#2196F3', cursor='hand2')
        self.sign_up.pack(pady=10)
        self.sign_up.bind("<Button-1>", self.open_register)

        self.root.mainloop()

    def open_register(self,event):
        self.root.destroy()
        Register()

    def login(self):
        mail = self.entry1.get().strip()
        password = self.entry2.get().strip()
        if mail.strip().lower() == "admin@gmail.com":
            if password.strip().lower() == "admin123":
                messagebox.showinfo("Success", "sign in successful welcome ADMIN!")
                self.root.destroy()
                from LoginPage import AdminOptions
                AdminOptions()

        else:

            res = self.ob.login(mail, password)
            if res != "Done":
                messagebox.showerror("Error", res)
                return
            else:
                messagebox.showinfo("Success", "sign in successful!")
                self.root.destroy()
                from userGUI import MyApp
                MyApp()

MyGUI()









