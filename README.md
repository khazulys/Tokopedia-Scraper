# Tokopedia-Scraper
Extracting data from website [tokopedia.com](https://www.tokopedia.com)
for the show details product.

# Module Required
`pip install requests`

`pip install bs4`

# Import Library
```python require markdown = 
from requests import Session
from bs4 import BeautifulSoup
```

# Class Object
```python require markdown =
class tokopedia:

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}

    def __init__(self, toko, tipe):
        self.toko = toko
        self.tipe = tipe
        self.s = Session()
        self.url = f'https://www.tokopedia/{self.toko}/etalase/all?q={self.tipe}'.replace(" ","%20")
   
    # main function
    def showdata(self):
        _request = self.s.get(self.url, headers=__class__.headers).text
        soup = BeautifulSoup(_request, 'html.parser')
        product_name = soup.find('div', class_ = 'css-1b6t4dn').text
        price = soup.find('div', class_='css-1ksb19c').text
        rating = soup.find('span', class_='css-t70v7i').text
        stock =
```
