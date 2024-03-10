person = {'name':'egoing', 'address':'seoul', 'interest':'web'}
print(person['name'])

for key in person:
    print(key, person[key])

    persons = [
        {'name':'egoing', 'address':'seoul', 'interest':'web'},
        {'name':'basta', 'address':'seoul', 'interest':'iot'},
        {'name':'blackdew', 'address':'seoul', 'interest':'ml'},
    ]

print(' ==== persons ==== ')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-------------')
