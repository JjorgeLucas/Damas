from matplotlib import style
from tabuleiro import *
from tkinter import *
import tkinter.ttk as ttk


class Tela:
  """
      Classe que agrupa métodos gerais da família
      de classes de telas do Tkinter.
  """
  def __init__(self):
    self.window = Tk()
    self.window.title('Damas')
    self.window.geometry('800x600+250+25')
    self.window.resizable(False, False)
    self.window.configure(background='gray')
  
  def coloca_imagem(self,inImage,outImage):
    """
        Método que coloca imagens na tela.
    """
    pass

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
    board = Tabuleiro()
    s = ttk.Style()
    s.configure('teste.TFrame', background='purple')
    s.configure('Preto.TLabel', background='black')
    s.configure('Branco.TLabel', background='white')

    frameTab = ttk.Frame(self.window, style='teste.TFrame')

    a1 = ttk.Button(frameTab)
    a2 = ttk.Button(frameTab)
    a3 = ttk.Button(frameTab)
    a4 = ttk.Button(frameTab)
    a5 = ttk.Button(frameTab)
    a6 = ttk.Button(frameTab)
    a7 = ttk.Button(frameTab)
    a8 = ttk.Button(frameTab)
    b1 = ttk.Button(frameTab)
    b2 = ttk.Button(frameTab)
    b3 = ttk.Button(frameTab)
    b4 = ttk.Button(frameTab)
    b5 = ttk.Button(frameTab)
    b6 = ttk.Button(frameTab)
    b7 = ttk.Button(frameTab)
    b8 = ttk.Button(frameTab)
    c1 = ttk.Button(frameTab)
    c2 = ttk.Button(frameTab)
    c3 = ttk.Button(frameTab)
    c4 = ttk.Button(frameTab)
    c5 = ttk.Button(frameTab)
    c6 = ttk.Button(frameTab)
    c7 = ttk.Button(frameTab)
    c8 = ttk.Button(frameTab)
    d1 = ttk.Button(frameTab)
    d2 = ttk.Button(frameTab)
    d3 = ttk.Button(frameTab)
    d4 = ttk.Button(frameTab)
    d5 = ttk.Button(frameTab)
    d6 = ttk.Button(frameTab)
    d7 = ttk.Button(frameTab)
    d8 = ttk.Button(frameTab)
    e1 = ttk.Button(frameTab)
    e2 = ttk.Button(frameTab)
    e3 = ttk.Button(frameTab)
    e4 = ttk.Button(frameTab)
    e5 = ttk.Button(frameTab)
    e6 = ttk.Button(frameTab)
    e7 = ttk.Button(frameTab)
    e8 = ttk.Button(frameTab)
    f1 = ttk.Button(frameTab)
    f2 = ttk.Button(frameTab)
    f3 = ttk.Button(frameTab)
    f4 = ttk.Button(frameTab)
    f5 = ttk.Button(frameTab)
    f6 = ttk.Button(frameTab)
    f7 = ttk.Button(frameTab)
    f8 = ttk.Button(frameTab)
    g1 = ttk.Button(frameTab)
    g2 = ttk.Button(frameTab)
    g3 = ttk.Button(frameTab)
    g4 = ttk.Button(frameTab)
    g5 = ttk.Button(frameTab)
    g6 = ttk.Button(frameTab)
    g7 = ttk.Button(frameTab)
    g8 = ttk.Button(frameTab)
    h1 = ttk.Button(frameTab)
    h2 = ttk.Button(frameTab)
    h3 = ttk.Button(frameTab)
    h4 = ttk.Button(frameTab)
    h5 = ttk.Button(frameTab)
    h6 = ttk.Button(frameTab)
    h7 = ttk.Button(frameTab)
    h8 = ttk.Button(frameTab)




    widgets = [frameTab]
    for i in widgets:
      i.pack(side='left', padx=5, pady=5)
    
    buttons =[[a1,a2,a3,a4,a5,a6,a7,a8],
              [b1,b2,b3,b4,b5,b6,b7,b8],
              [c1,c2,c3,c4,c5,c6,c7,c8],
              [d1,d2,d3,d4,d5,d6,d7,d8],
              [e1,e2,e3,e4,e5,e6,e7,e8],
              [f1,f2,f3,f4,f5,f6,f7,f8],
              [g1,g2,g3,g4,g5,g6,g7,g8],
              [h1,h2,h3,h4,h5,h6,h7,h8]]
    
    for row_index, row in enumerate(buttons):
      for col_index, btn in enumerate(buttons[row_index]):
        for linha in Tabuleiro.geraTabuleiroMaquina():
          for casa in linha:
            if casa == 0:
              btn['style'] = 'Branco.TLabel'
              btn.grid(row=row_index, column=col_index)
            elif casa == 1: 
              btn['style'] = 'Preto.TLabel'
              btn.grid(row=row_index, column=col_index)
              

    self.window.mainloop()

a= Tela()
a.telaPartida()
