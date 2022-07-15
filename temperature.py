import requests
from selectorlib import Extractor


class Temperature:
    extractor = Extractor.from_yaml_file('temperature.yaml')

    def __init__(self, country, city):
        self.country = country
        self.city = city
        self.base_url = 'https://www.timeanddate.com/weather/'

    def _get_url(self):
        self.city = self.city.replace(" ", "-")
        url = f'{self.base_url}{self.country}/{self.city}'
        return url

    def _scrape(self):
        url = self._get_url()
        response = requests.get(url)
        content = response.text
        raw_result = self.extractor.extract(content)
        return raw_result

    def get(self):
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())

# if __name__ == "__main__":
#    temperature = Temperature(country="brazil", city="sao paulo")
#    print(temperature.get())
