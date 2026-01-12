import requests
import tqdm

emails = []

for i in tqdm.tqdm(range(1, 30)):
    url = f'http://localhost:3000/rest/products/{i}/reviews'
    response = requests.get(url)
    if response.status_code == 200:
        reviews = response.json()
        for review in reviews['data']:
            email = review.get('author')
            if email and email not in emails:
                emails.append(email)

print("Emails encontrados nos reviews:")
for email in emails:
    print(email)   