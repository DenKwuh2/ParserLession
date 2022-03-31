import requests
from bs4 import BeautifulSoup
import json

#persons_list = [] - список для ссылок

#for i in range(0, 740, 20):
#    url = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/biografien/862712-862712?limit=20&noFilterSet=true&offset={i}' - url.запрос

#    q = requests.get(url)
#    result = q.content

#    soup = BeautifulSoup(result, 'lxml')

#    persons = soup.find_all(class_='bt-open-in-overlay')

#    for person in persons:
#        person_url = person.get('href')
#        persons_list.append(person_url)

#with open('person_url.txt', 'a', encoding='UTF-8') as file:
#    for line in persons_list:
#        file.write(f'{line}\n')

with open('Parser 1.person_url.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0
    for line in lines:
        q = requests.get('https://www.bundestag.de'+line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')

        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_list = []

        for i in social_networks:
            social_networks_list.append(i.get('href'))

        data = {
            'person_name': person_name,
            'person_company': person_company,
            'social_networks': social_networks_list
        }
        data_dict.append(data)

        count += 1
        print(f'#{count}: {line} is done!')

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, indent=4)






