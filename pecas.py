class Pedra:
  """
      Classe que representa as peças do jogo assim como armazena
      seus atributos e métodos.
  """

  def __init__(self, cor):
    self.cor = cor
    
  def movimento(self):
    """
        Método que cuida da movimentação de uma pedra (peça simples).
    """
    pass



class Dama(Pedra):
  """
      Instância especial da classe Pedra. Herda todos os atributos
      e métodos, com excessão do método movimento, que é sobreescrito
      nesta classe filha.
  """

  def __init__(self, cor):
    Pedra.__init__(self, cor)

  def movimento(self):
    """
        Método que cuida da movimentação da dama. Sobreescreve o método
        de mesmo nome da classe Pedra().
    """
    pass