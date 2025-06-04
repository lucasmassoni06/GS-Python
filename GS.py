# Integrantes: Lucas Mesquita Massoni RM 561686, Felipe Balbino Murad RM 562347

# LOGIN
login = input("Seja Bem Vindo!\nVocê já possui login?\n(Digite 's' para sim ou 'n' para não): ")
while login != "s" and login != "n":
    login = input("Resposta inválida!\n(Digite 's' para já tenho login ou 'n' para não tenho login): ")

if login == "n":
    print("Sua primeira vez aqui!!")
else:
    print("Tem certeza? Você não possui login aqui!")

usuario_criado = input("Vamos criar seu perfil!\nCrie o seu nome de usuário: ")
senha_criada = input("Agora crie sua senha: ")
print("Conta criada com sucesso!")

usuario = input("Para fazer seu login:\nDigite seu nome de usuário: ")
while usuario != usuario_criado:
    erro = input(f"Usuário '{usuario}' não existe!\nDeseja tentar de novo (t) ou alterar o nome (a)? ")
    if erro == "a":
        usuario_criado = input("Digite seu novo nome de usuário: ")
        usuario = usuario_criado
    else:
        usuario = input("Digite seu nome de usuário: ")

senha = input("Agora digite sua senha: ")
while senha != senha_criada:
    erro = input("Senha incorreta!\nDeseja tentar de novo (t) ou alterar a senha (a)? ")
    if erro == "a":
        senha_criada = input("Digite sua nova senha: ")
        senha = senha_criada
    else:
        senha = input("Digite sua senha: ")

# BASE DE DADOS
zona_sul = ["Moema", "Vila Mariana", "Vila Olímpia", "Itaim Bibi", "Ipiranga", "Morumbi", "Santo Amaro", "Brooklin", "Campo Belo", "Vila Andrade"]
zona_norte = ["Santana", "Tucuruvi", "Vila Guilherme", "Tremembé", "Vila Maria", "Jaçanã", "Brasilândia", "Freguesia do Ó", "Anhanguera"]
zona_leste = ["Mooca", "Tatuapé", "Itaquera", "Penha", "Sapopemba", "Vila Formosa", "Lajeado", "Cangaíba"]
zona_oeste = ["Pinheiros", "Vila Madalena", "Perdizes", "Vila Leopoldina", "Butantã", "Lapa", "Vila Sônia", "Barra Funda", "Alto de Pinheiros"]
zona_central = ["Sé", "Bela Vista", "Bom Retiro", "Liberdade", "República", "Santa Cecília", "Consolação", "Brás"]

zona_sul_risco = [3, 1, 2, 1, 2, 3, 3, 1, 1, 2]
zona_norte_risco = [3, 3, 3, 2, 2, 3, 3, 3, 1]
zona_leste_risco = [3, 3, 3, 3, 3, 3, 3, 3]
zona_oeste_risco = [2, 3, 2, 3, 2, 3, 2, 2, 1]
zona_central_risco = [3, 3, 3, 3, 2, 3, 3, 2, 2]

# Variáveis para reportes

bairros_reportados = []
quantidade_reportes = []

# Função para aumentar risco
def aumentar_risco(bairro_nome):
    for i in range(len(zona_sul)):
        if zona_sul[i] == bairro_nome and zona_sul_risco[i] < 3:
            zona_sul_risco[i] += 1
            print("Risco de", bairro_nome, "agora é", zona_sul_risco[i])
    for i in range(len(zona_norte)):
        if zona_norte[i] == bairro_nome and zona_norte_risco[i] < 3:
            zona_norte_risco[i] += 1
            print("Risco de", bairro_nome, "agora é", zona_norte_risco[i])
    for i in range(len(zona_leste)):
        if zona_leste[i] == bairro_nome and zona_leste_risco[i] < 3:
            zona_leste_risco[i] += 1
            print("Risco de", bairro_nome, "agora é", zona_leste_risco[i])
    for i in range(len(zona_oeste)):
        if zona_oeste[i] == bairro_nome and zona_oeste_risco[i] < 3:
            zona_oeste_risco[i] += 1
            print("Risco de", bairro_nome, "agora é", zona_oeste_risco[i])
    for i in range(len(zona_central)):
        if zona_central[i] == bairro_nome and zona_central_risco[i] < 3:
            zona_central_risco[i] += 1
            print("Risco de", bairro_nome, "agora é", zona_central_risco[i])

# 1 - MENU

continuar = "s"
while continuar == "s":
    fazer = input("O que você deseja fazer, você pode\n 1- Reportar alagamentos\n 2- Filtrar regiões por risco de alagamento agora \n 3- Saber o nível de alagamento de uma região específica \nDigite o número respectivo ao que deseja: -> ")
    
    while (fazer not in ["1", "2", "3"]):
        fazer = input("Mensagem inválida, digite um valor válido:\n 1- Reportar alagamentos\n 2- Filtrar regiões por risco de alagamento agora \n 3- Saber o nível de alagamento de uma região específica \nDigite o número respectivo ao que deseja: -> ")

# 2 - REPORTAR ALAGAMENTO

    if fazer == "1":
        bairro = input("Digite o nome do bairro com alagamento: ")
        encontrado = False
        for i in range(len(bairros_reportados)):
            if bairros_reportados[i] == bairro:
                quantidade_reportes[i] += 1
                encontrado = True
                print("Bairro já foi reportado", quantidade_reportes[i], "vezes.")
                if quantidade_reportes[i] == 3:
                    print("3 reportes! Aumentando risco...")
                    aumentar_risco(bairro)
        if not encontrado:
            bairros_reportados.append(bairro)
            quantidade_reportes.append(1)
            print("Alagamento reportado pela primeira vez!")

# 3 - FILTRAR REGIÃO DE RISCO

    elif fazer == "2":
        nivel = int(input("Digite o nível de risco (1 a 3): "))
        print("Bairros com risco", nivel, ":")
        for i in range(len(zona_sul)):
            if zona_sul_risco[i] == nivel:
                print("-", zona_sul[i])
        for i in range(len(zona_norte)):
            if zona_norte_risco[i] == nivel:
                print("-", zona_norte[i])
        for i in range(len(zona_leste)):
            if zona_leste_risco[i] == nivel:
                print("-", zona_leste[i])
        for i in range(len(zona_oeste)):
            if zona_oeste_risco[i] == nivel:
                print("-", zona_oeste[i])
        for i in range(len(zona_central)):
            if zona_central_risco[i] == nivel:
                print("-", zona_central[i])

# 4 - CONSULTAR RISCO DE BAIRRO ESPECIFICO

    elif fazer == "3":
        bairro = input("Digite o nome do bairro que deseja consultar: ")
        achou = False
        for i in range(len(zona_sul)):
            if zona_sul[i] == bairro:
                print(bairro, "tem risco", zona_sul_risco[i])
                achou = True
        for i in range(len(zona_norte)):
            if zona_norte[i] == bairro:
                print(bairro, "tem risco", zona_norte_risco[i])
                achou = True
        for i in range(len(zona_leste)):
            if zona_leste[i] == bairro:
                print(bairro, "tem risco", zona_leste_risco[i])
                achou = True
        for i in range(len(zona_oeste)):
            if zona_oeste[i] == bairro:
                print(bairro, "tem risco", zona_oeste_risco[i])
                achou = True
        for i in range(len(zona_central)):
            if zona_central[i] == bairro:
                print(bairro, "tem risco", zona_central_risco[i])
                achou = True
        if not achou:
            print("Bairro não encontrado.")

    continuar = input("\nDeseja fazer outra ação? (s para sim / qualquer outra tecla para sair): ")

print("Obrigado por usar o R.U.A!")
