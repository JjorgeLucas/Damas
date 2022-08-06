# https: // www.flaticon.com/br/icone-gratis/verificadores-chineses_2006254?term = damas & related_id = 2006254

from tabuleiro import *
from tkinter import *
import tkinter.ttk as ttk


class Tela(ttk.Frame):
  """
      Classe que agrupa métodos gerais da família
      de classes de telas do Tkinter.
  """
  def __init__(self):
    self.window = Tk()
    self.window.title('Damas')
    self.window.geometry('960x600+200+30')
    self.window.resizable(False, False)
    self.window.configure(background='gray')
    
    # imagens
    self.dama_branca = PhotoImage(file='images/damaBranca.png')
    self.dama_preta = PhotoImage(file='images/damaPreta.png')
    self.pedra_branca = PhotoImage(file='images/pedraBranca.png')
    self.pedra_preta = PhotoImage(file='images/pedraPreta.png')
    self.blank = PhotoImage(file='images/blank.png')
    self.menu = PhotoImage(file='images/imgMenus.png')
    self.foto1 = PhotoImage(file='images/foto1.png')
    self.foto2 = PhotoImage(file='images/foto2.png')
    self.foto3 = PhotoImage(file='images/foto3.png')
    self.foto4 = PhotoImage(file='images/foto4.png')


  def get_value(self, inValue):
    """
        Método que coleta informações geradas por Entry()
        e Button().
    """
    pass
  
  def telaPartida(self):
    """
        Tela que será exibida durante a partida.
    """
    # board = Tabuleiro()
    s = ttk.Style()
    s.configure('teste.TFrame', background='purple')
    s.configure('Branco.TLabel',
                background='white',
                foreground='green',
                width = 2, height = 10)
    s.configure('Preto.TLabel',
                background='black',
                foreground = 'green',
                width = 2, height = 10)


    main_frameTab = ttk.Frame(self.window, style='teste.TFrame')
    frameTab = ttk.Frame(main_frameTab)

    a1 = ttk.Label(frameTab)
    a2 = ttk.Label(frameTab)
    a3 = ttk.Label(frameTab)
    a4 = ttk.Label(frameTab)
    a5 = ttk.Label(frameTab)
    a6 = ttk.Label(frameTab)
    a7 = ttk.Label(frameTab)
    a8 = ttk.Label(frameTab)
    b1 = ttk.Label(frameTab)
    b2 = ttk.Label(frameTab)
    b3 = ttk.Label(frameTab)
    b4 = ttk.Label(frameTab)
    b5 = ttk.Label(frameTab)
    b6 = ttk.Label(frameTab)
    b7 = ttk.Label(frameTab)
    b8 = ttk.Label(frameTab)
    c1 = ttk.Label(frameTab)
    c2 = ttk.Label(frameTab)
    c3 = ttk.Label(frameTab)
    c4 = ttk.Label(frameTab)
    c5 = ttk.Label(frameTab)
    c6 = ttk.Label(frameTab)
    c7 = ttk.Label(frameTab)
    c8 = ttk.Label(frameTab)
    d1 = ttk.Label(frameTab)
    d2 = ttk.Label(frameTab)
    d3 = ttk.Label(frameTab)
    d4 = ttk.Label(frameTab)
    d5 = ttk.Label(frameTab)
    d6 = ttk.Label(frameTab)
    d7 = ttk.Label(frameTab)
    d8 = ttk.Label(frameTab)
    e1 = ttk.Label(frameTab)
    e2 = ttk.Label(frameTab)
    e3 = ttk.Label(frameTab)
    e4 = ttk.Label(frameTab)
    e5 = ttk.Label(frameTab)
    e6 = ttk.Label(frameTab)
    e7 = ttk.Label(frameTab)
    e8 = ttk.Label(frameTab)
    f1 = ttk.Label(frameTab)
    f2 = ttk.Label(frameTab)
    f3 = ttk.Label(frameTab)
    f4 = ttk.Label(frameTab)
    f5 = ttk.Label(frameTab)
    f6 = ttk.Label(frameTab)
    f7 = ttk.Label(frameTab)
    f8 = ttk.Label(frameTab)
    g1 = ttk.Label(frameTab)
    g2 = ttk.Label(frameTab)
    g3 = ttk.Label(frameTab)
    g4 = ttk.Label(frameTab)
    g5 = ttk.Label(frameTab)
    g6 = ttk.Label(frameTab)
    g7 = ttk.Label(frameTab)
    g8 = ttk.Label(frameTab)
    h1 = ttk.Label(frameTab)
    h2 = ttk.Label(frameTab)
    h3 = ttk.Label(frameTab)
    h4 = ttk.Label(frameTab)
    h5 = ttk.Label(frameTab)
    h6 = ttk.Label(frameTab)
    h7 = ttk.Label(frameTab)
    h8 = ttk.Label(frameTab)


    main_frameTab.pack(expand=True, fill='both')
    frameTab.pack(expand=True)
    
    Labels =[ [a1,a2,a3,a4,a5,a6,a7,a8],
              [b1,b2,b3,b4,b5,b6,b7,b8],
              [c1,c2,c3,c4,c5,c6,c7,c8],
              [d1,d2,d3,d4,d5,d6,d7,d8],
              [e1,e2,e3,e4,e5,e6,e7,e8],
              [f1,f2,f3,f4,f5,f6,f7,f8],
              [g1,g2,g3,g4,g5,g6,g7,g8],
              [h1,h2,h3,h4,h5,h6,h7,h8]]
    
    for row_index, row in enumerate(Labels):
      for col_index, lbl in enumerate(Labels[row_index]):
        lbl.grid(row=row_index, column=col_index)
        lbl.grid(row=row_index, column=col_index)
        
    for i in range(len(Labels)):
      for indice, label in enumerate(Labels[i]):
        if i % 2 == 0:
          if indice % 2 == 0:
            label['style'] = 'Preto.TLabel'
            label['image'] = self.pedra_preta
          else:
            label['image'] = self.blank
            label['style'] = 'Branco.TLabel'
        
        else:
          if indice % 2 != 0:
            label['image'] = self.dama_preta
            label['style'] = 'Preto.TLabel'
          else:
            label['image'] = self.blank
            label['style'] = 'Branco.TLabel'
          

    self.window.mainloop()

# a= Tela()
# a.telaPartida()


  def telaMenu(self):
    """
        Tela que será exibida enquanto o usuário estiver no menu principal.
    """
    
    # s = ttk.Style()
    # s.configure()
    
    
    main_frameMenu = ttk.Frame(self.window)
    lbl_fundo = ttk.Label(main_frameMenu, image=self.menu)
    
    # canvaMenu.create_image(image = self.menu)
    
    main_frameMenu.pack(expand=True, fill='both')
    lbl_fundo.pack(expand=True, fill= 'both')
    
    self.window.mainloop()
    
a= Tela()
a.telaMenu()