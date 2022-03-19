import csv
import re

def read_file(file_name):
  with open(file_name) as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list


def fill_fio_fields(contacts_list):
  for idx, item in enumerate(contacts, start=0):
    if not idx:
      continue
    fio = list()
    for idx1 in range(3):
      if len(item[idx1]):
        fio += item[idx1].split(" ")
    for key, value in enumerate(fio):
      item[key] = value
  return contacts_list


def substitute_phone_numbers(contacts_list):
  for item in contacts_list:
    for col, val in enumerate(item):
      pattern1 = r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})"
      substitution1 = r"\1(\2)\3-\4-\5"
      item[col] = re.sub(pattern1, substitution1, val)
      if "доб" in val:
          pattern2 = r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
          substitution2 = r"\1(\2)\3-\4-\5 \8\9\11"
          item[col] = re.sub(pattern2, substitution2, val)
  return contacts_list


def get_unique_values(contacts_list):
  unique_value = dict()
  dublicate_full_name = dict()
  for item in contacts_list:
    full_name = item[0] + " " + item[1]
    if full_name in unique_value:
      dublicate_full_name[full_name] = item
    else:
      unique_value[full_name] = item
  for item in unique_value:
    if(item in dublicate_full_name) and (unique_value[item][0] == dublicate_full_name[item][0]) \
            and (unique_value[item][1] == dublicate_full_name[item][1]):
      if not unique_value[item][3] and bool(dublicate_full_name[item][3]):
        unique_value[item][3] = dublicate_full_name[item][3]
      if not unique_value[item][4] and bool(dublicate_full_name[item][4]):
        unique_value[item][4] = dublicate_full_name[item][4]
      if not unique_value[item][5] and bool(dublicate_full_name[item][5]):
        unique_value[item][5] = dublicate_full_name[item][5]
      if not unique_value[item][6] and bool(dublicate_full_name[item][6]):
        unique_value[item][6] = dublicate_full_name[item][6]
  return unique_value



def write_file(unique_value):
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    results_list = list()
    for key, value in unique_value.items():
      results_list.append(value)
    datawriter.writerows(results_list)
  return results_list


if __name__ == '__main__':
  contacts = read_file("phonebook_raw.csv")
  contacts = fill_fio_fields(contacts)
  contacts = substitute_phone_numbers(contacts)
  contacts = get_unique_values(contacts)
  contacts = write_file(contacts)





