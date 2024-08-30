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

import os # Importando a biblioteca os 
from tabulate import tabulate # Importando a biblioteca Tabulate 
from random import randint # Importando o método randint 
import time # Importando a biblioteca time
import json # Importando a biblioteca Json
import winsound # Importando a biblioteca winsound

# Função que printa uma string no formato de titulo 1-parametro asting e 2-quantidade de caracteres desejados para formatação
def titulo(str, qnt = 50):
  print('\033[1;31;47m')
  print('='*qnt)
  print(f'{str:^{qnt}}')
  print('='*qnt)
  print('\033[m')

# Função que poe cores em strings 
def cores(str, cor):
  if cor == 'vermelho':
    return f'\033[1;37;41m{str}\033[m'
  elif cor == 'verde':
    return f'\033[1;37;42m{str}\033[m'
  elif cor == 'amarelo':
    return f'\033[1;37;43m{str}\033[m'
  elif cor == 'roxo':
    return f'\033[1;37;45m{str}\033[m'
  elif cor == 'azul':
    return f'\033[1;37;44m{str}\033[m'
  elif cor == 'branco':
    return f'\033[1;37;44m{str}\033[m'
  else:
    return str


# Função que printa uma foramatação
def formata(msg):
  print('#'*50)
  print(f'{msg:^50}')
  print('#'*50)

# Função que printa um erro
def erro(msg):
  print('\033[1;37;41m')
  print('#'*50)
  print(f'{msg:^50}')
  print('#'*50)
  print('\033[m')

# Função que toca SONS 
def tocarSomMenus():
  try:
    winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
  except:
    erro('NÃO FOI POSSÍVEL REPRODUZIR SONS!')


# som que toca ao fim do jogo
def somFim():
  try:
    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
  except:
    erro('NÃO FOI POSSÍVEL REPRODUZIR SONS!')

# Função que tocam som dos players
def beep(p):
  try:
    if p == 0:
      winsound.Beep(700, 300)
    else:
      winsound.Beep(300, 300)
  except:
    return None

# Função que limpa o terminal
def limpar():
  try:
    return os.system('cls||clear') or None
  except:
    erro('SEU SISTEMA OPERACIONAL NÃO É COMPATIVEL COM A LIMPEZA DE TERMINAL')
    return None


# Função que da uma pausa no fluxo do código
def pausa(str = ''):
  a = input(f'{str} Clique ENTER para continuar: ')
  return None

# Função que ensina as regras do jogo
def howToPlay():
  limpar()
  titulo('COMO JOGAR')
  print('\033[1;30;47m')
  print('-'*100)
  print(f'{'INFOS: O tabuleiro de números é um jogo no estilo tabuleiro, onde dois jogadores terão objetivos a':<100}\n{'cumprir, são eles: [Sequência ascendente, Sequência descendente, Sequência par e Sequência ímpar].':<100}\n{'O objetivo será sorteado aleatóriamente antes de iniciar a partida. Os jogadores não podem saber o ':<100}\n{'objetivo do adversário porém as jogadas feitas pelo adversário irão influênciar no seu jogo.':<100}\n{'Ganha quem conseguir cumprir seu objetivo primeiro.':<100}')
  print('-'*100)
  print('\033[m')
  pausa()


# Função que cria menus a partir de uma array
def createMenus(array):
  print('\033[1;30;47m')
  for i in range(len(array)):
    print(f'[{i+1}]--> {array[i]:<100}')
  print('\033[m')
  return



# Menu principal de escolhas 
def menuPrinc():
  print('\033[1;30;47m')
  print(f'{'MENU PRINCÍPAL':^100}')
  print('-'*100)
  print(f'{'[1]--> NOVO JOGO':<100}')
  print(f'{'[2]--> CARREGAR JOGO ANTIGO':<100}')
  print(f'{'[3]--> PLACAR':<100}')
  print(f'{'[4]--> APRENDA A JOGAR':<100}')
  print(f'{'[5]--> SAIR':<100}')
  print('-'*100)
  print('\033[m')


# Menu de escolhas para um novo jogo
def newGameMenu():
  print('\033[1;30;47m')
  print(f'{'POWER-UPS':^100}')
  print('-'*100)
  print(f'{'[1]--> ATIVADOS':<100}')
  print(f'{'[2]--> DESATIVADOS':<100}')
  print('-'*100)
  print('\033[m')


# Função que recebe um array de numeros e verifica se a escolha feita está dentro desse array
def verificacao(arrayDeEscolhas):
  cont = True
  while cont:
    try:
      print('\033[1;30;47m')
      esc = int(input('INFORME SUA ESCOLHA: ')) 
      print('\033[m')

      if arrayDeEscolhas.__contains__(esc):
        cont = False
        continue
      else:
        erro('O VALOR INFORMADO NÃO É VÁLIDO')
    except:
        erro('O VALOR INFORMADO NÃO É VÁLIDO')
  return esc


# Função que cria uma matriz que será a tabela do jogo e retorna
def createTable(num):
  lista = []
  header = ['V', 'W', 'X', 'Y', 'Z']
  for i in range(num):
    line = []
    for a in range(num + 1):
      if a == 0:
        line.append(header[i])
      else:
        line.append('')
    lista.append(line)
  return lista


# Função que formata a tabela a partir do tamanho e dificuldade escolhidos
def formatTable(table):
  if len(table) == 3:
    header = ['-','A', 'B', 'C']
  elif len(table) == 4:
    header = ['-','A', 'B', 'C', 'D']
  else:
     header = ['-','A', 'B', 'C', 'D','E']
  return tabulate(table, headers=header, tablefmt='simple_grid')


# Função que pede o nome de cada jogador, e  sorteia o tipo de jogo de cada um, e retorna uma lista com dois discionários com nome do jogador e o objetivo
def sorteiaJogadorJogo():
  titulo('NOME DOS JOGADORES')
  games = ['Sequencia Ascendente', 'Sequência Descendente', 'Sequência Pares', 'Sequência Ímpares']
  players = []
  nome = input('Informe o nome do jogador 1: ')
  if nome == '':
    players.append('Jogador-sem-nome-1')
  else:
    players.append(nome)
  nome = input('Informe o nome do jogador 2: ')
  if nome == '':
    players.append('Jogador-sem-nome-2')
  else:
    players.append(nome)
  sortedGameP1 = games[randint(0,len(games)-1)]
  sortedplayer = players.pop(randint(0,1))
  lastPlayer = players[0]
  limpar()
  print('#'*50)
  print(f'O primeiro jogador será: {sortedplayer}')
  print('#'*50)
  erro('Sorteando seu objetivo NÃO MOSTRE AO ADVERSÁRIO!!...')
  for i in range(3):
    time.sleep(1)
    print(f'{i+1}...')
  pausa()
  formata(f'O seu jogo {sortedplayer} é: {cores(games.pop(games.index(sortedGameP1)), 'verde')}')
  {time.sleep(3)}
  limpar()
  pausa()
  limpar()
  print('#'*50)
  print(f'Sorteando jogo do player {lastPlayer}')
  print('#'*50)
  sortedGameP2 = games[randint(0,len(games)-1)]
  erro('Sorteando seu objetivo NÃO MOSTRE AO ADVERSÁRIO!!...')
  time.sleep(1)
  for i in range(3):
    time.sleep(1)
    print(f'{i+1}...')
  pausa()
  formata(f'O seu jogo {lastPlayer} é: {cores(sortedGameP2, 'verde')}')
  {time.sleep(3)}
  limpar()
  pausa()
  limpar()

  formata(cores(f'O primeiro player será: {sortedplayer:<50} COR: amarelo', 'amarelo'))
  formata(cores(f'Próximo player: {lastPlayer:<50} COR: azul', 'azul'))
  return [{'nome': sortedplayer, 'objetivo':  sortedGameP1}, {'nome': lastPlayer, 'objetivo': sortedGameP2}]


# Função que recebe as cordenadas, valor e jogador e coloca na tabela distingindo entre jogador 0 e jogador 1 
def colocaNaTabela(cordenada, nJogados, table, valor):
  if cordenada != False:
    c1 = cordenada[0]
    c2 = cordenada[1]
    if nJogados == 0:
      table[c2][c1+1] = cores(valor, 'amarelo')
    else:
      table[c2][c1+1] = cores(valor, 'azul')

# Função que toca o som da vitória
def tocarSomVictory():
  try:
    winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
  except:
    erro('NÃO FOI POSSÍVEL REPRODUZIR SONS!')

# Função que toca o som da vitória
def tocarSomEmpate():
  try:
    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
  except:
    erro('NÃO FOI POSSÍVEL REPRODUZIR SONS!')


# Função que inicia o jogo
def iniciarJogo(dif, powerUp):
  limpar()
  tabela = createTable(dif + 2)
  playerAndGame = sorteiaJogadorJogo() # Retorna um array com 2 obj com nome e objetivo dos jogadores
  pausa()
  limpar()
  titulo('O jogo começou!')
  jogada(playerAndGame, dif+2, powerUp, tabela)


# Função que lista as linhas e as colunas da tabela e retorna as cordenadas da escolha feita pelo jogador
def cordenadas(tam, array):
  posibilidadesR = ['A', 'B', 'C', 'D', 'E']
  posibilidadesC = ['V', 'W', 'X', 'Y', 'Z']
  arrayRow = []
  arrayCol = []
  for a in range(tam):
    arrayRow.append(posibilidadesR[a])
    arrayCol.append(posibilidadesC[a])

  print(f'{cores(tabulate([arrayRow], tablefmt='simple_grid'), 'roxo')}')
  linha = input('Informe a linha: ').upper()
  print(f'{cores(tabulate([arrayCol], tablefmt='simple_grid'), 'roxo')}')
  coluna = input('Informe a coluna: ').upper()
  while not (arrayCol.__contains__(coluna) and arrayRow.__contains__(linha) and array[arrayCol.index(coluna)][arrayRow.index(linha) + 1] == ''):
    erro('Linha ou Coluna inválidos ou já escolhidos')
    print(f'{cores(tabulate([arrayRow], tablefmt='simple_grid'), 'roxo')}')
    linha = input('ESCOLHA NOVAMENTE LINHA: ').upper()
    print(f'{cores(tabulate([arrayCol], tablefmt='simple_grid'), 'roxo')}')
    coluna = input('ESCOLHA NOVAMENTE COLUNA: ').upper()

  return [arrayRow.index(linha), arrayCol.index(coluna)]


# Função que recebe o tamanho da tabela e retorna um array com as possibilidades de numeros que esse tamanho permite
def defineNum(tam):
  lista = []
  for a in range(1, tam*tam + 1):
    lista.append(a)
  return lista


# Recebe um array com as possibilidades de numeros e enquanto a escolha não estiver no array nada acontece
def pegaNum(array, apagados = []):
  if apagados != []:
    array.extend(apagados)
    array.sort()
  print(f'Os números disponiveis são:')
  print(cores(tabulate([array], tablefmt='simple_grid'), 'roxo'))
  escolha = 0
  while not array.__contains__(escolha):
    try:
      escolha = int(input('Informe o valor desejado: '))
      if not escolha in array:
        erro('VALOR INVÁLIDO')
    except:
      erro('VALOR INVÁLIDO')
  array.remove(escolha)
  return escolha


# Função que verifica se existe jogo salvo e se houver carrega esse jogo
def carregarOldGame():
  limpar()
  with open('dados.json', 'rt') as arq:
    dados = json.load(arq)
  if dados['ultimo_jogo'] != []:
    jogada(dados['ultimo_jogo'][0],dados['ultimo_jogo'][1], dados['ultimo_jogo'][2], dados['ultimo_jogo'][3],  dados['ultimo_jogo'][4])
  else:
    titulo('NÃO EXISTE JOGO SALVO NA MEMÓRIA')
    pausa()
    return


# Função que apaga uma linha da tabela ecolhida pelo jogador
def usarPoder(array):
  apagados = []
  esco = input('Digíte POWER para ativar o poder: ').upper()
  if esco == 'POWER':
    linhas = []
    for a in array:
      linhas.append(a[0])
    print(cores(tabulate([linhas], tablefmt='simple_grid'), 'roxo'))
    var = input('Digíte a linha que deseja apagar: ').upper()
    while not linhas.__contains__(var):
      erro('LINHA INFORMADA NÃO EXISTE!')
      print(cores(tabulate([linhas], tablefmt='simple_grid'), 'roxo'))
      var = input('Digíte a linha que deseja apagar: ').upper()
    var = linhas.index(var)
    for a in array:
      if array.index(a) == var:
        for i in range(len(a)):
          if i != 0:
            if a[i] != '':
              # Remove caracteres de escape e colchetes
              numero = a[i].strip('\x1b[]m')
              a[i] = ''
              # Imprime o número
              numero = int(numero[8:])
              apagados.append(numero)  
    erro('A LINHA FOI APAGADA')
    return apagados
  else:
    return False


# Função que verifica se todos os lugares da tabela estão preenchidos
def verificaSeAcabou(array):
  for a in array:
    for dado in a:
      if dado == '':
        return False
  return True


# Função que mostra o placar
def mostraPlacar():
  try:
    with open('dados.json', 'rt') as arq:
      dados = json.load(arq)
      placarOrdenado = dict(sorted(dados['placar'].items(), key=lambda item: item[1], reverse=True))
      lista = []
      i = 1
      for d in placarOrdenado:
        novaList = [f'{i}°', d, placarOrdenado[d]]
        i+=1
        lista.append(novaList)
      titulo('PLACAR')
      print(tabulate(lista, headers=['COLOCAÇÃO','NOME', 'PONTOS'], tablefmt='simple_grid'))
  except:
    titulo('OCORREU UM ERRO AO CARREGAR O PLACAR')
  finally:
    pausa('')
    return


# Função que salva o jogo
def salvar(playersGame, tamTable, power, tabela, numeros):
  lista = [playersGame, tamTable, power, tabela, numeros]
  with open('dados.json', 'rt') as arq:
    dados = json.load(arq)
    dados['ultimo_jogo'] = lista
  with open('dados.json', 'w' ) as arq:
    json.dump(dados, arq)  


# Função que atualiza o placar
def atualizaPlacar(nome, pontos):
  with open('dados.json', 'rt') as arq:
    dados = json.load(arq)
  if dados['placar'].get(nome) != None:
    dados['placar'][nome] += pontos 
  else:
    dados['placar'][nome] = pontos 
  with open('dados.json', 'w' ) as arq:
    json.dump(dados, arq)
  return 


# Funçaõ que verifica se as sequencias acendente e descendente foram alcançadas
def sequenciaAscenDescen(tabela, objetivo, tam):
  games = ['Sequencia Ascendente', 'Sequência Descendente']
  obj = games.index(objetivo)
  adjacente = []
  subjacente = []
  for a in range(len(tabela)):
    linha = tabela[a].copy()
    linha.pop(0)
    #verifica se é diferente de ''
    if linha[a] != '':
      n1 = linha[a].strip('\x1b[]m')
      adjacente.append(int(n1[8:]))
    #verifica se é diferente de ''
    if linha[(len(linha)-1) - a] != '':
      n1 = linha[(len(linha)-1) - a].strip('\x1b[]m')
      subjacente.append(int(n1[8:]))
    for elemento in range(len(linha)):
      if linha[elemento] != '':
        num = linha[elemento].strip('\x1b[]m')
        linha[elemento] = int(num[8:])
        # print(linha[elemento])

    # Validando vitória TAM 3
    if len(linha) == 3:
      if linha[0] != '' and linha[1] != '' and linha[2] != '':
        if (linha[2] == linha[1]+1 and linha[1] == linha[0]+1) and obj == 0:
          #print('Sequencia ascendente venceu')
          return True
        elif (linha[2] == linha[1]-1 and linha[1] == linha[0]-1) and obj == 1:
          #print('Sequencia descendente venceu')
          return True
    elif len(linha) == 4: # Validando vitória TAM 4
      if linha[0] != '' and linha[1] != '' and linha[2] != '' and linha[3] != '':
        if (linha[3] == linha[2]+1 and linha[2] == linha[1]+1 and linha[1] == linha[0]+1) and obj == 0:
          #print('Sequencia ascendente venceu')
          return True
        elif (linha[3] == linha[2]-1 and linha[2] == linha[1]-1 and linha[1] == linha[0]-1) and obj == 1:
          #print('Sequencia descendente venceu')
          return True
    elif len(linha) == 5: # Validando vitoria TAM 5 
      if linha[0] != '' and linha[1] != '' and linha[2] != '' and linha[3] != '' and linha[4] != '':
        if (linha[4] == linha[3] +1 and linha[3] == linha[2]+1 and linha[2] == linha[1]+1 and linha[1] == linha[0]+1) and obj == 0:
          #print('Sequencia ascendente venceu')
          return True
        elif (linha[4] == linha[3]-1 and linha[3] == linha[2]-1 and linha[2] == linha[1]-1 and linha[1] == linha[0]-1) and obj == 1:
          #print('Sequencia descendente venceu')
          return True
        
    # verifica adjacente TAM 3
    if len(adjacente) == 3 and tam == 3:
      if (adjacente[0] == adjacente[1]-1 and adjacente[1] == adjacente[2]-1) and obj == 0:
        #print('Sequencia ascendente venceu')
        return True
      elif (adjacente[0] == adjacente[1]+1 and adjacente[1] == adjacente[2]+1) and obj == 1:
        #print('Sequencia descendente venceu')
        return True
    elif len(adjacente) == 4 and tam == 4: # Verifica adjacente TAM 4
      if (adjacente[0] == adjacente[1]-1 and adjacente[1] == adjacente[2]-1 and adjacente[2] == adjacente[3]-1) and obj == 0:
        #print('Sequencia ascendente venceu')
        return True
      elif (adjacente[0] == adjacente[1]+1 and adjacente[1] == adjacente[2]+1 and adjacente[2] == adjacente[3]+1) and obj == 1:
        #print('Sequencia descendente venceu')
        return True
    elif len(adjacente) == 5 and tam == 5: # Verifica adjacente TAM 5
      if (adjacente[0] == adjacente[1]-1 and adjacente[1] == adjacente[2]-1 and adjacente[2] == adjacente[3]-1 and adjacente[3] == adjacente[4]-1) and obj == 0:
        #print('Sequencia ascendente venceu')
        return True
      elif (adjacente[0] == adjacente[1]+1 and adjacente[1] == adjacente[2]+1 and adjacente[2] == adjacente[3]+1 and adjacente[3] == adjacente[4]+1) and obj == 1:
        #print('Sequencia descendente venceu')
        return True

    # VERIFICA SUBJACENTE TAM 3
    if len(subjacente) == 3 and tam == 3:
      # subjacente.reverse()
      if (subjacente[0] == subjacente[1]+1 and subjacente[1] == subjacente[2]+1) and obj == 0:
        #print('Sequencia ascendente venceu')
        return True
      elif (subjacente[0] == subjacente[1]-1 and subjacente[1] == subjacente[2]-1) and obj == 1:
        #print('Sequencia descendente venceu')
        return True
    elif len(subjacente) == 4 and tam == 4: # Verifica subjacente TAM 4
      # subjacente.reverse()
      if (subjacente[0] == subjacente[1]+1 and subjacente[1] == subjacente[2]+1 and subjacente[2] == subjacente[3]+1) and obj == 0:
        #print('Sequencia ascendente venceu')
        return True
      elif (subjacente[0] == subjacente[1]-1 and subjacente[1] == subjacente[2]-1 and subjacente[2] == subjacente[3]-1) and obj == 1:
        #print('Sequencia descendente venceu')
        return True
    elif len(subjacente) == 5 and tam == 5: # Verifica subjacente TAM 4
      # subjacente.reverse()
      if (subjacente[0] == subjacente[1]+1 and subjacente[1] == subjacente[2]+1 and subjacente[2] == subjacente[3]+1 and subjacente[3] == subjacente[4]+1) and obj == 0:
        #print('Sequencia ascendente venceu')
        return True
      elif (subjacente[0] == subjacente[1]-1 and subjacente[1] == subjacente[2]-1 and subjacente[2] == subjacente[3]-1 and subjacente[3] == subjacente[4]-1) and obj == 1:
        #print('Sequencia descendente venceu')
        return True
  return False


# Função que verifica se ouve vitoria pela sequencia par ou impar
def sequenciaParImp(tabela, objetivo, tam):
  games = ['Sequência Pares', 'Sequência Ímpares']
  obj = games.index(objetivo)
  adjacente = []
  subjacente = []
  for a in range(len(tabela)):
    linha = tabela[a].copy()
    linha.pop(0)
    #verifica se é diferente de ''
    if linha[a] != '':
      n1 = linha[a].strip('\x1b[]m')
      adjacente.append(int(n1[8:]))
    #verifica se é diferente de ''
    if linha[(len(linha)-1) - a] != '':
      n1 = linha[(len(linha)-1) - a].strip('\x1b[]m')
      subjacente.append(int(n1[8:]))
    for elemento in range(len(linha)):
      if linha[elemento] != '':
        num = linha[elemento].strip('\x1b[]m')
        linha[elemento] = int(num[8:])
        #print(linha[elemento])

    # Verifica TAM 3
    if len(linha) == 3:
      if linha[0] != '' and linha[1] != '' and linha[2] != '':
        if (linha[2] == linha[1]+2 and linha[1] == linha[0]+2) and (obj == 0) and (linha[0] % 2 == 0):
          #print('Sequencia Par venceu')
          return True
        elif (linha[2] == linha[1]-2 and linha[1] == linha[0]-2) and (obj == 1) and (linha[0] % 2 == 1):
          #print('Sequencia Ímpar venceu')
          return True
        
    # VERIFICA TAM 4
    elif len(linha) == 4:
      if linha[0] != '' and linha[1] != '' and linha[2] != '' and linha[3] != '':
        if (linha[3] == linha[2]+2 and linha[2] == linha[1]+2 and linha[1] == linha[0]+2) and (obj == 0) and (linha[0] % 2 == 0):
          #print('Sequencia Par venceu')
          return True
        elif (linha[3] == linha[2]+2 and linha[2] == linha[1]+2 and linha[1] == linha[0]+2) and (obj == 1) and (linha[0] % 2 == 1):
          #print('Sequencia Ímpar venceu')
          return True

    # VERIFICA TAM 5
    elif len(linha) == 5:
      if linha[0] != '' and linha[1] != '' and linha[2] != '' and linha[3] != '' and linha[4] != '':
        if (linha[4] == linha[3]+2 and linha[3] == linha[2]+2 and linha[2] == linha[1]+2 and linha[1] == linha[0]+2) and (obj == 0) and (linha[0] % 2 == 0):
          #print('Sequencia Par venceu')
          return True
        elif (linha[4] == linha[3]+2 and linha[3] == linha[2]+2 and linha[2] == linha[1]+2 and linha[1] == linha[0]+2) and (obj == 1) and (linha[0] % 2 == 1):
          #print('Sequencia Ímpar venceu')
          return True

      # verifica adjacente TAM 3
    if len(adjacente) == 3 and tam == 3:
      if (adjacente[0] == adjacente[1]-2 and adjacente[1] == adjacente[2]-2) and (obj == 0) and adjacente[0] % 2 == 0:
        #print('Sequencia Par venceu')
        return True
      elif (adjacente[0] == adjacente[1]-2 and adjacente[1] == adjacente[2]-2) and (obj == 1) and (adjacente[0] % 2 == 1):
        #print('Sequencia Ímpar venceu')
        return True
        
  # verifica adjacente TAM 4
    elif len(adjacente) == 4 and tam == 4:
      if (adjacente[0] == adjacente[1]-2 and adjacente[1] == adjacente[2]-2 and adjacente[2] == adjacente[3]-2) and (obj == 0) and adjacente[0] % 2 == 0:
        #print('Sequencia Par venceu')
        return True
      elif (adjacente[0] == adjacente[1]-2 and adjacente[1] == adjacente[2]-2 and adjacente[2] == adjacente[3]-2) and (obj == 1) and (adjacente[0] % 2 == 1):
        #print('Sequencia Ímpar venceu')
        return True
        
      # verifica adjacente TAM 5
    elif len(adjacente) == 5 and tam == 5:
        if (adjacente[0] == adjacente[1]-2 and adjacente[1] == adjacente[2]-2 and adjacente[2] == adjacente[3]-2 and adjacente[3] == adjacente[4]+2) and (obj == 0) and adjacente[0] % 2 == 0:
          #print('Sequencia Par venceu')
          return True
        elif (adjacente[0] == adjacente[1]-2 and adjacente[1] == adjacente[2]-2 and adjacente[2] == adjacente[3]-2 and adjacente[3] == adjacente[4]-2) and (obj == 1) and (adjacente[0] % 2 == 1):
          #print('Sequencia Ímpar venceu')
          return True
    
    # Verifica subjacente TAM 3
    if len(subjacente) == 3 and tam == 3:
      # subjacente.reverse()
      if (subjacente[0] == subjacente[1]+2 and subjacente[1] == subjacente[2]+2) and (obj == 0) and (subjacente[0] % 2 == 0):
        #print('Sequencia Par venceu')
        return True
      elif (subjacente[0] == subjacente[1]+2 and subjacente[1] == subjacente[2]+2) and (obj == 1) and subjacente[0] % 2 == 1:
        #print('Sequencia Ímpar venceu')
        return True
      
    # Verifica subjacente TAM 4
    if len(subjacente) == 4 and tam == 4:
      # subjacente.reverse()
      if (subjacente[0] == subjacente[1]+2 and subjacente[1] == subjacente[2]+2 and subjacente[2] == subjacente[3]+2) and (obj == 0) and (subjacente[0] % 2 == 0):
        #print('Sequencia Par venceu')
        return True
      elif (subjacente[0] == subjacente[1]+2 and subjacente[1] == subjacente[2]+2 and subjacente[2] == subjacente[3]+2) and (obj == 1) and subjacente[0] % 2 == 1:
        #print('Sequencia Ímpar venceu')
        return True
      
    # Verifica subjacente TAM 5
    if len(subjacente) == 4 and tam == 5:
      # subjacente.reverse()
      if (subjacente[0] == subjacente[1]+2 and subjacente[1] == subjacente[2]+2 and subjacente[2] == subjacente[3]+2 and subjacente[3] == subjacente[4]+2) and (obj == 0) and (subjacente[0] % 2 == 0):
        #print('Sequencia Par venceu')
        return True
      elif (subjacente[0] == subjacente[1]+2 and subjacente[1] == subjacente[2]+2 and subjacente[2] == subjacente[3]+2 and subjacente[3] == subjacente[4]+2) and (obj == 1) and subjacente[0] % 2 == 1:
        #print('Sequencia Ímpar venceu')
        return True
  return False


# Função que verifica se houve vitória de algum jogador
def verificaVitoria(tabela, objetivo, tam):
  games = ['Sequencia Ascendente', 'Sequência Descendente', 'Sequência Pares', 'Sequência Ímpares']
  if (objetivo == games[0] or objetivo == games[1]):
    return sequenciaAscenDescen(tabela, objetivo, tam)
  else:
    return sequenciaParImp(tabela, objetivo, tam)


# Função onde as jogadas e escolhas são feitas
def jogada(playersGame, tamTable, power, tabela, numeros=[]):
  limpar()
  if numeros == []:
    numeros = defineNum(tamTable)
  i = 0
  usouPower1 = False
  usouPower2 = False
  while i >= 0 :
    if i % 2 == 0:
      titulo(f'Vez do jogador [{playersGame[0]['nome']}]')
      print(formatTable(tabela))
      pausa('NÃO DEIXE SEU ADVERSÁRIO VER SUA TELA!')
      formata(cores(f'OBJETIVO: {playersGame[0]['objetivo']}', 'verde'))
      varPower = False
      if power == 1 and usouPower1 == False:
        varPower = usarPoder(tabela)
      if varPower == False:
        cordenada = cordenadas(tamTable, tabela)
        colocaNaTabela(cordenada, 0, tabela, pegaNum(numeros))
      else:
        if varPower != []:
          numeros.extend(varPower) #################
          numeros.sort()
        usouPower1 = True
          
      print(formatTable(tabela))
      beep(0)
      pausa()
      limpar()
    else:
      titulo(f'Vez do jogador [{playersGame[1]['nome']}]')
      print(formatTable(tabela))
      pausa('NÃO DEIXE SEU ADVERSÁRIO VER SUA TELA!')
      formata(cores(f'OBJETIVO: {playersGame[1]['objetivo']}', 'amarelo'))
      varPower = False
      if power == 1 and usouPower2 == False:
        varPower = usarPoder(tabela)
      if varPower == False:
        cordenada = cordenadas(tamTable, tabela)
        colocaNaTabela(cordenada, 1, tabela, pegaNum(numeros)) 
      else:
        if varPower != []:
          numeros.extend(varPower) #########################
          numeros.sort()
        usouPower2 = True
      print(formatTable(tabela))
      beep(1)
      pausa()
      limpar()

    if verificaVitoria(tabela, playersGame[0]['objetivo'], tamTable):
      titulo(playersGame[0]['objetivo'])
      print(formatTable(tabela))
      titulo(f'{playersGame[0]['nome']} FOI O CAMPEÃO')
      tocarSomVictory()
      atualizaPlacar(playersGame[0]['nome'], tamTable)
      pausa()
      limpar()
      titulo('UM NOVO JOGO SERÁ INICIADO EM INSTANTES')
      somFim()
      i = -1
      continue
    elif verificaVitoria(tabela, playersGame[1]['objetivo'], tamTable):
      titulo(playersGame[1]['objetivo'])
      print(formatTable(tabela))
      titulo(f'{playersGame[1]['nome']} FOI O CAMPEÃO')
      tocarSomVictory()
      atualizaPlacar(playersGame[1]['nome'], tamTable)
      pausa()
      limpar()
      titulo('UM NOVO JOGO SERÁ INICIADO EM INSTANTES')
      somFim()
      i = -1
      continue  
    if verificaSeAcabou(tabela):
      i = -1
      titulo('FIM DO JOGO EMPATE')
      tocarSomEmpate()
      pausa()
      limpar()
      titulo('UM NOVO JOGO SERÁ INICIADO EM INSTANTES')
      somFim()
    else:
      i += 1

    if i % 2 == 0:
      print('#'*50)
      sair = input(cores('Para sair dígite [SAIR]: ', 'vermelho'))
      print('#'*50)
      if sair.upper() == 'SAIR':
        i = -1
        titulo('SEU JOGO FOI SALVO')
        salvar(playersGame, tamTable, power, tabela, numeros)
        pausa()
        limpar()
        continue
        
