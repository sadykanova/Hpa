from bs4 import BeautifulSoup
from logic import api


def hourse_data():
    # response = api.reqHourseData()

    # html = response.text
    # soup = BeautifulSoup(html, "html.parser")

    # response_data = []

    # area_list = soup.find_all('a', attrs={'class': 'a-card__title'})
    # price_list = soup.find_all('div', attrs={'class': 'a-card__price'})

    # for i in range(min(len(area_list), len(price_list))):
    #     data = {
    #         'area': area_list[i].text.split(',')[1],
    #         'link': 'https://krisha.kz' + area_list[i]['href'],
    #         'price': (''.join([j for j in price_list[i].text.strip() if j in '0123456789']) + ' 〒'),
    #     }
    #     response_data.append(data)
    
    response_data = [{'area': ' 40 м²', 'link': 'https://krisha.kz/a/show/666236186', 'price': '10700000 〒'}, {'area': ' 44.32 м²', 'link': 'https://krisha.kz/a/show/665799563', 'price': '11966400 〒'}, {'area': ' 39.57 м²', 'link': 'https://krisha.kz/a/show/666401871', 'price': '10683900 〒'}, {'area': ' 38 м²', 'link': 'https://krisha.kz/a/show/666883433', 'price': '11600000 〒'}, {'area': ' 31.8 м²', 'link': 'https://krisha.kz/a/show/666902887', 'price': '14500000 〒'}, {'area': ' 26 м²', 'link': 'https://krisha.kz/a/show/57036874', 'price': '4680500 〒'}, {'area': ' 44.42 м²', 'link': 'https://krisha.kz/a/show/662950124', 'price': '12304340 〒'}, {'area': ' 52 м²', 'link': 'https://krisha.kz/a/show/665365952', 'price': '14040000 〒'}, {'area': ' 40.94 м²', 'link': 'https://krisha.kz/a/show/662309117', 'price': '10288222 〒'}, {'area': ' 42.01 м²', 'link': 'https://krisha.kz/a/show/662766637', 'price': '14703500 〒'}, {'area': ' 36 м²', 'link': 'https://krisha.kz/a/show/666777837', 'price': '11500000 〒'}, {'area': ' 39.2 м²', 'link': 'https://krisha.kz/a/show/664819417', 'price': '15990000 〒'}, {'area': ' 42.5 м²', 'link': 'https://krisha.kz/a/show/666881356', 'price': '13920000 〒'}, {'area': ' 29.1 м²', 'link': 'https://krisha.kz/a/show/666734661', 'price': '13000000 〒'}, {'area': ' 40 м²', 'link': 'https://krisha.kz/a/show/665004130', 'price': '22800000 〒'}, {'area': ' 33 м²', 'link': 'https://krisha.kz/a/show/662989414', 'price': '8200000 〒'}, {'area': ' 39 м²', 'link': 'https://krisha.kz/a/show/666902572', 'price': '12500000 〒'}, {'area': ' 33.24 м²', 'link': 'https://krisha.kz/a/show/665673889', 'price': '12000000 〒'}, {'area': ' 46.54 м²', 'link': 'https://krisha.kz/a/show/663597788', 'price': '22106500 〒'}, {'area': ' 34.7 м²', 'link': 'https://krisha.kz/a/show/666909834', 'price': '11400000 〒'}, {'area': ' 31.4 м²', 'link': 'https://krisha.kz/a/show/665726922', 'price': '14500000 〒'}]


    return response_data
