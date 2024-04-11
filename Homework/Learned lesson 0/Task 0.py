import json


def testes(file):
    a1 = {'Andrei': [1, 2]}
    a2 = [{'name': i, 'mark': i} for i in a1]

    s1 = {'name': 'Irina'}
    s2 = {'mark': [1, 2]}
    s3 = {s1, s2}

    b1 = 'Group 1'

    c1 = {b1: a2}


    # with open(file, 'w', encoding='UTF-8') as f:
    #     f.write('[ \n ]')

    try:
        data = json.load(open(file))
    except FileNotFoundError:
        data = []  # Или []

    data.append(c1)
    print(type(data))

    with open(file, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=2)


testes('file_name.json')

