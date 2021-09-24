import json
import re


class CountriesIterator:

    URL = 'https://en.wikipedia.org/wiki/'

    def __init__(self, path):
        self.file = open(path, encoding='windows-1251')
        self.data = json.loads(self.file.read())

    def get_country(self, country_id):
        return self.data[country_id]['name']['common']

    def get_link(self, country_id):
        return f'{self.URL}{self.get_country(country_id)}'

    def change_link_format(self, country_id):
        return re.sub(r'\s', '_', self.get_link(country_id))

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor == len(self.data):
            raise StopIteration
        country = self.get_country(self.cursor)
        link = self.change_link_format(self.cursor)
        self.cursor += 1
        return f'{country} - {link}'


if __name__ == '__main__':
    for i in CountriesIterator('countries.json'):
        print(i)
