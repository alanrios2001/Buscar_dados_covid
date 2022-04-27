#Coded By: Alan Melo
import requests
import json
import os



def get_paises():
    url = "https://covid-193.p.rapidapi.com/countries"
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "4277b98439msh68c37d821f2cd02p126742jsn049fbeb87156"
        }
    response = requests.request("GET", url, headers=headers, params='')
    dict_paises = json.loads(response.text)
    paises = dict_paises['response']

    return paises

def select_pais(paises):
    lista_paises = []
    print('*'*5,'PAISES-DISPONIVEIS','*'*5)
    for pais in paises:
        print('-',pais)
        lista_paises.append(pais)
    while True:
        escolha = input('escreva o nome do pais que deseja vizualizar o dado: ')
        if escolha not in lista_paises:
            print('pais indisponivel para busca')
        else:
            break
    return escolha

def get_dados(pais):
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "4277b98439msh68c37d821f2cd02p126742jsn049fbeb87156"
    }
    response = requests.request("GET", url, headers=headers)
    dict_response = json.loads(response.text)
    dados = dict_response['response']

    for item in dados:
        if item['country'] == pais:
            dados_obtidos = item
            break
    return dados_obtidos

def show_dados(obtidos):
    print('*'*10,obtidos['country'].upper(),'*'*10)
    print(f'população: ', obtidos['population'])
    print('-'*5,'CASOS','-'*5)
    print(f'total de casos: ', obtidos['cases']['total'])
    print(f'novos casos: ', obtidos['cases']['new'])
    print(f'casos ativos: ', obtidos['cases']['active'])
    print(f'casos ativos criticos: ', obtidos['cases']['critical'])
    print(f'casos curados: ', obtidos['cases']['recovered'])
    print('-'*5,'MORTALIDADE','-'*5)
    print(f'ultimas mortes(24h): ', obtidos['deaths']['new'])
    print(f'total de mortes: ', obtidos['deaths']['total'])
    print('-'*5,'TESTES','-'*5)
    print(f'total de testes feitos: ', obtidos['tests']['total'])
    print('')
    print('-'*5,'DATA DOS DADOS','-'*5)
    print(f'data: ', obtidos['day'].replace('-','/'))
    lista_horario = list(obtidos['time'])
    
    i = 0
    while True:
        if lista_horario[i] != 'T':
            lista_horario.remove(lista_horario[i])
        elif lista_horario[i] == 'T':
            lista_horario.remove(lista_horario[i])
            break
    
    hora = ''.join([lista_horario[0],lista_horario[1]])
    min = ''.join([lista_horario[3],lista_horario[4]])
    seg = ''.join([lista_horario[6],lista_horario[7]])
    fuso = ''.join([lista_horario[8],lista_horario[9],lista_horario[10]])
    print(f'horario: {hora}:{min}:{seg}')
    print(f'fuso: {fuso}:00')

def main():
    #try:
        i = 1
        while i > 0:
            j = 1
            paises = get_paises()
            escolha = select_pais(paises)
            dados = get_dados(escolha)
            os.system('cls')
            show_dados(dados)
            while j > 0:
                opc = input('deseja realizar outra consulta?(s/n): ')
                if opc == 's':
                    j = 0
                    input('pressione enter: ')
                    if os.name == 'posix':
                        os.system('clear')
                    else:
                        os.system('cls')
                elif opc == 'n':
                    j = 0
                    i = 0
                elif opc != 's' or opc != 'n':
                    print('opcao invalida')
    #except:
        #print('opcao invalida')
    

main()