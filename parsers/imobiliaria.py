from xml.dom.minidom import parse

dom = parse("imobiliaria.xml")

# Elemento raiz do XML (imobiliaria)
imobiliaria = dom.documentElement

# Recebe uma lista dos elementos com tag "imovel"
imoveis = imobiliaria.getElementsByTagName('imovel')

linha = "-"*50

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
    elemento_rua = elemento_proprietario.getElementsByTagName('rua')[0]
    rua = elemento_rua.firstChild.nodeValue
    elemento_bairro = elemento_proprietario.getElementsByTagName('bairro')[0]
    bairro = elemento_bairro.firstChild.nodeValue
    elemento_cidade = elemento_proprietario.getElementsByTagName('cidade')[0]
    cidade = elemento_cidade.firstChild.nodeValue
    elemento_numero = elemento_proprietario.getElementsByTagName('número')[0]
    numero = elemento_numero.firstChild.nodeValue

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