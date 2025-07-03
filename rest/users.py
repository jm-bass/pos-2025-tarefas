import requests

linha = "=" * 50
api_url = "https://jsonplaceholder.typicode.com/users"

def list_():
    response = requests.get(api_url)
    if response.status_code == 200:
        users = response.json()
        print(linha)
        print("Lista de Usuários:")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        print(linha)
    else:
        print("Falha ao obter a lista de usuários.")

def create():
    print("Preencha os dados do novo usuário:")
    name = input("Nome: ")
    username = input("Nome de usuário: ")
    email = input("Email: ")
    street = input("Rua: ")
    city = input("Cidade: ")
    zipcode = input("Código postal: ")
    lat = input("Latitude: ")
    lng = input("Longitude: ")

    user_novo = {
        "name": name,
        "username": username,
        "email": email,
        "address": {
            "street": street,
            "city": city,
            "zipcode": zipcode,
            "geo": {
                "lat": lat,
                "lng": lng
            }
        }
    }

    response = requests.post(api_url, json=user_novo)
    if response.status_code == 201:
        print("Usuário criado com sucesso!")
        print(f"ID: {response.json()['id']}, Name: {response.json()['name']}, Email: {response.json()['email']}")
    else:
        print("Falha ao criar usuário.")

def read():
    user_id = input("Digite o ID do usuário que deseja ler: ")
    response = requests.get(f"{api_url}/{user_id}")
    if response.status_code == 200:
        user = response.json()
        print(linha)
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        print(linha)
    else:
        print("Usuário não encontrado.")

def update():
    user_id = input("Digite o ID do usuário que deseja atualizar: ")
    

# Menu principal
usuario = input("Digite 'l' para listar usuários ou 'c' para criar um novo usuário: ")
if usuario.lower() == 'l':
    list_()
elif usuario.lower() == 'c':
    create()
else:
    print("Opção inválida. Por favor, escolha 'l' ou 'c'.")
