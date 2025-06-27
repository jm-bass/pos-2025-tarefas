import json
from xml.dom.minidom import parse

dom = parse("parsers/imobiliaria.xml")

# Elemento raiz do XML (imobiliaria)
imobiliaria = dom.documentElement

# Recebe uma lista dos elementos com tag "imovel"
imoveis = imobiliaria.getElementsByTagName('imovel')

linha = "-"*50

dados_json = []

for imovel in imoveis:
    elemento_descricao = imovel.getElementsByTagName('descricao')[0]
    descricao = elemento_descricao.firstChild.nodeValue

    elemento_proprietario = imovel.getElementsByTagName('proprietario')[0]
    elemento_nome = elemento_proprietario.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    elemento_email = elemento_proprietario.getElementsByTagName('email')
    quantEmail = 0
    elemento_telefone = elemento_proprietario.getElementsByTagName('telefone')
    quantTelefone = 0

    elemento_endereco = imovel.getElementsByTagName('endereco')[0]
    elemento_rua = elemento_endereco.getElementsByTagName('rua')[0]
    rua = elemento_rua.firstChild.nodeValue
    elemento_bairro = elemento_endereco.getElementsByTagName('bairro')[0]
    bairro = elemento_bairro.firstChild.nodeValue
    elemento_cidade = elemento_endereco.getElementsByTagName('cidade')[0]
    cidade = elemento_cidade.firstChild.nodeValue
    if elemento_endereco.getElementsByTagName('numero'):
        elemento_numero = elemento_endereco.getElementsByTagName('numero')
    else:
        elemento_numero = elemento_endereco.getElementsByTagName('número')
    if elemento_numero:
        elemento_numero = elemento_numero[0]
    else:
        elemento_numero = None
    if elemento_numero and elemento_numero.firstChild:
        numero = elemento_numero.firstChild.nodeValue
    else:
        numero = None
     
    elemento_caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]
    elemento_tamanho = elemento_caracteristicas.getElementsByTagName('tamanho')[0]
    tamanho = elemento_tamanho.firstChild.nodeValue
    elemento_numQuartos = elemento_caracteristicas.getElementsByTagName('numQuartos')[0]
    numQuartos = elemento_numQuartos.firstChild.nodeValue
    elemento_numBanheiros = elemento_caracteristicas.getElementsByTagName('numBanheiros')[0]
    numBanheiros = elemento_numBanheiros.firstChild.nodeValue

    elemento_valor = imovel.getElementsByTagName('valor')[0]
    valor = elemento_valor.firstChild.nodeValue


    print("Nome:", nome)

    print(f'Descrição: {descricao}')
    print(f"Nome do proprietário: {nome}")
    if elemento_email:
        for email in elemento_email:
            quantEmail += 1
            print(f"Email {quantEmail}: {email.firstChild.nodeValue}")
    if elemento_telefone:
        for telefone in elemento_telefone:
            quantTelefone += 1
            print(f"Telefone {quantTelefone}: {telefone.firstChild.nodeValue}")
    print("Endereço:")
    print(f" Rua: {rua}")
    print(f" Bairro: {bairro}")
    print(f" Cidade: {cidade}")
    if numero:
        print(f" Número: {numero}")

    print("Características:")
    print(f" Tamanho: {tamanho}")
    print(f" Número de quartos: {numQuartos}")
    print(f" Número de banheiros: {numBanheiros}")

    print("Valor:", valor)
    print(linha)

    imovel_dict = {
        "descricao": descricao,
        "proprietario": {
            "nome": nome,
            "emails": [email.firstChild.nodeValue for email in elemento_email],
            "telefones": [tel.firstChild.nodeValue for tel in elemento_telefone]
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    }


    dados_json.append(imovel_dict)

with open("parsers/imobiliaria.json", "w", encoding="utf-8") as f:
    json.dump(dados_json, f, ensure_ascii=False, indent=4)
    print("Dados salvos em imobiliaria.json")