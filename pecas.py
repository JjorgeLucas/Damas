class Pedra:
  """
      Classe que representa as peças do jogo assim como armazena
      seus atributos e métodos.
  """

  def __init__(self, cor):
    self.cor = cor


class Dama(Pedra):
  """
      Instância especial da classe Pedra. Herda todos os atributos
      e métodos, com excessão do método movimento, que é sobreescrito
      nesta classe filha.
  """

  def __init__(self, cor):
    Pedra.__init__(self, cor)
