import requests

# Função que consulta a API do OpenWeatherMap
def get_weather(city, api_key):
    # URL base da API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Realizando a requisição GET para a API
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None

# Função principal que utiliza a função de consulta e exibe o resultado
def main():
    # Substitua sua chave de API aqui
    api_key = "sua_chave_api_aqui"
    city = input("Digite o nome da cidade: ")
    
    # Chama a função de consulta e obtém a temperatura
    temperature = get_weather(city, api_key)
    
    # Exibe a temperatura ou uma mensagem de erro
    if temperature:
        print(f"A temperatura em {city} é {temperature}°C.")
    else:
        print(f"Não foi possível obter a temperatura para {city}. Verifique o nome da cidade ou sua chave de API.")

# Chama a função principal
if __name__ == "__main__":
    main()
