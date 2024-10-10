import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage, messagebox
from USERE import USER

class Register:
    obj = USER()

    def __init__(self):
        self.register = tk.Tk()
        self.register.configure(bg='#ffffff')
        self.register.title("Register Form")
        self.register.geometry("1555x1000")

        self.frame = tk.Frame(self.register, bg='#ffffff')
        self.frame.pack(expand=True, fill='both')

        self.title_frame = tk.Frame(self.frame, bg='#3498DB')
        self.title_frame.pack(pady=30)

        self.label = tk.Label(self.title_frame, text="Welcome To Our Store", font=('Georgia', 14, 'bold'), bg='#3498DB', fg='white')
        self.label.pack(pady=30, padx=50)

        self.user_info_frame = tk.Frame(self.frame, bg='#ffffff')
        self.user_info_frame.pack(pady=30)

        self.username_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.username_frame.grid(row=0, column=0, pady=20)

        self.icon_canvas = tk.Canvas(self.username_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.icon_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\WhatsApp Image 2024-09-17 at 13.57.20 (2).png")
        self.icon_canvas.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_canvas.create_image(25, 25, anchor='center', image=self.icon_image)
        self.icon_canvas.pack(side='left', padx=5)

        self.username_label = tk.Label(self.username_frame, text="User name:", font=('Georgia', 16), bg='#ffffff')
        self.username_label.pack(side='left', padx=5)
        self.username_entry = tk.Entry(self.username_frame, font=('Georgia', 16), bg='#ffffff', width=25)
        self.username_entry.pack(side='left', padx=5)

        self.pass_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.pass_frame.grid(row=0, column=1, pady=20)

        self.icon_pass = tk.Canvas(self.pass_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.pass_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\WhatsApp Image 2024-09-17 at 13.57.20 (1).png")
        self.icon_pass.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_pass.create_image(25, 25, anchor='center', image=self.pass_image)
        self.icon_pass.pack(side='left', padx=5)

        self.password_label = tk.Label(self.pass_frame, text="Password: ", font=('Georgia', 16), bg='#ffffff')
        self.password_label.pack(side='left', padx=5)
        self.password_entry = tk.Entry(self.pass_frame, font=('Georgia', 16), show="*", bg='#ffffff', width=25)
        self.password_entry.pack(side='left', padx=5)

        self.email_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.email_frame.grid(row=1, column=0, pady=20)

        self.icon_email = tk.Canvas(self.email_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.email_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\email.png")
        self.icon_email.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_email.create_image(25, 25, anchor='center', image=self.email_image)
        self.icon_email.pack(side='left', padx=5)

        self.email_label = tk.Label(self.email_frame, text="Email:     ", font=('Georgia', 16), bg='#ffffff')
        self.email_label.pack(side='left', padx=5)
        self.email_entry = tk.Entry(self.email_frame, font=('Georgia', 16), bg='#ffffff', width=25)
        self.email_entry.pack(side='left', padx=5)

        self.phone_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.phone_frame.grid(row=1, column=1, pady=20)

        self.icon_phone = tk.Canvas(self.phone_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.phone_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\telephone-icon-3617.png")
        self.icon_phone.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_phone.create_image(25, 25, anchor='center', image=self.phone_image)
        self.icon_phone.pack(side='left', padx=5)

        self.phone_label = tk.Label(self.phone_frame, text="Number:   ", font=('Georgia', 16), bg='#ffffff')
        self.phone_label.pack(side='left', padx=5)
        self.phone_entry = tk.Entry(self.phone_frame, font=('Georgia', 16), bg='#ffffff', width=25)
        self.phone_entry.pack(side='left', padx=5)

        self.age_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.age_frame.grid(row=2, column=0, pady=20)

        self.icon_age = tk.Canvas(self.age_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.age_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\age.png")
        self.icon_age.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_age.create_image(25, 25, anchor='center', image=self.age_image)
        self.icon_age.pack(side='left', padx=5)

        self.age_label = tk.Label(self.age_frame, text="Age:       ", font=('Georgia', 16), bg='#ffffff')
        self.age_label.pack(side='left', padx=5)
        self.age_entry = tk.Entry(self.age_frame, font=('Georgia', 16), bg='#ffffff', width=25)
        self.age_entry.pack(side='left', padx=5)

        self.id_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.id_frame.grid(row=2, column=1, pady=20)

        self.icon_id = tk.Canvas(self.id_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.id_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\id.png")
        self.icon_id.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_id.create_image(25, 25, anchor='center', image=self.id_image)
        self.icon_id.pack(side='left', padx=5)

        self.id_label = tk.Label(self.id_frame, text="National ID:", font=('Georgia', 16), bg='#ffffff')
        self.id_label.pack(side='left', padx=5)
        self.id_entry = tk.Entry(self.id_frame, font=('Georgia', 16), bg='#ffffff', width=25)
        self.id_entry.pack(side='left', padx=5)

        self.gov_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.gov_frame.grid(row=3, column=0, pady=20)

        self.icon_gov = tk.Canvas(self.gov_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.gov_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\gov.png")
        self.icon_gov.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_gov.create_image(25, 25, anchor='center', image=self.gov_image)
        self.icon_gov.pack(side='left', padx=5)

        self.governorate_label = tk.Label(self.gov_frame, text="Governorate:", font=('Georgia', 16), bg='#ffffff')
        self.governorate_label.pack(side='left', padx=5)
        self.governorate_entry = tk.Entry(self.gov_frame, font=("arial", 16), bg='#ffffff', width=25)
        self.governorate_entry.pack(side='left', padx=5)

        self.gender_frame = tk.Frame(self.user_info_frame, bg='#ffffff')
        self.gender_frame.grid(row=3, column=1, pady=20)

        self.icon_gender = tk.Canvas(self.gender_frame, width=50, height=50, bg='#ffffff', highlightthickness=0)
        self.gender_image = PhotoImage(file=r"C:\Users\Abdallah\Desktop\projectimages\gen.png")
        self.icon_gender.create_oval(5, 5, 45, 45, fill='#ffffff', outline='#ffffff')
        self.icon_gender.create_image(25, 25, anchor='center', image=self.gender_image)
        self.icon_gender.pack(side='left', padx=5)

        self.gender_label = tk.Label(self.gender_frame, text="Gender: ", font=('Georgia', 16), bg='#ffffff')
        self.gender_label.pack(side='left',pady=5)
        self.gender = ttk.Combobox(self.gender_frame, values=["Female", "Male"], font=('Georgia', 16))
        self.gender.pack(side='left',pady=5, padx=20)

        self.register_button = tk.Button(self.frame, text="Register", command=self.save_data, font=('Georgia', 16), bg='#3498DB', fg='white')
        self.register_button.pack(pady=40)

        self.register.mainloop()

    def save_data(self):
        user_info = {
            "username": self.username_entry.get().strip(),
            "password": self.password_entry.get().strip(),
            "email": self.email_entry.get().strip(),
            "phone": self.phone_entry.get().strip(),
            "age": self.age_entry.get().strip(),
            "national_id": self.id_entry.get().strip(),
            "governorate": self.governorate_entry.get().strip(),
            "gender": self.gender.get().strip()
        }
        res = self.obj.register(user_info["username"], user_info["phone"], user_info["email"], user_info["gender"],
                                user_info["governorate"], user_info["password"], user_info["age"],
                                user_info["national_id"])
        if res != "ADDED":
            messagebox.showerror("Error", res)
            return
        else:
            messagebox.showinfo("Success", "Registration successful!")
            self.register.destroy()
            from userGUI import MyApp
            MyApp()

