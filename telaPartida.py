from tabuleiro import *
from telaMae import *

class TelaPartida(Tela,Tabuleiro):
    """
        Tela que será exibida durante a partida.
    """
        
    def __init__(self):
        Tabuleiro.__init__(self)
        Tela.__init__(self)
        
        s = ttk.Style()
        s.configure('teste.TLabel', background='red', foreground='black')
        s.configure('teste.TFrame', background='purple')
        
        frameTab = ttk.Frame(Tela.window, style='teste.TFrame')
        lblteste = ttk.Label(frameTab, text='Hello World!', style='teste.TLabel')
        
        widgets = [frameTab, lblteste]
        for i in widgets:
            i.pack(side='top', padx=5, pady=5, fill='y',)
        
        
tela = TelaPartida()