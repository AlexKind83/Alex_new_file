import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    latter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(latter)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel,
    }
    return person


def get_key():
    keys = ''
    data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(keys) != 10:
        keys += choice(data)

    return keys


def write_json(person_dict):
    try:
        data = json.load(open('homework.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('homework.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(2):
    write_json({get_key(): gen_person()})
