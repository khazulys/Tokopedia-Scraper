import requests
from bs4 import BeautifulSoup as bs

class tokped:

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}
    
    def __init__(self, tipe, toko):
        self.tipe = tipe
        self.toko = toko
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}
        self.url = f'https://www.tokopedia.com/{self.toko}/etalase/all?q={self.tipe}/'.replace(" ", "%20")

    def main_function(self):
        _request = requests.get(self.url, headers=self.headers).text
        soup = bs(_request, "lxml")
        product_name = soup.find('div', class_="css-1b6t4dn").text
        price = soup.find('div', class_='css-1ksb19c').text
        rating = soup.find('span', class_='css-t70v7i').text
        stock = soup.find('div', class_='css-1458qc4').text
        print(f'''

        Product : {product_name}
        Price   : {price}
        rating  : {rating}
        stock   : {stock}''')

tokped("galaxy a72", "samsung").main_function()