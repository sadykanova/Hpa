import requests


def ajax(url: str, data: dict = {}, method: str = 'GET'):
    if method == 'GET':
        param_str = ''
        for data_key in data.keys():
            param_str += data_key + '=' + str(data[data_key]) + '&'

        if param_str:
            param_str = param_str[0:-1]

        response = requests.get(url=url + '?' + param_str)

        return response

    if method == 'POST':
        response = requests.post(url=url, data=data)

        return response


if __name__ == '__main__':
    response = ajax('https://jsonplaceholder.typicode.com/comments', {'postId': 1})
    print(response.text)
