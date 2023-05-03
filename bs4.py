from urllib.request import urlopen
from bs4 import BeautifulSoup

#url = "https://webscraper.io/test-sites/tables"
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,'lxml')

#region Test for https://webscraper.io/test-sites/tables 
'''Get H2 Tags from HTML Code '''
# h2 = soup.find_all("h2")
# print(h2)

'''Get IMG Tags from HTML Code'''
# imgs = soup.find_all("img")
# print(imgs)
# print(imgs[1]['src'])

'''Get Table Detail Data'''
# table = soup.find_all("td")
# print(table)

''' Get Table Detail Data - Alternative Method'''
# table = soup.find('table')
# rows = table.find_all('tr')[1:]
# firstname = []
# surname = []
# username = []
# for row in rows:
#     firstname.append(row.findAll('td')[1].get_text())
#     surname.append(row.findAll('td')[2].get_text())
#     username.append(row.findAll('td')[3].get_text())
# print(firstname, surname, username)

#endregion

#region Test for https://en.wikipedia.org/wiki/Python_(programming_language)
''' Get Table Data from Wikipedia Page'''
table = soup.find(class_="wikitable")
body = table.find("tbody")
rows = body.find_all("tr")[1:]
mutables = []
immutables = []

for row in rows:
    data = row.find_all("td")
    if data[1].get_text() == "mutable\n":
        mutables.append(data[0].get_text())
    if data[1].get_text() == "immutable\n":
        immutables.append(data[0].get_text())

print(f'Mutable Types = {mutables}')
print(f'Imutable Types = {immutables}')
#endregion