import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
headers = {'Content-Type': 'text/xml; charset=utf-8'}

controle = True
while controle == True:
    linha = "-" * 50
    print("Funções disponíveis:")
    print("1 - Nome do país a partir do código ISO")
    print("2 - Código ISO a partir do nome do país")
    print("3 - Capital a partir do código ISO")
    print("4 - Sair")

    resposta = input("Escolha uma opção (1/2/3/4): ").strip()
    if resposta not in ['1', '2', '3', '4']:
        print("Opção inválida. Encerrando o programa.")
        exit()

    if resposta == "1":
        iso = input("Digite o código ISO do país (ex: BRA): ").strip().upper()
        payload = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{iso}</sCountryISOCode>
                </CountryName>
            </soap:Body>
        </soap:Envelope>"""
        response = requests.post(url, headers=headers, data=payload)
        dom = parseString(response.text)
        country_name = None
        for elemento in dom.getElementsByTagName('*'):
            if elemento.tagName.endswith('CountryNameResult'):
                country_name = elemento.firstChild.nodeValue
                break
        if country_name:
            print(f"Nome do país: {country_name}")
            print(f"{linha}\n")
        else:
            print("País não encontrado.")
            print(f"{linha}\n")

    if resposta == "2":
        nome = input("Digite o nome do país (ex: Brazil): ").strip()
        payload = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CountryISOCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryName>{nome}</sCountryName>
                </CountryISOCode>
            </soap:Body>
        </soap:Envelope>"""
        response = requests.post(url, headers=headers, data=payload)
        dom = parseString(response.text)
        iso_code = None
        for elemento in dom.getElementsByTagName('*'):
            if elemento.tagName.endswith('CountryISOCodeResult'):
                iso_code = elemento.firstChild.nodeValue
                break
        if iso_code:
            print(f"Código ISO: {iso_code}")
            print(f"{linha}\n")
        else:
            print("Código ISO não encontrado.")
            print(f"{linha}\n")

    if resposta == "3":
        iso = input("Digite o código ISO do país (ex: BRA): ").strip().upper()
        payload = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{iso}</sCountryISOCode>
                </CapitalCity>
            </soap:Body>
        </soap:Envelope>"""
        response = requests.post(url, headers=headers, data=payload)
        dom = parseString(response.text)
        capital = None
        for elemento in dom.getElementsByTagName('*'):
            if elemento.tagName.endswith('CapitalCityResult'):
                capital = elemento.firstChild.nodeValue
                break
        if capital:
            print(f"Capital: {capital}")
            print(f"{linha}\n")
        else:
            print("Capital não encontrada.")
            print(f"{linha}\n")
        
    if resposta == "4":
        controle = False
        print("Encerrando o programa.")