from logic import ajax

def reqHourseData(numberOfRooms: int = 1, page: int = 1):
    return ajax.ajax('https://krisha.kz/prodazha/kvartiry/nur-sultan/', {'das[live.rooms]': numberOfRooms, 'page': page})


if __name__ == '__main__':
    response = reqHourseData()
    print(response.text)
