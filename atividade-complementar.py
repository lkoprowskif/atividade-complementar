#Análise das notas dos alunos


alunos = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carlos": 9.0,
    "Daniela": 7.5,
    "Eduardo": 5.5
}
#Etapa 01
def listar_alunos(alunos):
    print("Alunos cadastrados:")
    for aluno in alunos.keys():
        print(aluno)

#Etapa 02
def calcular_media(alunos):
    soma = 0
    for nota in alunos.values():
        soma += nota

    quantidade = len(alunos.keys())
    media = soma / quantidade
    #print(f"Media da turma: {media:.1f}:")------------------------------

    return media

#Etapa 03
def exibir_notas(alunos):
    for nome, nota in alunos.items():
        print(f"{nome}: {nota}")

#Etapa 04
def consultar_nota(alunos, nome):
    return alunos.get(nome, None)

#Etapa 05
def listar_aprovados(alunos, media_minima):
    aprovados = []
    for nome, nota in alunos.items():
        if nota >= media_minima:
            aprovados.append(nome)
    return aprovados

#Etapa 06
def ler_nota():
    while True:
        try:
            nota = input("Informe uma nota do aluno: ")
            nota = float(nota)
            return nota
        except ValueError:
            print("Entrada inválida! Digite uma nota válida.")

#Etapa 07
def adicionar_aluno(alunos, nome, nota):
    if nome in alunos.keys():
        return False
    alunos[nome] = nota
    return True

#Etapa 08
nome = input("Informe o nome do aluno: ")
nota = consultar_nota(alunos, nome)

if nota is None:
    print("Aluno não encontrado.")
else:
    print(f"Nota de {nome}: {nota}")

media_minima = ler_nota()

aprovados = listar_aprovados(alunos, media_minima)

print("Alunos aprovados:")
for aluno in aprovados:
    print(aluno)





