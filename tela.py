<<<<<<< Updated upstream
import tkinter as Tk
=======
from tkinter import *
import tkinter.ttk as ttk

from matplotlib import widgets

>>>>>>> Stashed changes

class Tela:
  """
      Classe que gerencia a interface com que o usuário
      vai interagir com durante o funcionamento do jogo.
  """
  def __init__(self):
    pass
  
  def coloca_imagem(self,inImage,outImage):
    """
        Método que coloca imagens na tela.
    """
    pass
  
  def get_value(self, widget_name):
    """
        Método que coleta informações geradas por Entry()
        e Button().
    """
    pass
  def destroy(self, frame):
    """
        Método que destroi um frame a fim de exibir outro numa mesma
        tela.
    """
    frame.destroy()
    
  def 