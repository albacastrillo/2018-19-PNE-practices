import json
import termcolor

f = open("people.json", 'r')

people = json.load(f)

print("Total number of people in the database:", len(people['Person']))

for person in people['Person']:
    print()
    termcolor.cprint("Name: ", 'green', end='')
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(person['Age'])

    for i,num in enumerate(person['phoneNumber']):
        termcolor.cprint("  Phone {}: ".format(i+1), 'blue')

        termcolor.cprint("   Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("   Number: ", 'red', end='')
        print(num['number'])
