import pandas as pd
import matplotlib.pyplot as plt

#inicializando o dataframe
alunos_df = pd.DataFrame(columns=['Aluno', 'Matemática', 'Português', 'História', 'Química'])

def adicionar_aluno():
    nome = input("Nome do aluno: ")
    try:
        matematica = float(input("Nota de Matemática: "))
        portugues = float(input("Nota de Português: "))
        historia = float(input("Nota de História: "))
        quimica = float(input("Nota de Química: "))
    except ValueError:
        print("Digite um nome válido.")
        return
    
    novo = pd.DataFrame([{
        'Aluno': nome,
        'Matemática': matematica,
        'Português': portugues,
        'História': historia,
        'Química': quimica
    }])
    global alunos_df
    alunos_df = pd.concat([alunos_df, novo], ignore_index=True)
    print(f'Aluno "{nome}" adicionado.') 
    while True:
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
        elif opcao == '2':
            
        elif opcao == '3':
            
        elif opcao == '4':
            
        elif opcao == '5':
            
        elif opcao == '6':
            
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")