from pprint import pp
import csv
import re

from Tools.scripts.generate_opcode_h import header

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def name_phonebook():
  list_name = []
  result = []
  for x in contacts_list[1:]:
    list_names = x[:3]
    list_names = ' '.join(list_names).split()
    last_name = list_names[0]
    first_name = list_names[1]
    if len(list_names) > 2:
      surname = list_names[2]
    if last_name and first_name not in list_name:
      list_name.append(last_name)
      list_name.append(first_name)
      list_name.append(surname)
  for x in range(0,len(list_name),3):
    result.append(list_name[x:x+3])
  return result

def number():
  pattern = re.compile(r"(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?")
  pat_sub = r"+7(\2)\3-\4-\5 \8\9"
  list_number = []
  for x in contacts_list[1:]:
    phone = x[5]
    if phone:
      phone1 = pattern.sub(pat_sub,phone).strip()
      list_number.append(phone1)
    else:
      list_number.append('')
  return list_number

def name_csv():
  name_book = name_phonebook()
  phone_book = number()
  result_list = []
  header = []
  new_list = []
  orgg = []
  pos = []
  email = []
  for x in contacts_list[0]:
    header.append(x)
  for org in contacts_list[1:]:
    orgg.append(org[3])
  for position in contacts_list[1:]:
    pos.append(position[4])
  for emaill in contacts_list[1:]:
    email.append(emaill[6])

  for nam in name_book:
    dict_name = {}
    dict_name['last_name'] = nam[0]
    dict_name['first_name'] = nam[1]
    dict_name['surname'] = nam[2]
    new_list.append(dict_name)
  for idx, x in enumerate(new_list):
    if idx < len(orgg):
      x['organization'] = orgg[idx]
    if idx < len(pos):
      x['position'] = pos[idx]
    if idx < len(phone_book):
      x['phone'] = phone_book[idx]
    if idx < len(email):
      x['email'] = email[idx]

  result_list.append(header)
  for res in new_list:
    result = list(res.values())
    result_list.append(result)


  with open("phonebook1.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result_list)








if __name__=='__main__':
  name_csv()







