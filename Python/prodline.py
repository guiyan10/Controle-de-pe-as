estoque = {}
repeticao = True

def adicionar_peca(peca,quantidade):
    estoque[peca] = peca + quantidade
    print(f"A ferramenta {peca} foi adicionada com sucesso com {quantidade} unidades. ")

def remover_peca(peca,quantidade):
    if peca in estoque:
        # estoque[peca] = estoque - quantidade
        resultado = (estoque - quantidade) 
        
        print(f"Foi removido a ferramenta'{peca}' no total de", quantidade, "unidades e agora possui ", resultado, "unidades")
    else:
        print(f"A peça não foi removida, pois não há essa peça no estoque.")

def exibir_estoque(peca, quantidade):
    if estoque:
        print(f"Possuimos em nosso estoque a ferramenta", peca, "e possui", quantidade, "unidades")
while repeticao:

    operacao = int(input("O que deseja fazer? digite 1 para adicionar peças, 2 para remover, 3 para exibir todas as peças "))

    if operacao == 1:
        peca = input("qual peça deseja adicionar?")
        quantidade = input("Qual quantidade?")
        adicionar_peca(peca, quantidade)

    if operacao == 2:
        peca = input("qual peça deseja excluir?")
        quantidade = int(input("Qual quantidade que deseja remover?"))
        remover_peca(peca, quantidade)

    if operacao == 3:
      print(f"Temos em nosso estoque a ferramenta ", peca, "na quantidade de ", quantidade)
      exibir_estoque(peca,quantidade)

    else:
        print("Digite um numero de 1 a 0 ")

if estoque < 14:
    print("Estoque com nivel baixo")
continuar = input("Deseja fazer uma nova consulta ao estoque? pressione 1 para sim e 2 para não")
if continuar != 1:
        repeticao = False


