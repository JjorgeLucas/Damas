
# from tkinter import ttk
from tkinter import *
import tkinter.ttk as ttk


tela = Tk()

style = ttk.Style()
style.configure('Branco.TFrame', background='black')
style.configure('Vermelho.TFrame', background='red')

frame1 = ttk.Frame(tela, style='Vermelho.TFrame')
frame2 = ttk.Frame(tela, style='Branco.TFrame')

# método pra dar pack()
widgets = [frame1, frame2]
for i in widgets:
    i.pack(side = 'top', padx= 5, pady= 5, fill= 'y',)


tela.mainloop()

# window = Tk()
# window.title("Title Name")
# window.config(bg='#FFFAFA')
# window.geometry('1024x800')


# menubar = Menu(window)
# filemenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='Open')
# filemenu.add_command(label='Clear')
# filemenu.add_command(label='Save As')
# filemenu.add_separator()
# filemenu.add_command(label='Exit')


# helpmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='Precuations')
# helpmenu.add_command(label='Version Info')
# helpmenu.add_command(label='Technical Support')

# window.config(menu=menubar)

# rows = 0
# while rows < 50:
#     window.rowconfigure(rows, weight=1)
#     window.columnconfigure(rows, weight=1)
#     rows += 1

# #creation of frame
# mainframe = ttk.Notebook(window, width=50)
# mainframe.grid(row=1, column=2, columnspan=45, rowspan=43, sticky='NESW')

# #create tabs within the frame
# tab1 = ttk.Frame(mainframe)
# mainframe.add(tab1, text="Tab1")


# tab2 = ttk.Frame(mainframe)
# mainframe.add(tab2, text="Tab2")


# tab3 = ttk.Frame(mainframe)
# mainframe.add(tab3, text="Tab3")

# tab4 = ttk.Frame(mainframe)
# mainframe.add(tab4, text="Tab4")

# tab5 = ttk.Frame(mainframe)
# mainframe.add(tab5, text="Tab4")

# window.mainloop()
