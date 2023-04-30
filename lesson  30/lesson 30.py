from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x500")
#
# lst = ["Один", "Два", "Пятнадцать"]
# lstbox = Listbox(win,
#                  selectmode=EXTENDED,
#                  bg="pink",
#                  fg="lightblue",
#                  )
# lstbox.pack()
# Button(win, text="НОпкеа", command = get_lst).pack()
#
#
#
#
# #1 пособ: через вставку циклом
# # for elem in lst:
# #     lstbox.insert(END, elem)
#
#
# #2 Способ: через переменую
# lst_tk = StringVar(value=lst)
# print(lst_tk.get())
# lstbox['listvariable'] = lst_tk
#
#
#
# messagebox.showinfo("Информация","Я люблю твою мамау")
# messagebox.showerror()
# messagebox.showwarning()

# Button(win, text="Я играю в раст").pack(pady=50, ipadx=20)
# Button(win, text="Я играю в раст").pack(pady=50)



# column - столбик
# row - ряд
# Button(win, text="нопка для мозгов").grid(column=0, row=0)
# Button(win, text="Я играю в раст").grid(column=3, row=0)
# Button(win, text=" тебя есть отчем").grid(column=2, row=0)
# Button(win, text=" у тебя есть мозг").grid(column=0, row=1, columnspan=2, sticky=EW)
#
#








# Button(win, text="sksksk").place(x=10, y=10)






#
# def hello():
#     print("Прифки")
#     win.after(1000, hello)
#
# win.after(5000, hello)

# win.mainloop()





# def hello():
#     print("Риффки")
#
# btn = Button(win, text="Кнопка")
# btn.pack()
# btn.bind("<Return>", hello)
# btn.bind()






# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5)
# print(rb_val)






#
#
# Entry(win, show="*").pack()  # создаст Entry где любые символы отобразятся как *
# Entry(win, show="Э").pack()  # да, любые вводимые символы отобразятся как Э
#

win.mainloop()