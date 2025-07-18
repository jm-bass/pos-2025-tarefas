import zeep

from zeep import Client

# define a URL do WSDL
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o número para converter
while True:
    numero = int(input("Digite um número para converter: "))
    if numero >= 0:
        break
    else:
        print("Por favor, digite um número não negativo.")

# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum=numero
)

# imprime o resultado
print(f"O número {numero} convertido é: {result}")