import time
import pandas as pd
import matplotlib.pyplot as plt
from os import system as sys; sys('cls')

#inicializando o dataframe
alunos_df = pd.DataFrame(columns=['Aluno', 'Matematica', 'Portugues', 'Historia', 'Quimica'])

def adicionar_aluno():
    nome = input("Nome do aluno: ")
    try:
        Matematica = float(input("Nota de Matemática: "))
        Portugues = float(input("Nota de Português: "))
        Historia = float(input("Nota de História: "))
        Quimica = float(input("Nota de Química: "))
    except ValueError:
        print("Digite um nome válido.")
        return
    
    novo = pd.DataFrame([{
        'Aluno': nome,
        'Matematica': Matematica,
        'Portugues': Portugues,
        'Historia': Historia,
        'Quimica': Quimica
    }])
    global alunos_df
    alunos_df = pd.concat([alunos_df, novo], ignore_index=True)
    print(f'Aluno "{nome}" adicionado.') 

def mostrar_por_materia():
    materia = input("Digite a matéria (Matematica, Portugues, Historia ou Quimica): ").capitalize()
    if materia not in alunos_df.columns:
        print("Matéria não disponível.")
        return
    ranking = alunos_df.sort_values(by=materia, ascending=False)
    print(f"\nRanking - {materia}")
    print(ranking[['Aluno', materia]])

def mostrar_geral():
    #Feito por gabriel, mas deu problema no merge
    df = alunos_df.copy()
    df['Média Geral'] = df[['Matematica', 'Portugues', 'Historia', 'Quimica']].mean(axis=1)
    ranking= df.sort_values(by='Média Geral', ascending=False)
    print("\nRanking - Média Geral")
    print(ranking[['Aluno', 'Média Geral']])

def gerar_grafico_materias():
    df = alunos_df.set_index('Aluno')
    df[['Matematica', 'Portugues', 'Historia', 'Quimica']].plot(kind='bar', figsize=(12, 6))
    plt.title("Média por Matéria - Alunos")
    plt.xlabel("Aluno")
    plt.ylabel("Média")
    plt.ylim(0, 10)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def gerar_grafico_geral():
    df = alunos_df.copy() 
    df['Média Geral'] = df[['Matematica', 'Portugues', 'Historia', 'Quimica']].mean(axis=1) 
    df = df.set_index('Aluno') 
    df['Média Geral'].sort_values(ascending=False).plot(kind='bar', color='lightgreen', figsize=(10, 5)) 
    plt.title('Ranking - Média Geral dos Alunos')
    plt.xlabel('Aluno')
    plt.ylabel('Média Geral')
    plt.ylim(0, 10)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def salvar_dados():
    alunos_df.to_csv("dados_alunos.csv", index=False)
    print("Dados salvos em 'dados_alunos.csv'.")

    

while True:
    print("\nSistema de Ranking de Médias")
    print("1-Adicionar novo aluno")
    print("2-Ver ranking por materia")
    print("3-Ver ranking geral")
    print("4-Gerar gráfico por matéria")
    print("5-Gerar gráfico de média geral")
    print("6-Salvar dados")
    print("7-Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_aluno()
        time.sleep(3)
        sys('cls')
    elif opcao == '2':
        mostrar_por_materia()
        time.sleep(3)
        print("")
    elif opcao == '3':
        mostrar_geral()
        time.sleep(3)
        print("")

    elif opcao == '4':
        gerar_grafico_materias()
        time.sleep(3)
        print("")
    elif opcao == '5':
        gerar_grafico_geral()
        time.sleep(3)
        print("")
    elif opcao == '6':
        salvar_dados()
        time.sleep(3)
        print("")
    elif opcao == '7':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")