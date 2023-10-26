#variaveis globais
VitoriasPC = 0
VitoriasJogador = 0

def tipoPartida():
  #Em um campeonato, ocorrem 3 partidas e vence quem ganhar a maior quantidade
  print("\nBem-vindo ao jogo do NIM! Escolha: ")
  print("\n1 - para jogar uma partida isolada")
  escolha = int(input("2 - para jogar um  campeonato "))
  return escolha

def verificaQuemComeca(n, m):
  if n % (m+1) == 0:
    return 0 #jogador começa
  else:
    return 1 #computador começa

def imprimePlacar(vitoriasPc, vitoriasJogador):
  print("Placar: Você:", vitoriasJogador, "x", vitoriasPc, "Computador")

def computador_escolhe_jogada(m, n):
  """
    Se a quantidade de peças restantes no tabuleiro for menor ou igual
  ao máximo que pode ser retirado, ele retira todas (e vence)
    Senão, vai tentar retirar uma quantidade de peças que mantenha a regra de que
  deve ficar disponivel para o jogador sempre uma quantidade n que seja multipla
  de m+1.
  """
  contador = m
  if n <= m:
    return n
  else:
    while contador >= 1:
      if (n - contador) % (m+1) == 0:
        return contador
      else:
        contador = contador - 1
    #Caso nao encontre um valor ideal, ele vai retirar uma peça
    return m
  
def usuario_escolhe_jogada(m, n):
  valido = False
  while valido != True:
    pecasRetiradas = int(input("Quantas peças você vai tirar? "))
    if(pecasRetiradas > m or pecasRetiradas < 1):
      print("\nOops! Jogada inválida! Tente de novo.\n")
    else:
      valido = True
  return pecasRetiradas

def imprimeRetiradaPC(retiradasPC):
  if retiradasPC == 1:
    print("O computador tirou uma peça.")
  else:
    print("O computador tirou", retiradasPC, "peças.")

def imprimeRetiradaJogador(retiradasJogador):
  if retiradasJogador == 1:
    print("\nVocê tirou uma peça")
  else:
    print("\nVocê tirou", retiradasJogador, "peças")

def imprimeSobra(n):
  if n == 1:
    print("Agora resta apenas uma peça no tabuleiro.\n")
  else:
    print("Agora restam", n, "peças no tabuleiro.\n")

def vitoriaPC():
  print("Fim do jogo! O computador ganhou!\n")

def vitoriaJogador():
  print("Fim de jogo! Você ganhou!\n")

def sequencia1(m, n):
  retiradasPC = computador_escolhe_jogada(m,n)
  n = n - retiradasPC
  imprimeRetiradaPC(retiradasPC)
  
  if n == 0:
    global VitoriasPC
    VitoriasPC += 1
    vitoriaPC()
  else:
    imprimeSobra(n)
    
    retiradasJogador = usuario_escolhe_jogada(m,n)
    n = n - retiradasJogador
    imprimeRetiradaJogador(retiradasJogador)
    
    if n == 0:
      global VitoriasJogador
      VitoriasJogador += 1
      vitoriaJogador()
    else:
      imprimeSobra(n)
    
  if n > 0:
    sequencia1(m, n)

def sequencia2(m, n):
  retiradasJogador = usuario_escolhe_jogada(m,n)
  n = n - retiradasJogador
  imprimeRetiradaJogador(retiradasJogador)
  
  if n == 0:
    global VitoriasJogador
    VitoriasJogador += 1
    vitoriaJogador()
  else:
    imprimeSobra(n)
    
    retiradasPC = computador_escolhe_jogada(m,n)
    n = n - retiradasPC
    imprimeRetiradaPC(retiradasPC)
    
    if n == 0:
      global VitoriasPC
      VitoriasPC += 1
      vitoriaPC()
    else:
      imprimeSobra(n)
    
  if n > 0:
    sequencia2(m, n)
  
def partida():
  escolha = tipoPartida()
  partidaAtual = 1
  
  if escolha == 2:
    print("\nVoce escolheu um campeonato!")
    totalPartidas = 3
  else:
    print("\nVocê escolheu uma partida isolada")
    totalPartidas = 1

  while (partidaAtual <= totalPartidas):
    print("\n**** Rodada", partidaAtual,"****\n")
    n = int(input("Quantas peças no tabuleiro? "))
    m = int(input("Limite de peças retiradas por jogada? "))
  
    quemComeca = verificaQuemComeca(n, m)
  
    if quemComeca == 1 or n <= m:
      print("\nComputador começa!\n")
      sequencia1(m, n)
        
    else:
      print("\nVocê começa!\n")
      sequencia2(m, n)
    
    partidaAtual += 1

  if totalPartidas > 1:
    print("**** Final do Campeonato ****\n")
    global VitoriasPC
    global VitoriasJogador
    imprimePlacar(VitoriasPC, VitoriasJogador)

partida()