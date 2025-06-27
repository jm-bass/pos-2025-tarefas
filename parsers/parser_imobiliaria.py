import json

with open("parsers/imobiliaria.json", "r", encoding="utf-8") as f:
    imoveis = json.load(f)

linha = "-"*50

id_imovel = 0
for imovel in imoveis:
    print(f"{id_imovel+1} - {imovel['descricao']}")
    id_imovel += 1
print(linha)

casa = int(input("Digite o ID da casa que deseja saber mais: "))

print(f"\n{linha}\n")

imovelControle = 1
for imovel in imoveis:
    if casa == imovelControle:
        print(f"Proprietário: {imovel['proprietario']['nome']}\n")

        print("Emails:")
        if imovel['proprietario']['emails']:
            for email in imovel['proprietario']['emails']:
                print(" °", email, "\n")
        else:
            print(" ° Não tem\n")
            False

        print("Telefones:")
        if imovel['proprietario']['telefones']:
            for tel in imovel['proprietario']['telefones']:
                print(" °", tel)
        else:
            print(" ° Não tem")
            False

        print("\nEndereço:")
        print(" Rua:", imovel['endereco']['rua'])
        print(" Bairro:", imovel['endereco']['bairro'])
        print(" Cidade:", imovel['endereco']['cidade'])
        if imovel['endereco']['numero']:
            print(" Número:", imovel['endereco']['numero'])

        print("\nCaracterísticas:")
        print(" Tamanho:", imovel['caracteristicas']['tamanho'])
        print(" Quartos:", imovel['caracteristicas']['numQuartos'])
        print(" Banheiros:", imovel['caracteristicas']['numBanheiros'], "\n")

        print("Valor:", imovel['valor'])
        break 

    imovelControle += 1