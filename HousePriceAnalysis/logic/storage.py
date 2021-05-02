# C
def create_data(data: dict):
    data_in_db = []
    try:
        with open('db.txt', 'r', encoding='utf-8') as f:
            if data not in [eval(i) for i in f.read().split('\n')[:-1]]:
                with open('db.txt', 'a', encoding='utf-8') as f:
                    f.write(str(data)+'\n')
    except Exception as e:
        with open('db.txt', 'a', encoding='utf-8') as f:
            f.write(str(data)+'\n')


# R
def read_data():
    try:
        with open('db.txt', 'r', encoding='utf-8') as f:
            return [eval(i) for i in f.read().split('\n')[:-1]]
    except Exception as e:
        return []

# U
def update_data(data: dict):
    pass


# D
def delete_data(data: dict):
    with open('db.txt', 'r', encoding='utf-8') as f:
        data = list(filter(lambda el: el != data, [eval(i) for i in f.read().split('\n')[:-1]]))
    with open('db.txt', 'w', encoding='utf-8') as f:
        f.write(''.join([str(i)+'\n' for i in data]))
