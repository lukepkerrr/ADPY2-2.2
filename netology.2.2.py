import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
def check_by_name(lastname, firstname, list_of_items):
    for item in list_of_items:
        if item[0] == lastname and item[1] == firstname:
            return list_of_items.index(item)


def make_pretty_phone(phone, pattern):
    return re.sub(pattern, r'+7(\2)\4-\6-\8\11\10\12', phone)


pattern = re.compile('(\+7|8){1}\s*\(?(\d{3})\)?(\s*|-*)*(\d{3})(\s*|-*)*(\d{2})(\s*|-*)*(\d{2})(\s*\(*(доб.)(\s)*(\d+))?\)*')


new_contacts_list = []
new_contacts_list.append(contacts_list[0])
contacts_list.pop(0)


for contact in contacts_list:
    full_name = ' '.join(contact[0:3])
    list_of_name = full_name.split(' ')
    checked_name = check_by_name(list_of_name[0], list_of_name[1], new_contacts_list)
    pretty_number = make_pretty_phone(contact[5], pattern)
    new_contact = []
    new_contact.append(list_of_name[0])
    new_contact.append(list_of_name[1])
    new_contact.append(list_of_name[2])
    new_contact.append(contact[3])
    new_contact.append(contact[4])
    new_contact.append(pretty_number)
    new_contact.append(contact[6])

    if checked_name is None:
        new_contacts_list.append(new_contact)
    else:
        i = 0
        while i < len(new_contacts_list[checked_name]):
            if new_contacts_list[checked_name][i] == '':
                new_contacts_list[checked_name][i] = new_contact[i]
            i += 1
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)