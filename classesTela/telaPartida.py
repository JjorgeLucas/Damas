from ..Damas import Tabuleiro
from telaMae import *

class TelaPartida(Tela,Tabuleiro):
    """
        Tela que será exibida durante a partida.
    """
    
    def __init__(self,tabuleiro=Tabuleiro.tab):
        Tabuleiro.__init__(self)
        Tela.__init__(self)
        frameTab = ttk.Frame(Tela.window)
        
        
        
tela = TelaPartida()