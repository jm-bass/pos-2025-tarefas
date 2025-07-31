import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()['access']
print(response.json())

headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

response = requests.get(api_url+"/ensino/meu-boletim/2024/1/", headers=headers)

disciplinas = response.json()

#print(response.json())

for disciplina in disciplinas['results']:
    print(f" Disciplina: {disciplina['disciplina']}, Nota Etapa 1: {disciplina['nota_etapa_1']['nota']}, Nota Etapa 2: {disciplina['nota_etapa_2']['nota']}, Nota Etapa 3: {disciplina['nota_etapa_3']['nota']}, Nota Etapa 4: {disciplina['nota_etapa_4']['nota']}")

print(response)

#{'codigo_diario': '126447', 'disciplina': 'TIN.0597 - Análise e Projeto Orientados a Objetos(60H)',
#'segundo_semestre': False, 'carga_horaria': 80, 'carga_horaria_cumprida': 85, 'numero_faltas': 14,
#'percentual_carga_horaria_frequentada': 84.0, 'situacao': 'Aprovado', 'quantidade_avaliacoes': 4,
#'nota_etapa_1': {'nota': 70, 'faltas': 0}, 'nota_etapa_2': {'nota': 89, 'faltas': 0}, 'nota_etapa_3': {'nota': 83, 'faltas': 14},
#'nota_etapa_4': {'nota': 89, 'faltas': 0}, 'media_disciplina': 83, 'nota_avaliacao_final': {'nota': None, 'faltas': 0}, 'media_final_disciplina': '83'},