import requests

linha = "=" * 50
api_url = "https://jsonplaceholder.typicode.com/users"

def list():
    response = requests.get(api_url)
    if response.status_code == 200:
        users = response.json()
        print(linha)
        print("Lista de Usuários:")
        for user in users:
            print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")
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
        print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")
        print(linha)
    else:
        print("Usuário não encontrado.")

def update():
    user_id = input("Digite o ID do usuário que deseja atualizar: ")
    response = requests.get(f"{api_url}/{user_id}")
    user = response.json()
    print("Usuário selecionado: ")
    print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")

    nome = input("Deseja alterar o nome y|n? ")
    if nome.lower() == 'y':
        user['name'] = input("Novo nome: ")
    
    username = input("Deseja alterar o nome de usuário y|n? ")
    if username.lower() == 'y':
        user['username'] = input("Novo nome de usuário: ")
    
    email = input("Deseja alterar o email y|n? ")
    if email.lower() == 'y':
        user['email'] = input("Novo email: ")
    
    street = input("Deseja alterar a rua y|n? ")
    if street.lower() == 'y':
        user['address']['street'] = input("Nova rua: ")
    
    city = input("Deseja alterar a cidade y|n? ")
    if city.lower() == 'y':
        user['address']['city'] = input("Nova cidade: ")
    
    zipcode = input("Deseja alterar o código postal y|n? ")
    if zipcode.lower() == 'y':
        user['address']['zipcode'] = input("Novo código postal: ")

    lat = input("Deseja alterar a latitude y|n? ")
    if lat.lower() == 'y':
        user['address']['geo']['lat'] = input("Nova latitude: ")

    lng = input("Deseja alterar a longitude y|n? ")
    if lng.lower() == 'y':
        user['address']['geo']['lng'] = input("Nova longitude: ")

    response = requests.put(f"{api_url}/{user_id}", json=user)
    if response.status_code == 200:
        print("Usuário atualizado com sucesso!")
        print(f"ID: {response.json()['id']}, Name: {response.json()['name']}, Email: {response.json()['email']}")
    else:
        print("Falha ao atualizar usuário.")

def delete():
    user_id = input("Digite o ID do usuário que deseja excluir: ")
    response = requests.delete(f"{api_url}/{user_id}")
    if response.status_code == 200:
        print("Usuário excluído com sucesso!")
    else:
        print("Falha ao excluir usuário.")


