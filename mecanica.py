import ferramentas
import estatisticas
import jogador
import exceptions
import log
import maquina
import pecas
import tabuleiro
import tela


class MecanicaGeral:
  """
      Classe que organiza e define as instâncias do jogo
      no loop principal.
  """
  pass

  #Regras: http://www.damasciencias.com.br/regras-jogo-de-damas/
  
  def __init__(self,):
    #usar um if para saber se o jogo será carregado a partir de um save
    #ou se será um novo jogo.
    pass

  def checaJogada(self):
    """
        Método que checa se a jogada é válida.
    """
    pass
  
  def checaFinal(self):
    """
        Método que checa se houve vencedor, quem foi ou se 
        houve empate, de acordo com as regras oficiais do jogo.
    """
    pass
  
  def save(self):
    """
        Faz um save manual do estado do jogo.
    """
    pass
  
  def autosave(self):
    """
        Faz um save temporário a cada intervalo a ser definido.
    """
    #a cada jogada, a cada algumas jogadas, etc.
    pass
  
  def jogada():
    """
        Método que realiza a jogada do jogador. A jogada da máquina
        será feita através de um método próprio na classe Maquina().
    """
    pass