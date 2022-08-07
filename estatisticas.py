import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ferramentas import *


class Estatisticas:
  """
      Classe que tratará a geração de tabelas e gráficos
      usando o Matplotlib e o Pandas para estatísticas
      coletadas nas partidas.
      
      Vitórias x Derrotas
      Empates
      Tempo de conclusão
  """
  pass

def geraTabela():
  """
      Gera uma tabela a partir da escolha do jogador. As
      opções serão passadas na interface gráfica.
  """
  pass


def geraGrafico(tipo, arquivo):
  """
      Gera um gráfico a partir da escolha do jogador. As
      opções serão passadas na interface gráfica.
  """
  file = open(arquivo)
  file_data = file.read().splitlines()
  file.close()
  file_data = [x.split(sep=', ') for x in file_data]
  partidas = int(file_data[-1][0])
  # return file_data
  
  vit = []
  der = []
  emp = []
  
  for i in range(len(file_data)):
    for j in file_data[i]:
      if j == 'v':
        vit.append(1)
        der.append(0)
        emp.append(0)
      elif j == 'd':
        der.append(1)
        vit.append(0)
        emp.append(0)
      elif j == 'e':
        emp.append(1)
        vit.append(0)
        der.append(0)
  
  if tipo == 1:  # partidas X vitórias
    fig, ax = plt.subplots()
    x = np.linspace(1,partidas,partidas)
    y = np.cumsum(vit)
    
    ax.plot(x, y, 'g-', linewidth=2)
    ax.set_yticks(np.arange(1, partidas, 1))
    ax.set_xticks(np.arange(1, partidas, 1))
    # plt.show()
    plt.savefig(f'images/estatisticas/vitorias.png')
   
  elif tipo == 2:  # partidas X derrotas
    fig, ax = plt.subplots()
    x = np.linspace(1, partidas, partidas)
    y = np.cumsum(der)
    
    ax.plot(x, y, 'r-', linewidth=2)
    ax.set_yticks(np.arange(1, partidas, 1))
    ax.set_xticks(np.arange(1, partidas, 1))
    # plt.show()
    plt.savefig(f'images/estatisticas/derrotas.png')

  
  elif tipo == 3: # partidas X empates
    fig, ax = plt.subplots()
    x = np.linspace(1, partidas, partidas)
    y = np.cumsum(emp)
    
    ax.plot(x, y, 'b-', linewidth=1)
    ax.set_yticks(np.arange(1, partidas, 1))
    ax.set_xticks(np.arange(1, partidas, 1))
    # plt.show()
    plt.savefig(f'images/estatisticas/empates.png')



# print(geraGrafico(1, 'saves/dados/teste1.txt'))
# print(geraGrafico(2, 'saves/dados/teste1.txt'))
# print(geraGrafico(3, 'saves/dados/teste1.txt'))
