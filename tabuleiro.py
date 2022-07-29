import ferramentas
import numpy as np

class Tabuleiro:
  """
      Classe que representará o tabuleiro 8x8 do jogo no Back-end do jogo.
  """
  
  def __init__(self, novo_jogo=True):
    """
        O método mágico __init__ criará os tabuleiros.
    """
    if novo_jogo == True:
      indices = range(-6, 8, 2)
      self.tab = np.zeros(shape=[8, 8], dtype=np.int32)
      for i in indices:
          self.tab += np.eye(N=8, M=8, k=i, dtype=np.int32)
      self.tab = [list(x) for x in self.tab]
      # linhas 0, 1 e 2 - -> pretas
      # linhas 5, 6 e 7 - -> brancas
      for i in range(8):
        for j in range(8):
          
          if self.tab[i][j] == 1 and i < 3:
            self.tab[i][j] = 'p'
          
          elif self.tab[i][j] == 1 and i > 4:
            self.tab[i][j] = 'b'
      
    else:
      #carrega jogo salvo em arquivo
      pass


  def salvaTabuleiro():
    """
        Método que salva o estado do tabuleiro e o armazena.
    """
    pass
  
  

# tabu = Tabuleiro()
# print(tabu.tab)
