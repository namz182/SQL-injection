#dev:Mainza Namangani
import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3

connection = sqlite3.connect("user_login.db")
cursor = connection.cursor()

#----------------------create account-------------------------------------
def create_account():
    table = '''CREATE TABLE IF NOT EXISTS users(
                username varchar(255),
           P     password varchar(255)
    )''' 
    cursor.execute(table)
    username = create_user_name.get()
    password = create_password.get()

    if confirm_password.get() != password:
        tkmb.showerror(title="error", message="passwords do not match")
    
    elif len(username) == 0 or len(password) == 0:
        tkmb.showerror(title="error", message="username or password cannot be empty")
    else:
      cursor.execute('INSERT INTO users (username, password) VALUES (?,?)',(username,password))
      tkmb.showinfo(title="accout created", message="Account created successfully")
    connection.commit()
#------------------------------login--------------------------------------
def Login():
    username = user_name.get()
    password = password_entry.get()
    
    cursor.execute('''SELECT * FROM users WHERE USERNAME= '{0}' AND PASSWORD= '{1}';'''.format(username,password))
    
    result = cursor.fetchone()

    if len(username) == 0 or len(password) == 0:
        tkmb.showerror(title="error", message="username or password cannot be empty")
    elif result:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username or password")
    

#----------------------------show password--------------------------------------
def show_password():
    if password_entry.cget("show") == "":
        password_entry.configure(show="*")
        show_password_button.configure(text="show password")
    else:
        password_entry.configure(show="")
        show_password_button.configure(text="hide")

#--------------------------------------------------------------------------
def show_password2():
    if create_password.cget("show") == "" or confirm_password.cget("show") == "":
        create_password.configure(show="*")
        confirm_password.configure(show="*")
        show_password_button2.configure(text="Show Password")
    else:
        create_password.configure(show="")
        confirm_password.configure(show="")
        show_password_button2.configure(text="Hide Password")

    
#-------------------------------creating window------------------------------------------
window = ctk.CTk()
window.geometry('500x350')
window.resizable(False, False)
window.title('Login')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

label = ctk.CTkLabel(window, text="Welcome")
label.pack(padx=0, pady=10)

tabView = ctk.CTkTabview(window, width=400,
                                height=400,
                                corner_radius=20)
tabView.pack(side='left', fill='both', expand= 22, padx= 20, pady= 20)

tabView.add("login")
tabView.add("sign up")

#----------------------------login tab---------------------------------------------
Login_frame =ctk.CTkFrame(tabView.tab("login"),corner_radius=20)
Login_frame.pack( expand= 1)

user_name = ctk.CTkEntry(Login_frame, placeholder_text="Username")
user_name.pack(fill='both', expand= 1, padx= 0, pady= 5)

password_entry = ctk.CTkEntry(Login_frame, placeholder_text="password", show="*")
password_entry.pack(fill='both', expand= 1, padx= 0, pady= 5)


show_password_button = ctk.CTkButton(Login_frame, text="Show Password", command=show_password)
show_password_button.pack(side="right", padx=20)


Login_button =ctk.CTkButton(Login_frame, text="Login", command=Login)
Login_button.pack(padx=10, pady=5)

#--------------------------------sign up tab----------------------------------------
signup_frame = ctk.CTkFrame(tabView.tab("sign up"), corner_radius=20)
signup_frame.pack()

create_user_name = ctk.CTkEntry(signup_frame, placeholder_text="Enter Username")
create_user_name.pack(fill='both', expand= 1, padx= 0, pady= 5)

create_password = ctk.CTkEntry(signup_frame, placeholder_text="Enter password", show="*")
create_password.pack(fill='both', expand= 1, padx= 0, pady= 5)

confirm_password = ctk.CTkEntry(signup_frame, placeholder_text="Confirm password", show="*")
confirm_password.pack(fill='both', expand= 1, padx= 0, pady= 5)

show_password_button2 = ctk.CTkButton(signup_frame, text="Show Password", command=show_password2)
show_password_button2.pack(side="right", padx=20)

create_button =ctk.CTkButton(signup_frame, text="Create account", command=create_account)
create_button.pack(padx=10, pady=5)

window.mainloop()
connection.commit()
connection.close()