#este arquivo está quase pronto
import tkinter
from tkinter import messagebox
import getpass

window = tkinter.Tk()
window.title("Login")
window.geometry('750x550')
window.configure(bg='#FFE608')

def login():
    username = "root/admin"
    password = "190the@quick#browm$fox%jumps&over*the@lazy#dog486"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login correto!", message="Você está logado.")
    else:
        messagebox.showerror(title="Erro", message="Login inválido.")


#sessão abaixo ainda necessita ser finalizada
database = {"Alan": "123456", "Alana": "654321"}
username = input("Coloque o seu nome : ")
password = getpass.getpass("Senha : ")
for i in database.keys():
if username == i:
while password != database.get(i):
password = getpass.getpass("entre sua senha novamente : ")
break
print("Verified")

frame = tkinter.Frame(bg='#8F00FF')

login_label = tkinter.Label(frame, text="Renault", bg='#000000', fg="#DC143C", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
