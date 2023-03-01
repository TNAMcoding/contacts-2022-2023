import json
file = open('main/contacts.json', 'r')
dictionary = json.load(file)
contacts = dictionary['contacts']
file.close()

while(True):
    response = input('(1)add contact (2)print contacts (3)exit: ')
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
       # person_email = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone
        }
        contacts.append(person_contact)

    elif response == '2':
        for contact in contacts:
            print("---CONTACT---")
            print(f"{contact['name']} {contact['surname']}")
            print(f"Phone: {contact['phone']}")
           # print(f"Email: {contact['email']}")        
        
    elif response == '3':
        print('Saving data...')

        # code to save the date in json format
        dictionary = {'contacts' : contacts}
        file = open('main/contacts.json', 'w', encoding='utf-8' )
        json.dump(dictionary, file, indent = 4)
        file.close()

        print('Data saved.')
        print('Bye bye!')
        exit()
    else:
        print('Please respond with 1, 2 or 3')
