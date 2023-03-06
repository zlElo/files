import customtkinter
from time import strftime
from time_ import *

root = customtkinter.CTk()
root.title('OClock')


def time():
    string = strftime('%H:%M:%S Uhr')
    time_label_current.configure(text=string)

    if string == '13:30:00 Uhr':
        called_successfully()

    time_label_current.after(1000, time)

time_label_current = customtkinter.CTkLabel(root, font=('Arial', 70))
time_label_current.pack(anchor='center')

time()

root.mainloop()