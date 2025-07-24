import requests
from getpass import getpass
from tabulate import tabulate

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=data)
token = response.json()['access']

headers = {
    "Authorization": f'Bearer {token}'
}


ano = int(input("Digite o ano: "))
semestre = int(input("Digite o semestre (1 ou 2): "))


if ((ano == int) and (ano < 2026)) and semestre == (1 or 2):
    response = requests.get(api_url + "/ensino/meu-boletim/{ano}/{semestre}/".format(ano=ano, semestre=semestre), headers=headers)
    disciplinas = response.json()

    tabela_dados = []
    for disciplina in disciplinas['results']:
        linha = [
            disciplina['disciplina'],
            disciplina['nota_etapa_1']['nota'],
            disciplina['nota_etapa_2']['nota'],
            disciplina['nota_etapa_3']['nota'],
            disciplina['nota_etapa_4']['nota']
        ]

        if disciplina['nota_etapa_1']['nota'] is None:
            disciplina['nota_etapa_1']['nota'] = "0"
        else: disciplina['nota_etapa_1']['nota'],

        if disciplina['nota_etapa_2']['nota'] is None:
            disciplina['nota_etapa_2']['nota'] = "0"
        else: disciplina['nota_etapa_2']['nota'],

        if disciplina['nota_etapa_3']['nota'] is None:
            disciplina['nota_etapa_3']['nota'] = "0"
        else: disciplina['nota_etapa_3']['nota'],

        if disciplina['nota_etapa_4']['nota'] is None:
            disciplina['nota_etapa_4']['nota'] = "0"
        else: disciplina['nota_etapa_4']['nota'],
        #add a linha na tebela
        tabela_dados.append(linha)

    # Define cabeçalhos
    cabecalhos = ["Disciplina", "Etapa 1", "Etapa 2", "Etapa 3", "Etapa 4"]


    # Exibir a tabela formatada
    print("\nBOLETIM - NOTAS POR ETAPA")
    print(tabulate(tabela_dados, headers=cabecalhos, tablefmt="grid"))
else:
    print("Ano ou semestre inválido. Por favor, tente novamente.")