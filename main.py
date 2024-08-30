"""
Autor: Antonio Aparecido Medeiros Santana
Componente Curricular: Algoritmos I
Concluido em: 05/07/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

# Importando a biclioteca de funções 
from funcoes import *
# Variável de controle 
continua = True
while continua: 
  # Bloco que printa o titulo do game
  limpar()
  titulo(f'{'BEM VINDO AO TABULEIRO DE NÚMEROS!':^50}\n{'AMPLIE SEU TERMINAL!':^50}')
  tocarSomMenus()
  pausa()
  limpar()

  # Bloco onde é chamado o menu principal e dependendo da escola uma funcao é chamada
  menuPrinc()
  choiceFirstMenu = verificacao([1 ,2 , 3, 4, 5, 6])

  if choiceFirstMenu == 1: # Se a escolha for 1 um novo game é iniciado
    limpar()
    createMenus(['JOGO FÁCIL', 'JOGO MÉDIO','JOGO DIFÍCIL'])
    dificuldade = verificacao([1, 2, 3])
    limpar()
    newGameMenu()
    iniciarJogo(dificuldade, verificacao([1, 2]))

  elif choiceFirstMenu == 2: # Se a escolhar for 2 um jogo antigo será carregado caso exista
    limpar()
    carregarOldGame()

  elif choiceFirstMenu == 3: # Na escolha 3 o placar é exibido
    limpar()
    mostraPlacar()
    
  elif choiceFirstMenu == 4: # Na escolha 4 algumas instrucões de como jogar serão exibidadas
    limpar()
    howToPlay()

  elif choiceFirstMenu == 5: # Na escolha 5 o programa é interrompido e Sai
    continua = False

  else: # se nao for nenhuma das anteriores uma mensagem de erro é executada
    print(cores('DADOS INVÁLIDOS!!!','vermelho'))
    pausa()

titulo('VOCÊ SAIU!') # Ao sair um titulo com a mensagem 'voce saiu' é exibido 
