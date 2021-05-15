from bs4 import BeautifulSoup
import requests
import pandas as pd
URL = 'https://www.friendshome.pk/search.php?category%5B%5D=938&category%5B%5D=939&category%5B%5D=869&category%5B%5D=1629&category%5B%5D=871&category%5B%5D=942&category%5B%5D=1443&category%5B%5D=881&category%5B%5D=1880&category%5B%5D=1627&cat=29%2C150%2C189&catarr=29%2C150%2C189'

source = requests.get(URL)
soup = BeautifulSoup(source.content, 'lxml')

productTitle = []
productPrice = []
productModel = []

#print (soup.prettify())
for title in soup.find_all('div', class_='prd_title'):
     prdtitle = title.a.text
     productTitle.append(prdtitle)
    # print(prdtitle)

for price in soup.find_all('span', class_='prd_price'):
     prdprice = price.text
     productPrice.append(prdprice)
    # print(prdprice)

for model in soup.find_all('div', class_='prd_mdl'):
     prdmodel = model.text
     prdmodel = prdmodel[6:]
     productModel.append(prdmodel)
     #print(prdmodel)

#print(productModel)
data = {'Title':productTitle,
        'Model':productModel,
        'Price':productPrice}
#print(data['Title'])
df = pd.DataFrame(data)
print(df.size)
print(df.shape)
print(df.head())
df.to_csv('LEDPricesFriends.csv', index = False)
df.to_excel(r'LEDPricesFriends.xlsx',index = False, header = True)
