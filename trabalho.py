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
    
