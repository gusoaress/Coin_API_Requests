import requests 


req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
req_coin_price = req.json()

print("Bem vindo ao ambiente de visualiação de cotação de moedas")
coin = input("Voce quer saber a cotação de qual moeda?\n(Digite entre as opções dolar, bitcoin ou euro:\n").lower()

euro_price = req_coin_price['EURBRL']['bid']
dolar_price = req_coin_price['USDBRL']['bid']
bit_price = req_coin_price['BTCBRL']['bid']


if coin == "euro":
    print(f'Euro igual a {euro_price} Real brasileiro')
elif coin == "dolar":
    print(f'Dolar igual a {dolar_price} Real brasileiro')
elif coin == "bitcoin":
    print(f'Bitcoin igual a {bit_price} Real brasileiro')
else: 
    print("Por favor, digite entre as opções indicadas:\n(Dolar, Bitcoin ou Euro")
    

    