
client_date = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8_000,
    'city': 'New York'
}

client_date_new = {
    'name': client_date.pop('name'),
    'salary': client_date.pop('salary')
}

print(client_date)
print(client_date_new)
