from tkinter import END, messagebox, StringVar, Entry, Button, Menu, Tk
from translate import Translator

width = 450
height = 450

root = Tk()
root.title("GoogleTranslatePY")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)


def translate():
    message_t = message.get()
    lang_1_t = lang_1.get()
    lang_2_t = lang_2.get()
    translator = Translator(from_lang=lang_1_t, to_lang=lang_2_t)
    result = translator.translate(message_t)
    message_entry_4.delete(0, END)
    message_entry_4.insert(0, result)


def info():
    messagebox.showinfo("Інформація", """У 1 полі вставте те, що перекладатиметься.
У 2 і 3 полях - з якого і якою мовою ми переведемо повідомлення.
У 4 полі буде переведене повідомлення.
Використовуйте для 2 і 3 поля лише англійські значення, наприклад :\n Ukrainian,English...""")


message = StringVar()
lang_1 = StringVar()
lang_2 = StringVar()
message_1 = StringVar()

message_entry_1 = Entry(textvariable=message)
message_entry_1.place(relx=.5, rely=.3, anchor="c", width="300", height="25")
message_entry_2 = Entry(textvariable=lang_1)
message_entry_2.place(relx=.3, rely=.4, anchor="c", width="120", height="25")
message_entry_3 = Entry(textvariable=lang_2)
message_entry_3.place(relx=.7, rely=.4, anchor="c", width="120", height="25")
message_entry_4 = Entry()
message_entry_4.place(relx=.5, rely=.5, anchor="c", width="300", height="25")

message_button = Button(text="Перевести", padx="20", pady="15", background="#555", foreground="#fff", command=translate)
message_button.place(relx=.5, rely=.7, anchor="c")

main_menu = Menu()
main_menu.add_cascade(label="Інформація", command=info)

root.config(menu=main_menu)
root.mainloop()
