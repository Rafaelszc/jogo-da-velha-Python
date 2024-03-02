seq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
repetidas = []
jogador = 0
jogo = """ 
{} | {} | {} 
==+===+==
{} | {} | {}
==+===+==
{} | {} | {}""".format(seq[0][0],seq[0][1],seq[0][2],seq[1][0],seq[1][1],seq[1][2],seq[2][0],seq[2][1],seq[2][2])
print(jogo)

def verificaçao(jogador):
    global seq
    global repetidas
    pontos = 0
    #retas horizontais
    for i in range(3):
        if pontos < 3:
            pontos = 0
        elif pontos == 3:
            print(jogador,'ganhou')
            exit()
        for j in range(3):
            if seq[i][j] == jogador:
                pontos += 1
    if pontos < 3:
        pontos = 0
    elif pontos == 3:
        print(jogador,'ganhou')
        exit()
    #retas verticais
    for j in range(3):
        if pontos < 3:
            pontos = 0
        elif pontos == 3:
            print(jogador,'ganhou')
            exit()
        for i in range(3):
            if seq[i][j] == jogador:
                pontos += 1
    if pontos < 3:
        pontos = 0
    elif pontos == 3:
        print(jogador,'ganhou')
        exit()
    #diagonal esquerda-direita
    for c in range(3):
        if seq[c][c] == jogador:
            pontos += 1
    if pontos == 3:
        print(jogador,'ganhou')
        exit()
    else: 
        pontos = 0
    #diagonal direita-esquerda
    q = 2
    for s in range(3):
        if seq[s][q] == jogador:
            pontos += 1
        q -= 1
    if pontos == 3:
        print(jogador,'ganhou')
        exit()
    #verificação de velha
    if len(repetidas) == 9:
        print('velha')
        exit()


while True:
    #escolha
    try:
        num = int(input('Escolha um número: '))
    except ValueError:
        print('Escolha inválida')
    else:
    #verificações
        verify1 = num in repetidas
        verify2 = num >=1 and num <= 9

        if verify1 == False and verify2 == True:
            repetidas.append(num)
            for c in range(3):

            #ideintificar e definir posição do número
                verify3 = num in seq[c]
                if verify3 == True:
                    pos = seq[c].index(num)
                #ação jogador O
                    if jogador == 0:
                        seq[c][pos] = 'X'
                        jogador = 1
                        jogo = """ 
                        {} | {} | {} 
                        ==+===+==
                        {} | {} | {}
                        ==+===+==
                        {} | {} | {}""".format(seq[0][0],seq[0][1],seq[0][2],seq[1][0],seq[1][1],seq[1][2],seq[2][0],seq[2][1],seq[2][2])
                        print(jogo)
                    #verificação de vitórias
                        verificaçao('X')
                        verificaçao('O')
                #ação jogador O
                    elif jogador == 1:
                        seq[c][pos] = 'O'
                        jogador = 0
                        jogo = """ 
                        {} | {} | {} 
                        ==+===+==
                        {} | {} | {}
                        ==+===+==
                        {} | {} | {}""".format(seq[0][0],seq[0][1],seq[0][2],seq[1][0],seq[1][1],seq[1][2],seq[2][0],seq[2][1],seq[2][2])
                        print(jogo)
                        verificaçao('X')
                        verificaçao('O')
                
        elif verify2 == False:
            print('Escolha um número entre 1 e 9')
        elif verify1 == True:
            print('Repetido')