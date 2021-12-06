def lerArquivo(nome):
    arq = open(nome, "r")
    linhas = arq.readlines()
    result = []
    for l in linhas:
        result.append(l.replace('\n', ''))
    arq.close()
    return result

def obtemParticipantes(dados):
    participantes = []
    for d in dados:
        if "," in d:
            individual = d.split(",")
            participantes.append(individual)
    return participantes

entrada = lerArquivo("dados.txt")
pessoas = obtemParticipantes(entrada)
#--------------------------------------------------------------#
#-------------------- ZERO --------------------#

#Lista dos Generos
G = []
for i in pessoas:
    G.append(i[0])
    
M = G.count('M')
pM = M * 100/ len(pessoas)

F = G.count('F')
pF = F * 100/ len(pessoas)

#--------------------------------------------------------------#
#-------------------- UM --------------------#

#Lista de Idades
idade = []
for i in pessoas:
    idade.append(i[1])

idade_letras = []
for i in idade:
    i = int(i)
    if (i <= 19): 
        idade_letras.append('J')
        
    elif (i > 19 and i <=59):
        idade_letras.append('A')
        
    elif (i >= 60):
        idade_letras.append('I')

# JOVENS
J = idade_letras.count('J')
pJ = J * 100/ len(pessoas)

# ADULTOS
A = idade_letras.count('A')
pA = A * 100/ len(pessoas)

# IDOSOS
I = idade_letras.count('I')
pI = I * 100/ len(pessoas)

#Lista dos Vacinados ou Placebo
vacinas = []
for i in pessoas:
    vacinas.append(i[2])
    

V = vacinas.count('V')
pV = V * 100/ len(pessoas)

P = vacinas.count('P')
pP = P * 100/ len(pessoas)

#Lista de quem contraiu ou Não

contrasao = []
for i in pessoas:
    contrasao.append(i[3])
    
S = contrasao.count('S')
pS = S * 100/ len(pessoas)

N = contrasao.count('N')
pN = N * 100/ len(pessoas)

#--------------------------------------------------------------#
#-------------------- DOIS --------------------#

#Eficacia geral da vacina
#100* (a-b)/a

arq = open('dados.txt', "r")
linhas = arq.readlines()
qtd = int(linhas[0])
a = b = 0
for i in range(1, qtd + 1, 1):
    coluna = linhas[i].split(',')
    # a = placebo e contraiu covid
    if coluna[2] == 'P' and coluna[3] == 'S\n':
        a = a + 1
    # b = vacina e contraiu covid    
    elif coluna[2] == 'V' and coluna[3] == 'S\n':
        b = b + 1
eficacia = 100 * (a - b) / a

#--------------------------------------------------------------#
#-------------------- TRÊS --------------------#

arq = open('dados.txt', 'r')
linhas = arq.readlines()
qtd = int(linhas[0])


aj = bj = aa = ba = ai = bi = 0
for i in range(1, qtd + 1, 1):
    p = linhas[i].split(',')
    if int(p[1]) <= 19 and p[2] == 'P' and p[3] == 'S\n':
        aj = aj + 1

    if int(p[1]) <= 19 and p[2] == 'V' and p[3] == 'S\n':
        bj = bj + 1

    if int(p[1]) > 19 and int(p[1]) <= 59 and p[2] == 'P' and p[3] == 'S\n':
        aa = aa + 1

    if int(p[1]) > 19 and int(p[1]) <= 59 and p[2] == 'V' and p[3] == 'S\n':
        ba = ba + 1

    if int(p[1]) > 59 and p[2] == 'P' and p[3] == 'S\n':
        ai = ai + 1

    if int(p[1]) > 59 and p[2] == 'V' and p[3] == 'S\n':
        bi = bi + 1


eJ = 100 * (aj - bj) / aj
eA = 100 * (aa - ba) / aa
eI = 100 * (ai - bi) / ai

#--------------------------------------------------------------#
#-------------------- QUATRO --------------------#

arq = open('dados.txt', "r")
linhas = arq.readlines()
qtd = int(linhas[0])
amasc = bmasc = 0
afemi = bfemi = 0
for i in range(1, qtd + 1, 1):
    colunas = linhas[i].split(',')
    #MASCULINO
    if colunas[0] == 'M' and colunas[2] == 'P' and colunas[3] == 'S\n':
        amasc = amasc+ 1
    if colunas[0] == 'M' and colunas[2] == 'V' and colunas[3] == 'S\n':
        bmasc = bmasc + 1
    #FEMININO
    if colunas[0] == 'F' and colunas[2] == 'P' and colunas[3] == 'S\n': 
        afemi = afemi + 1 
    if colunas[0] == 'F' and colunas[2] == 'V' and colunas[3] == 'S\n':
        bfemi = bfemi + 1

eficaciaMasculino = 100*(amasc - bmasc)/amasc
eficaciaFeminino = 100*(afemi - bfemi)/afemi

#--------------------------------------------------------------#
#-------------------- VAMOS LÁ --------------------#

opção = 0
while opção !=5:
    print("="*80)
    print("DIGITE DE 0 a 5 PARA EXIBIR AS OPÇÕES:\n")
    print("[ 0 ] - Mostrar % do Genero M/F")
    print("[ 1 ] - Percentuais Geral dos Participantes em Porcentagem")
    print("[ 2 ] - Eficácia Geral da Vacina.")
    print("[ 3 ] - Eficácia entre os jovens, adultos e idosos ")
    print("[ 4 ] - Eficácia onde restringe a população ao gêneros masculino e feminino.")
    print("[ 5 ] - Sair\n")

    opção = int(input("DIGITE DE 0 a 5 PARA EXIBIR AS OPÇÕES:"))
    if opção ==0:
        print(f"{pM:.0f}% Masculino - {pF:.0f}% Feminino")
    elif opção ==1:
        print(f"{pM:.0f}% Masculino - {pF:.0f}% Feminino")
        print(f"{pJ:.0f}% JOVENS - {pA:.0f}% ADULTOS - {pI:.0f}% IDOSOS")
        print(f"{pV:.0f}% Vacina - {pP:.0f}% Placebo")
        print(f"{pS:.0f}% Contraiu Covid - {pN:.0f}% Não Contraiu")
    elif opção ==2:
        print(f"{eficacia:.1f}% Eficácia Geral da Vacina")
    elif opção ==3:
        print(f"{eJ:.1f}% Eficácia nos Jovens")
        print(f"{eA:.1f}% Eficácia nos Adultos")
        print(f"{eI:.1f}% Eficácia nos Idosos")
    elif opção ==4:
        print(f"{eficaciaMasculino:.1f}% Eficácia Geral da Vacina em Homens")
        print(f"{eficaciaFeminino:.1f}% Eficácia Geral da Vacina em Mulheres")
    elif opção ==5:
        print("Você Encerrou")